import pytest
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


class TestAutoDictId:
    """自动字典ID生成测试类"""

    def test_auto_generated_dict_id(self):
        """测试自动生成的字典ID"""
        # 验证自动生成的ID字段存在且为字符串类型
        assert hasattr(UserStatus.INACTIVE, 'id')
        assert isinstance(UserStatus.INACTIVE.id, str)
        # 验证其他字段正确保留（通过value字典访问）
        assert UserStatus.INACTIVE.value['name'] == 'Inactive'
        assert UserStatus.INACTIVE.value['description'] == 'Disabled account'

    def test_info_method(self):
        """测试info方法"""
        # 验证info方法返回正确的信息
        info = UserStatus.ACTIVE.info()
        assert isinstance(info, dict)
        assert info['module'] == 'tests.id_utils.test_auto_dict_id'
        assert info['class'] == 'UserStatus'
        assert info['member'] == 'ACTIVE'

    def test_callback_method(self):
        """测试callback方法"""
        # 验证callback方法返回正确的字典值
        callback_value = UserStatus.INACTIVE.callback(
            description='Deactivated account'
        )
        assert isinstance(callback_value, dict)
        assert callback_value['id'] == UserStatus.INACTIVE.id
        assert callback_value['name'] == 'Inactive'
        assert callback_value['description'] == 'Deactivated account'

    def test_callback_method_with_invalid_key(self):
        """测试callback方法使用无效键时的行为"""
        # 验证使用无效键时抛出KeyError异常
        with pytest.raises(KeyError):
            UserStatus.INACTIVE.callback(invalid_key='value')

    def test_get_info_by_id(self):
        """测试根据ID获取信息的功能"""
        # 验证可以根据ID获取信息
        info = get_info_by_id(UserStatus.INACTIVE.value)
        assert info is not None
        assert isinstance(info, dict)
        assert info['module'] == 'tests.id_utils.test_auto_dict_id'
        assert info['class'] == 'UserStatus'
        assert info['member'] == 'INACTIVE'

    def test_order_status_fields(self):
        """测试订单状态字段"""
        # 验证订单状态字段正确生成
        assert hasattr(OrderStatus.CREATED, 'order_id')
        assert isinstance(OrderStatus.CREATED.order_id, str)
        assert OrderStatus.CREATED.state == 'New'

        assert hasattr(OrderStatus.PROCESSING, 'order_id')
        assert isinstance(OrderStatus.PROCESSING.order_id, str)
        assert OrderStatus.PROCESSING.state == 'In Progress'

        assert hasattr(OrderStatus.COMPLETED, 'order_id')
        assert isinstance(OrderStatus.COMPLETED.order_id, str)
        assert OrderStatus.COMPLETED.state == 'Fulfilled'

    def test_unique_dict_ids(self):
        """测试所有字典ID的唯一性"""
        # 验证所有枚举类中的ID都是唯一的
        all_ids = set()
        for enum_class in [UserStatus, OrderStatus]:
            for member in enum_class:
                id_str = str(member.value)
                assert id_str not in all_ids, f'Duplicate ID found: {id_str}'
                all_ids.add(id_str)

    def test_id_registry(self):
        """测试字典ID注册表"""
        # 验证ID在注册表中正确注册
        from feffery_dash_utils.id_utils.auto_dict_id import (
            auto_dict_id_registry,
        )

        assert str(UserStatus.INACTIVE.value) in auto_dict_id_registry
        assert str(UserStatus.ACTIVE.value) in auto_dict_id_registry
        assert str(OrderStatus.CREATED.value) in auto_dict_id_registry
