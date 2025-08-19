from typing import Any, Dict, Union
from .auto_id import auto_id_registry
from .auto_dict_id import auto_dict_id_registry


def get_info_by_id(
    id: Union[str, Dict[str, Any]],
) -> Union[Dict[str, Any], None]:
    """
    根据ID获取枚举成员信息

    :param id: 枚举成员的ID字符串或字典
    :return: 包含枚举成员信息的字典
    """
    if isinstance(id, str):
        if id in auto_id_registry:
            module_name, enum_class_name, member_name = auto_id_registry[id]
            return {
                'module': module_name,
                'class': enum_class_name,
                'member': member_name,
                'value': id,
            }
    elif isinstance(id, dict):
        id_value = str(id)
        if id_value in auto_dict_id_registry:
            module_name, enum_class_name, member_name = auto_dict_id_registry[
                id_value
            ]
            return {
                'module': module_name,
                'class': enum_class_name,
                'member': member_name,
                'value': id,
            }

    return None
