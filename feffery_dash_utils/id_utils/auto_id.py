from enum import Enum, EnumMeta, _EnumDict
from typing import cast, Dict, Type
from .common import Auto, generate_unique_id

# 全局id注册表 {id_value: (module_name, enum_class_name, member_name)}
auto_id_registry: Dict[str, tuple] = {}


class _UniqueIdEnumMeta(EnumMeta):
    """自定义元类，确保所有枚举成员具有唯一id值"""

    def __new__(mcs, name: str, bases: tuple, attrs: _EnumDict) -> Type:
        # 获取模块名和完整类名
        module = attrs.get('__module__', '__main__')
        full_class_name = f'{module}-{name}'.replace('.', '-')

        # 临时存储处理后的成员
        processed_members = {}

        # 处理类属性
        for member_name, member_value in attrs.items():
            if member_name.startswith('__') or not member_name.isupper():
                # 跳过非成员属性
                continue

            # 处理Auto标记 - 生成基于类名和成员名的ID字符串
            if member_value is Auto:
                new_id = generate_unique_id(full_class_name, member_name)
                # 检查唯一性
                if new_id in auto_id_registry:
                    existing = auto_id_registry[new_id]
                    raise ValueError(
                        f'❌ ID冲突! {full_class_name}.{member_name} 与 {existing[0]}.{existing[1]} 使用了相同的ID: {new_id}'
                    )
                auto_id_registry[new_id] = (module, name, member_name)
                processed_members[member_name] = new_id

            # 处理显式字符串值
            elif isinstance(member_value, str):
                if member_value in auto_id_registry:
                    existing = auto_id_registry[member_value]
                    raise ValueError(
                        f"❌ ID冲突! '{full_class_name}.{member_name}' 与 '{existing[0]}.{existing[1]}' 使用了相同的ID: {member_value}"
                    )
                auto_id_registry[member_value] = (module, name, member_name)
                processed_members[member_name] = member_value

        # 更新属性并创建枚举类
        # Python3.10+-版本兼容性处理：清理_member_names并重新添加枚举成员
        # 清理_member_names中的枚举成员
        member_names = getattr(attrs, '_member_names', None)
        if member_names is not None:
            # Python 3.11及以上中_member_names是字典，Python 3.10及以下中是列表
            if isinstance(member_names, dict):
                for member_name in processed_members.keys():
                    if member_name in member_names:
                        del member_names[member_name]
            elif isinstance(member_names, list):
                # 对于列表，我们需要移除对应的成员名
                for member_name in processed_members.keys():
                    while member_name in member_names:
                        member_names.remove(member_name)
        # 删除attrs中的枚举成员
        for member_name in processed_members.keys():
            if member_name in attrs:
                del attrs[member_name]
        # 添加处理后的枚举成员
        for member_name, member_value in processed_members.items():
            attrs[member_name] = member_value
        cls = cast(Type, super().__new__(mcs, name, bases, attrs))

        return cls


class AutoUniqueIdEnum(Enum, metaclass=_UniqueIdEnumMeta):
    """
    用户继承的基类，自动应用唯一id元类
    """

    def info(self) -> Dict[str, str]:
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

    def callback(self) -> str:
        """
        获取当前成员在回调函数中的值

        :return: 当前成员在回调函数中的值
        """
        return self.value
