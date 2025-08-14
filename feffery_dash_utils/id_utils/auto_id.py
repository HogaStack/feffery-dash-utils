import uuid
from enum import Enum, EnumMeta
from typing import Any, Dict

# 全局id注册表 {id_value: (enum_class_name, member_name)}
_id_registry: Dict[uuid.UUID, tuple] = {}


class AutoId:
    """
    标记类，表示枚举成员需要自动生成id
    """

    pass


class _UniqueIdEnumMeta(EnumMeta):
    """
    自定义元类，确保所有枚举成员具有唯一id值
    """

    def __new__(mcs, name: str, bases: tuple, attrs: Dict[str, Any]):
        # 临时存储处理后的成员
        processed_members = {}

        for member_name, value in attrs.items():
            if member_name.startswith('__') or not member_name.isupper():
                # 跳过非成员属性
                continue

            # 处理AutoId标记
            if value is AutoId:
                new_id = mcs._generate_unique_id(name, member_name)
                processed_members[member_name] = new_id

            # 处理显式UUID值
            elif isinstance(value, (uuid.UUID, str)):
                id_val = (
                    value if isinstance(value, uuid.UUID) else uuid.UUID(value)
                )
                if id_val in _id_registry:
                    existing = _id_registry[id_val]
                    raise ValueError(
                        f'❌ id冲突! {name}.{member_name} 与 {existing[0]}.{existing[1]} 使用了相同的id: {id_val}'
                    )
                _id_registry[id_val] = (name, member_name)
                processed_members[member_name] = id_val

        # 更新属性并创建枚举类
        attrs.update(processed_members)
        cls = super().__new__(mcs, name, bases, attrs)
        return cls

    @staticmethod
    def _generate_unique_id(enum_name: str, member_name: str) -> uuid.UUID:
        """
        生成唯一id并注册

        :param enum_name: 枚举类名
        :param member_name: 成员名
        :return: 唯一id
        """
        while True:
            new_id = uuid.uuid4()
            if new_id not in _id_registry:
                _id_registry[new_id] = (enum_name, member_name)
                return new_id


class UniqueIdEnum(Enum, metaclass=_UniqueIdEnumMeta):
    """
    用户继承的基类，自动应用唯一id元类
    """

    pass
