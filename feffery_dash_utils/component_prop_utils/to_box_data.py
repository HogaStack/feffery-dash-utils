import numpy as np


def to_box_data(raw_data) -> dict:
    """将原始数组转换为适用于fact.AntdBox参数data数据项格式的结果

    Args:
        raw_data: 原始数据数组

    Returns:
        dict: 转化结果数据项
    """

    # 转换为numpy数组
    data = np.array(raw_data)

    # 计算四分位数
    q1 = np.percentile(data, 25)
    q2 = np.median(data)
    q3 = np.percentile(data, 75)

    # 计算四分位距
    iqr = q3 - q1

    # 计算上下边界
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # 提取异常值
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    # 返回适用于fact.AntdBox参数data数据项格式的结果
    return {
        'low': lower_bound,
        'q1': q1,
        'median': q2,
        'q3': q3,
        'high': upper_bound,
        'outliers': list(outliers),
    }
