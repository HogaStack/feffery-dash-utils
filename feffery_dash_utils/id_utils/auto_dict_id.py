from enum import EnumMeta, Enum
from typing import Any, cast, Dict, Type
from .common import Auto, generate_unique_id


# 全局字典id键对应值注册表 {dict_id_value: (module_name, enum_class_name, member_name)}
auto_dict_id_registry: Dict[str, tuple] = {}


class Match:
    """
    标记类，表示枚举成员需要匹配其他成员的值
    """

    pass


class _UniqueDictIdEnumMeta(EnumMeta):
    """
    元类处理自动值生成和唯一性检查
    """

    def __new__(mcs, name: str, bases: tuple, attrs: Dict[str, Any]) -> Type:
        # 获取模块名和完整类名
        module = attrs.get('__module__', '__main__')
        full_class_name = f'{module}-{name}'
        # 临时存储处理后的成员
        processed_members = {}
        match_values = {}

        # 处理类属性
        for member_name, member_value in attrs.items():
            if member_name.startswith('__') or not member_name.isupper():
                # 跳过非成员属性
                continue
            if isinstance(member_value, dict):
                # 处理字典类型的值
                processed_value, new_match_values = mcs._process_dict_value(
                    full_class_name, member_name, member_value, match_values
                )
                # 检查唯一性
                processed_value_str = str(processed_value)
                if processed_value_str in auto_dict_id_registry:
                    existing = auto_dict_id_registry[processed_value_str]
                    raise ValueError(
                        f'❌ ID冲突! {full_class_name}.{member_name} 与 {existing[0]}.{existing[1]} 使用了相同的ID: {processed_value_str}'
                    )
                auto_dict_id_registry[processed_value_str] = (module, name, member_name)
                processed_members[member_name] = processed_value
                match_values.update(new_match_values)

        # 更新属性并创建枚举类
        attrs.update(processed_members)
        cls = cast(Type, super().__new__(mcs, name, bases, attrs))

        return cls

    @staticmethod
    def _process_dict_value(
        full_class_name: str,
        member_name: str,
        value_dict: dict,
        match_values: Dict[str, str],
    ) -> Dict[str, Any]:
        """
        处理字典值

        :param full_class_name: 完整类名
        :param member_name: 成员名
        :param value_dict: 成员值
        :param match_values: 已匹配的值字典
        :return: 生成的id字符串
        """

        processed_dict = {}
        auto_fields = []
        match_fields = []
        new_match_fields = {}

        # 分离自动生成字段和固定字段
        for k, v in value_dict.items():
            if v is Auto:
                auto_fields.append(k)
            elif v is Match:
                match_fields.append(k)
            else:
                processed_dict[k] = v

        # 为每个自动字段生成唯一值
        for field in auto_fields:
            new_value = generate_unique_id(full_class_name, member_name)
            processed_dict[field] = new_value

        for field in match_fields:
            if field in match_values:
                # 使用已存在的Match字段值
                processed_dict[field] = match_values[field]
            else:
                # 首次使用Match字段，生成新的唯一值
                new_value = generate_unique_id(full_class_name, member_name)
                processed_dict[field] = new_value
                new_match_fields[field] = new_value

        return processed_dict, new_match_fields


class AutoUniqueDictIdEnum(Enum, metaclass=_UniqueDictIdEnumMeta):
    """
    支持自动生成唯一字典id的枚举基类
    """

    def __init__(self, value_dict) -> None:
        # 直接存储到__dict__避免触发__getattr__
        self.__dict__['_value_dict'] = value_dict

    def __getattr__(self, name) -> Any:
        # 安全访问_value_dict属性
        value_dict = self.__dict__.get('_value_dict')
        if value_dict is not None and name in value_dict:
            return value_dict[name]
        raise AttributeError(
            f"❌ 枚举成员 '{self.__class__.__name__}' 值中没有键 '{name}'"
        )

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}: {self.value}>'

    def info(self) -> Dict[str, Any]:
        """
        获取当前成员的id信息

        :return: 包含id信息的字典
        """
        return {
            'module': self.__class__.__module__,
            'class': self.__class__.__name__,
            'member': self.name,
            'value': self.value,
        }

    def callback(self, **replacements) -> Dict[str, Any]:
        """
        获取当前成员在回调函数中的值

        :param replacements: 替换成员值字典中的键值对
        :return: 当前成员在回调函数中的值
        """
        new_dict = self.value.copy()
        for key, new_value in replacements.items():
            if key not in new_dict:
                raise KeyError(f"❌ 枚举值中没有键 '{key}'")
            new_dict[key] = new_value
        return new_dict
