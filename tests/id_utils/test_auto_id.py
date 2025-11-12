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


class TestAutoId:
    """自动ID生成测试类"""

    def test_auto_generated_id(self):
        """测试自动生成的ID"""
        # 验证自动生成的ID是字符串类型
        assert isinstance(Status.PENDING.value, str)
        # 验证自动生成的ID包含类名和成员名
        assert 'Status-PENDING' in Status.PENDING.value

    def test_explicit_string_id(self):
        """测试显式指定的字符串ID"""
        # 验证显式指定的字符串ID
        assert Status.RUNNING.value == 'a0b1c2d3-e4f5-6789-0123-456789abcdef'

    def test_explicit_uuid_object_id(self):
        """测试显式指定的UUID对象ID"""
        # 验证显式指定的UUID对象ID
        expected_uuid = uuid.UUID('12345678-1234-5678-1234-567812345678')
        assert Status.COMPLETED.value == expected_uuid

    def test_info_method(self):
        """测试info方法"""
        # 验证info方法返回正确的信息
        info = Status.RUNNING.info()
        assert isinstance(info, dict)
        assert info['module'] == 'tests.id_utils.test_auto_id'
        assert info['class'] == 'Status'
        assert info['member'] == 'RUNNING'
        assert info['value'] == 'a0b1c2d3-e4f5-6789-0123-456789abcdef'

    def test_callback_method(self):
        """测试callback方法"""
        # 验证callback方法返回正确的值
        callback_value = Priority.MEDIUM.callback()
        assert callback_value == Priority.MEDIUM.value

    def test_get_info_by_id(self):
        """测试根据ID获取信息的功能"""
        # 验证可以根据ID获取信息
        info = get_info_by_id(Status.PENDING.value)
        assert info is not None
        assert isinstance(info, dict)
        assert info['module'] == 'tests.id_utils.test_auto_id'
        assert info['class'] == 'Status'
        assert info['member'] == 'PENDING'

    def test_unique_ids(self):
        """测试所有ID的唯一性"""
        # 验证所有枚举类中的ID都是唯一的
        all_uuids = {m.value for e in [Status, Priority] for m in e}
        expected_count = len(list(Status)) + len(list(Priority))
        assert len(all_uuids) == expected_count

    def test_id_registry_for_auto_and_string_ids(self):
        """测试ID注册表中自动和字符串ID的注册"""
        # 验证自动和字符串ID在注册表中正确注册
        from feffery_dash_utils.id_utils.auto_id import auto_id_registry

        assert Status.PENDING.value in auto_id_registry
        assert Status.RUNNING.value in auto_id_registry
