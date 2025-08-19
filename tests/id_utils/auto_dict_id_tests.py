from feffery_dash_utils.id_utils import (
    Auto,
    AutoUniqueDictIdEnum,
    get_info_by_id,
)


class UserStatus(AutoUniqueDictIdEnum):
    INACTIVE = {
        'id': Auto,
        'name': 'Inactive',
        'description': 'Disabled account',
    }
    ACTIVE = {'id': Auto, 'name': 'Active', 'description': 'Enabled account'}
    PENDING = {
        'id': Auto,
        'name': 'Pending',
        'description': 'Awaiting activation',
    }


class OrderStatus(AutoUniqueDictIdEnum):
    CREATED = {'order_id': Auto, 'state': 'New'}
    PROCESSING = {'order_id': Auto, 'state': 'In Progress'}
    COMPLETED = {'order_id': Auto, 'state': 'Fulfilled'}


if __name__ == '__main__':
    # 获取自动生成的字段值
    print(UserStatus.INACTIVE.id)
    # 获取成员信息
    print(UserStatus.ACTIVE.info())
    # 获取在回调函数中的值
    callback_value = UserStatus.INACTIVE.callback(
        description='Deactivated account'
    )
    print(callback_value)
    # 根据id查找信息
    info = get_info_by_id(UserStatus.INACTIVE.value)
    print(info)
    # 直接获取字段值
    order = OrderStatus.CREATED
    print(f'Order {order.order_id} is {order.state}')
