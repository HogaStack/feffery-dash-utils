import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import Dash, html
from dash.dependencies import Input, Output
from feffery_dash_utils.i18n_utils import Translator
from flask import request


def test_i18n_chinese_locale(dash_duo):
    """测试中文本地化功能"""

    app = Dash(__name__, suppress_callback_exceptions=True)

    translator = Translator(translations='./tests/i18n_utils/locales.json')

    app.layout = lambda: html.Div(
        [
            fuc.FefferyCookie(
                id='current-locale',
                cookieKey=translator.cookie_name,
                expires=3600 * 24 * 365,
            ),
            fuc.FefferyReload(id='page-reload'),
            html.Div(id='page-container'),
        ],
        style={'padding': 50},
    )

    @app.callback(
        Output('page-container', 'children'),
        Input('page-container', 'id'),
    )
    def render(_):
        current_locale = request.cookies.get(translator.cookie_name)
        current_locale = current_locale or 'zh-cn'

        return fac.AntdSpace(
            [
                fac.AntdButton(
                    (
                        '切换到英语'
                        if current_locale == 'zh-cn'
                        else 'switch to japanese'
                        if current_locale == 'en-us'
                        else '中国語を切り替えます'
                    ),
                    type='primary',
                    id='switch-button',
                    clickExecuteJsString="""
window.dash_clientside.set_props(
    'current-locale',
    {
        value: '%s'
    }
)
window.dash_clientside.set_props(
    'page-reload',
    {
        reload: true
    }
)
"""
                    % (
                        'en-us'
                        if current_locale == 'zh-cn'
                        else 'jp'
                        if current_locale == 'en-us'
                        else 'zh-cn'
                    ),
                ),
                fac.AntdAlert(
                    type='info',
                    showIcon=True,
                    message=translator.t('示例警告消息'),
                    description=translator.t('示例警告描述'),
                    id='test-alert',
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#page-container')

    # 验证中文内容显示正确
    dash_duo.wait_for_text_to_equal('#switch-button', '切换到英语')
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-message', '示例警告消息'
    )
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-description', '示例警告描述'
    )


def test_i18n_english_locale(dash_duo):
    """测试英文本地化功能"""
    app = Dash(__name__, suppress_callback_exceptions=True)

    translator = Translator(translations='./tests/i18n_utils/locales.json')

    app.layout = lambda: html.Div(
        [
            fuc.FefferyCookie(
                id='current-locale',
                cookieKey=translator.cookie_name,
                value='en-us',  # 设置为英文
                expires=3600 * 24 * 365,
            ),
            fuc.FefferyReload(id='page-reload'),
            html.Div(id='page-container'),
        ],
        style={'padding': 50},
    )

    @app.callback(
        Output('page-container', 'children'),
        Input('page-container', 'id'),
    )
    def render(_):
        current_locale = request.cookies.get(translator.cookie_name)
        current_locale = current_locale or 'zh-cn'

        return fac.AntdSpace(
            [
                fac.AntdButton(
                    (
                        '切换到英语'
                        if current_locale == 'zh-cn'
                        else 'switch to japanese'
                        if current_locale == 'en-us'
                        else '中国語を切り替えます'
                    ),
                    type='primary',
                    id='switch-button',
                    clickExecuteJsString="""
window.dash_clientside.set_props(
    'current-locale',
    {
        value: '%s'
    }
)
window.dash_clientside.set_props(
    'page-reload',
    {
        reload: true
    }
)
"""
                    % (
                        'en-us'
                        if current_locale == 'zh-cn'
                        else 'jp'
                        if current_locale == 'en-us'
                        else 'zh-cn'
                    ),
                ),
                fac.AntdAlert(
                    type='info',
                    showIcon=True,
                    message=translator.t('示例警告消息'),
                    description=translator.t('示例警告描述'),
                    id='test-alert',
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#page-container')

    # 验证英文内容显示正确
    dash_duo.wait_for_text_to_equal('#switch-button', 'switch to japanese')
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-message', 'Sample message of alert'
    )
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-description', 'Sample description of alert'
    )


def test_i18n_japanese_locale(dash_duo):
    """测试日文本地化功能"""
    app = Dash(__name__, suppress_callback_exceptions=True)

    translator = Translator(translations='./tests/i18n_utils/locales.json')

    app.layout = lambda: html.Div(
        [
            fuc.FefferyCookie(
                id='current-locale',
                cookieKey=translator.cookie_name,
                value='jp',  # 设置为日文
                expires=3600 * 24 * 365,
            ),
            fuc.FefferyReload(id='page-reload'),
            html.Div(id='page-container'),
        ],
        style={'padding': 50},
    )

    @app.callback(
        Output('page-container', 'children'),
        Input('page-container', 'id'),
    )
    def render(_):
        current_locale = request.cookies.get(translator.cookie_name)
        current_locale = current_locale or 'zh-cn'

        return fac.AntdSpace(
            [
                fac.AntdButton(
                    (
                        '切换到英语'
                        if current_locale == 'zh-cn'
                        else 'switch to japanese'
                        if current_locale == 'en-us'
                        else '中国語を切り替えます'
                    ),
                    type='primary',
                    id='switch-button',
                    clickExecuteJsString="""
window.dash_clientside.set_props(
    'current-locale',
    {
        value: '%s'
    }
)
window.dash_clientside.set_props(
    'page-reload',
    {
        reload: true
    }
)
"""
                    % (
                        'en-us'
                        if current_locale == 'zh-cn'
                        else 'jp'
                        if current_locale == 'en-us'
                        else 'zh-cn'
                    ),
                ),
                fac.AntdAlert(
                    type='info',
                    showIcon=True,
                    message=translator.t('示例警告消息'),
                    description=translator.t('示例警告描述'),
                    id='test-alert',
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('#page-container')

    # 验证日文内容显示正确
    dash_duo.wait_for_text_to_equal('#switch-button', '中国語を切り替えます')
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-message', 'サンプルアラートメッセージ'
    )
    dash_duo.wait_for_text_to_equal(
        '#test-alert .ant-alert-description', 'サンプルアラート説明'
    )
