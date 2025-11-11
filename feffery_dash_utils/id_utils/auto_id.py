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
        attrs.update(processed_members)
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
