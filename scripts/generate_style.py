"""
cd scripts
python generate_style.py
"""

import re
from DrissionPage import SessionPage

page = SessionPage()

# 访问中文目标页面
page.get('https://www.w3school.com.cn/cssref/index.asp')

raw_texts = [
    item.raw_text
    for item in page.eles('xpath://table[@class="dataintable"]//td')
]

# 构造中文css常用属性字典
zh_cn_styles = {
    name: description
    for name, description in zip(raw_texts[:-1:2], raw_texts[1::2])
}

# 访问英文目标页面
page.get('https://www.w3schools.com/cssref/index.php')

raw_texts = [
    item.raw_text
    for item in page.eles('xpath://table[contains(@class, "ws-table-all")]//td')
]

# 构造英文css常用属性字典
en_us_styles = {
    name: description
    for name, description in zip(raw_texts[:-1:2], raw_texts[1::2])
}


# 合并中英文css常用属性字典
styles = {
    ''.join(
        [s if i == 0 else s.capitalize() for i, s in enumerate(key.split('-'))]
    ): '{}  {}'.format(
        zh_cn_styles[key].replace('\n', ' '),
        re.sub(
            ' {2,}',
            ' ',
            en_us_styles[key].replace('\n', ' '),
        ),
    )
    for key in (set(zh_cn_styles.keys()) & set(en_us_styles.keys()))
    if re.match(r'[\-a-z]+', key)
}

# 生成style_utils.py文件

raw_code = '''import inspect
from cssutils import parseString

def style(
    rawCSS: str = None,
<函数参数定义>
    **kwargs
) -> dict:
    """
    Args:
        - rawCSS: 接受原始CSS字符串，用于自动解析相应的样式属性键值对。  Accepts the original CSS string to automatically parse the corresponding style property key-value pairs
<函数参数说明>
"""

    frame = inspect.currentframe()
    try:
        argvalues = inspect.getargvalues(frame)
        args_dict = dict(argvalues.locals)
        kwargs = args_dict.pop('kwargs', {})
        # 去除None值属性
        args = {key: value for key, value in args_dict.items() if value is not None and key not in ['rawCSS', 'frame', 'argvalues', 'args_dict']}
    finally:
        del frame

    # 处理针对rawCSS的自动解析
    args_from_css = {}
    if rawCSS:
        css_rules = parseString(rawCSS)
        for rule in css_rules:
            if rule.type == rule.STYLE_RULE:
                args_from_css = {
                    css_prop.name: css_prop.value
                    for css_prop in rule.style
                }
    # 将args_from_css中的键名格式转换为小驼峰格式
    args_from_css = {
        ''.join(
            [
                s if i == 0 else s.capitalize()
                for i, s in enumerate(key.split('-'))
            ]
        ): value
        for key, value in args_from_css.items()
    }

    return {**args_from_css, **args, **kwargs}
'''

# 生成<函数参数定义>
raw_code = raw_code.replace(
    '<函数参数定义>',
    '\n'.join(['    {}=None,'.format(key) for key in sorted(styles.keys())]),
)

# 生成<函数参数说明>
raw_code = raw_code.replace(
    '<函数参数说明>',
    '\n'.join(
        [
            '        - {}: {}'.format(key, styles[key])
            for key in sorted(styles.keys())
        ]
    ),
)

with open(
    '../feffery_dash_utils/style_utils/style.py',
    'w',
    encoding='utf-8',
) as f:
    f.write(raw_code)
    print('style.py生成成功')
