import uuid
from feffery_dash_utils.id_utils import AutoId, UniqueIdEnum


class Status(UniqueIdEnum):
    PENDING = AutoId  # 自动生成UUID
    RUNNING = 'a0b1c2d3-e4f5-6789-0123-456789abcdef'  # 显式指定UUID字符串
    COMPLETED = uuid.UUID(
        '12345678-1234-5678-1234-567812345678'
    )  # 显式指定UUID对象


class Priority(UniqueIdEnum):
    LOW = AutoId
    MEDIUM = AutoId
    HIGH = AutoId


if __name__ == '__main__':
    # 直接访问成员值
    print(Status.PENDING.value)
    print(Status.RUNNING.value)
    print(Priority.HIGH.value)

    # 检查唯一性
    all_uuids = {m.value for e in [Status, Priority] for m in e}
    # 输出 True
    print(len(all_uuids) == len(list(Status)) + len(list(Priority)))
