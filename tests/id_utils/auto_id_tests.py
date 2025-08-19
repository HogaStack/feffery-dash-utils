import uuid
from feffery_dash_utils.id_utils import Auto, AutoUniqueIdEnum, get_info_by_id


class Status(AutoUniqueIdEnum):
    PENDING = Auto  # 自动生成UUID
    RUNNING = 'a0b1c2d3-e4f5-6789-0123-456789abcdef'  # 显式指定UUID字符串
    COMPLETED = uuid.UUID(
        '12345678-1234-5678-1234-567812345678'
    )  # 显式指定UUID对象


class Priority(AutoUniqueIdEnum):
    LOW = Auto
    MEDIUM = Auto
    HIGH = Auto


if __name__ == '__main__':
    # 直接访问成员值
    print(Status.PENDING.value)
    # 获取成员信息
    print(Status.RUNNING.info())
    # 获取在回调函数中的值
    callback_value = Priority.MEDIUM.callback()
    print(callback_value)
    # 根据id查找信息
    info = get_info_by_id(Status.PENDING.value)
    print(info)

    # 检查唯一性
    all_uuids = {m.value for e in [Status, Priority] for m in e}
    # 输出 True
    print(len(all_uuids) == len(list(Status)) + len(list(Priority)))
