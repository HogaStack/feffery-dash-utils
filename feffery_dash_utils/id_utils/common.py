import uuid


class Auto:
    """
    标记类，表示枚举成员需要自动生成id
    """

    pass


def generate_unique_id(full_class_name: str, member_name: str) -> str:
    """
    生成基于类名和成员名的ID字符串

    :param full_class_name: 完整类名
    :param member_name: 成员名
    :return: 生成的ID字符串
    """
    # 格式: "类名-成员名-随机UUID4"
    return f'{full_class_name}-{member_name}-{uuid.uuid4()}'
