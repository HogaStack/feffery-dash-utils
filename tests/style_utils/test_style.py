from feffery_dash_utils.style_utils import style


class TestStyleUtils:
    """样式工具测试类"""

    def test_style_with_keyword_arguments(self):
        """测试使用关键字参数生成样式字典"""
        result = style(
            fontSize=20,
            background='yellow',
        )
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证样式属性是否正确设置
        assert 'fontSize' in result
        assert result['fontSize'] == 20
        assert 'background' in result
        assert result['background'] == 'yellow'

    def test_style_with_raw_css_string(self):
        """测试使用原始CSS字符串生成样式字典"""
        css_string = """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}"""
        result = style(css_string)
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证CSS属性是否正确解析
        assert 'width' in result
        assert result['width'] == '91.46%'
        assert 'marginLeft' in result
        assert result['marginLeft'] == '4.27%'
        assert 'marginBottom' in result
        assert result['marginBottom'] == '5%'
        assert 'position' in result
        assert result['position'] == 'relative'

    def test_style_with_raw_css_string_and_keyword_arguments(self):
        """测试同时使用原始CSS字符串和关键字参数生成样式字典"""
        css_string = """
.IvkwhTOsc9wu6RdvHESR .yK52Sq0w7wspWaS28YNl {
    width: 91.46%;
    margin-left: 4.27%;
    margin-bottom: 5%;
    position: relative;
}"""
        result = style(
            css_string,
            fontSize=18.8,
        )
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证CSS属性是否正确解析
        assert 'width' in result
        assert result['width'] == '91.46%'
        assert 'marginLeft' in result
        assert result['marginLeft'] == '4.27%'
        assert 'marginBottom' in result
        assert result['marginBottom'] == '5%'
        assert 'position' in result
        assert result['position'] == 'relative'
        # 验证关键字参数是否正确应用
        assert 'fontSize' in result
        assert result['fontSize'] == 18.8

    def test_style_with_none_values(self):
        """测试处理None值的情况"""
        result = style(fontSize=20, background=None, color='red')
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证非None值是否正确设置
        assert 'fontSize' in result
        assert result['fontSize'] == 20
        assert 'color' in result
        assert result['color'] == 'red'
        # 验证None值是否被忽略
        assert 'background' not in result

    def test_style_empty_call(self):
        """测试空调用的情况"""
        result = style()
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证返回空字典
        assert result == {}

    def test_style_camel_case_conversion(self):
        """测试CSS属性名到驼峰命名的转换"""
        css_string = """
.example {
    margin-left: 10px;
    background-color: blue;
    font-size: 16px;
    z-index: 10;
}"""
        result = style(css_string)
        # 验证返回值是否为字典
        assert isinstance(result, dict)
        # 验证CSS属性名是否正确转换为驼峰命名
        assert 'marginLeft' in result
        assert result['marginLeft'] == '10px'
        assert 'backgroundColor' in result
        assert result['backgroundColor'] == 'blue'
        assert 'fontSize' in result
        assert result['fontSize'] == '16px'
        assert 'zIndex' in result
        assert result['zIndex'] == '10'
