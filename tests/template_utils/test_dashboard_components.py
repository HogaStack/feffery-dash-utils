import feffery_antd_charts as fact
import feffery_antd_components as fac
import random
from dash import Dash, html
from feffery_dash_utils.template_utils.dashboard_components import (
    welcome_card,
    blank_card,
    index_card,
    simple_chart_card,
)


def test_welcome_card_component(dash_duo):
    """测试欢迎卡片组件"""
    app = Dash(__name__)

    app.layout = html.Div(
        welcome_card(
            title='欢迎用户Feffery，又是元气满满的一天',
            description=[
                '您有8条未处理的消息，点击',
                html.A('此处'),
                '查看。',
            ],
            extra=fac.AntdDescriptions(
                items=[
                    {
                        'label': '项目数',
                        'children': '12',
                    },
                    {
                        'label': '待办项',
                        'children': '5 / 17',
                    },
                    {
                        'label': '消息',
                        'children': '8',
                    },
                ],
                column=1,
                size='small',
                style=dict(width=125),
                styles={
                    'content': dict(fontSize=16),
                    'label': dict(fontSize=16),
                },
            ),
            root_id='welcome-card',
            rootStyle=dict(
                background='linear-gradient(273deg,#abdcff,#0396ff)'
            ),
            titleStyle=dict(color='#fff'),
            descriptionStyle=dict(color='#fff'),
        ),
        style=dict(padding=50),
    )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#welcome-card')

    # 验证欢迎卡片渲染成功
    welcome_card_element = dash_duo.find_element('#welcome-card')
    assert welcome_card_element is not None


def test_blank_card_component(dash_duo):
    """测试空白卡片组件"""
    app = Dash(__name__)

    app.layout = html.Div(
        blank_card(
            backgroundImage='https://images.unsplash.com/photo-1527066579998-dbbae57f45ce?q=80&w=1987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            root_id='blank-card',
            rootStyle=dict(height=200),
        ),
        style=dict(padding=50),
    )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#blank-card')

    # 验证空白卡片渲染成功
    blank_card_element = dash_duo.find_element('#blank-card')
    assert blank_card_element is not None


def test_index_card_component(dash_duo):
    """测试指标卡片组件"""
    app = Dash(__name__)

    app.layout = html.Div(
        [
            fac.AntdRow(
                [
                    fac.AntdCol(
                        index_card(
                            index_description='指标描述示例',
                            index_value='99.99%',
                            extra_content=fac.AntdCenter(
                                fac.AntdProgress(percent=80),
                                style=dict(height='100%'),
                            ),
                            footer_content='日销售额 ￥12,423',
                            root_id='index-card-1',
                        ),
                        span=6,
                    ),
                    fac.AntdCol(
                        index_card(
                            index_description='指标描述示例',
                            index_value='88.88%',
                            extra_content=fact.AntdTinyArea(
                                data=[
                                    random.randint(50, 100) for _ in range(20)
                                ],
                                height=60,
                                smooth=True,
                                padding=0,
                                appendPadding=0,
                            ),
                            footer_content='日销售额 ￥12,423',
                            root_id='index-card-2',
                        ),
                        span=6,
                    ),
                ],
                gutter=18,
            )
        ],
        style=dict(padding=50),
    )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#index-card-1')
    dash_duo.wait_for_element('#index-card-2')

    # 验证指标卡片渲染成功
    index_card_1_element = dash_duo.find_element('#index-card-1')
    index_card_2_element = dash_duo.find_element('#index-card-2')
    assert index_card_1_element is not None
    assert index_card_2_element is not None


def test_simple_chart_card_component(dash_duo):
    """测试简单图表卡片组件"""
    app = Dash(__name__)

    app.layout = html.Div(
        simple_chart_card(
            title='标题测试',
            description='辅助描述信息',
            chart=fact.AntdColumn(
                data=[
                    {
                        'date': f'2020-0{i}',
                        'y': random.randint(50, 100),
                    }
                    for i in range(1, 10)
                ],
                xField='date',
                yField='y',
                color='#1677ff',
            ),
            extra=fac.AntdButton('测试', type='link'),
            root_id='chart-card',
        ),
        style=dict(padding=50),
    )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#chart-card')

    # 验证图表卡片渲染成功
    chart_card_element = dash_duo.find_element('#chart-card')
    assert chart_card_element is not None
