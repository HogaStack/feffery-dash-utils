import numpy as np
import pytest
from feffery_dash_utils.component_prop_utils import to_box_data


def test_to_box_data_basic():
    """测试基本的 to_box_data 功能"""
    # 准备测试数据
    raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 调用函数
    result = to_box_data(raw_data)

    # 验证结果
    assert isinstance(result, dict)
    assert 'low' in result
    assert 'q1' in result
    assert 'median' in result
    assert 'q3' in result
    assert 'high' in result
    assert 'outliers' in result

    # 验证基本统计值
    assert result['median'] == 5.5  # 中位数
    assert result['q1'] == 3.25  # 第一四分位数
    assert result['q3'] == 7.75  # 第三四分位数


def test_to_box_data_with_outliers():
    """测试包含异常值的数据"""
    # 准备包含异常值的测试数据
    raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]  # 100 是异常值

    # 调用函数
    result = to_box_data(raw_data)

    # 验证结果
    assert isinstance(result, dict)
    assert 100 in result['outliers']  # 异常值应该被检测到


def test_to_box_data_empty_list():
    """测试空列表输入会抛出异常"""
    # 准备空列表数据
    raw_data = []

    # 验证会抛出 ValueError 异常
    with pytest.raises(ValueError, match="输入数组不能为空"):
        to_box_data(raw_data)


def test_to_box_data_single_value():
    """测试单个值输入会抛出异常"""
    # 准备单个值数据
    raw_data = [5]

    # 验证会抛出 ValueError 异常
    with pytest.raises(ValueError, match="输入数组必须包含至少两个元素才能计算箱线图数据"):
        to_box_data(raw_data)


def test_to_box_data_negative_values():
    """测试负数值输入"""
    # 准备负数值数据
    raw_data = [-10, -5, 0, 5, 10]

    # 调用函数
    result = to_box_data(raw_data)

    # 验证结果
    assert isinstance(result, dict)
    assert result['median'] == 0
    assert result['q1'] == -5
    assert result['q3'] == 5


def test_to_box_data_numpy_array():
    """测试 numpy 数组输入"""
    # 准备 numpy 数组数据
    raw_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # 调用函数
    result = to_box_data(raw_data)

    # 验证结果
    assert isinstance(result, dict)
    assert result['median'] == 5.5
    assert result['q1'] == 3.25
    assert result['q3'] == 7.75


def test_to_box_data_identical_values():
    """测试所有值都相同的数组"""
    # 准备相同值的数据
    raw_data = [5, 5, 5, 5, 5]

    # 调用函数
    result = to_box_data(raw_data)

    # 验证结果
    assert isinstance(result, dict)
    assert result['median'] == 5
    assert result['q1'] == 5
    assert result['q3'] == 5
    assert result['low'] == 5
    assert result['high'] == 5
    assert result['outliers'] == []
