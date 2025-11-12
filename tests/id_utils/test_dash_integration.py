from feffery_dash_utils.id_utils import (
    Auto,
    AutoUniqueIdEnum,
    AutoUniqueDictIdEnum,
    Match,
)
from dash import Dash, html, ALL, MATCH, no_update, ctx
from dash.dependencies import Input, Output, State
from feffery_antd_components import AntdButton, AntdSpace, AntdSelect



class ButtonType(AutoUniqueIdEnum):
    ADD = Auto
    DELETE = Auto
    UPDATE = Auto


class ActionButton(AutoUniqueDictIdEnum):
    BASE = {'type': 'action', 'index': Auto}
    ADD = {'type': 'action', 'index': Auto}
    DELETE = {'type': 'action', 'index': Auto}
    UPDATE = {'type': 'action', 'index': Auto}


class BaseAction(AutoUniqueDictIdEnum):
    BUTTON = {'type': 'button', 'index': Match}
    OUTPUT = {'type': 'output', 'index': Match}


class AddAction(AutoUniqueDictIdEnum):
    BUTTON = {'type': 'button', 'index': Match}
    OUTPUT = {'type': 'output', 'index': Match}


class DeleteAction(AutoUniqueDictIdEnum):
    BUTTON = {'type': 'button', 'index': Match}
    OUTPUT = {'type': 'output', 'index': Match}


class UpdateAction(AutoUniqueDictIdEnum):
    BUTTON = {'type': 'button', 'index': Match}
    OUTPUT = {'type': 'output', 'index': Match}


def test_string_id_buttons(dash_duo):
    """测试字符串ID按钮功能"""
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.Div('字符串id测试'),
            AntdSpace(
                [
                    AntdButton(
                        id=ButtonType.ADD.value, type='primary', children='新增'
                    ),
                    AntdButton(
                        id=ButtonType.DELETE.value,
                        type='default',
                        danger=True,
                        children='删除',
                    ),
                    AntdButton(
                        id=ButtonType.UPDATE.value,
                        type='default',
                        children='修改',
                    ),
                ]
            ),
            html.Div(id='output', style={'marginTop': '20px'}),
        ]
    )

    @app.callback(
        Output('output', 'children'),
        [
            Input(ButtonType.ADD.callback(), 'nClicks'),
            Input(ButtonType.DELETE.callback(), 'nClicks'),
            Input(ButtonType.UPDATE.callback(), 'nClicks'),
        ],
        prevent_initial_call=True,
    )
    def update_output(add_clicks, delete_clicks, update_clicks):
        return (
            f'新增按钮点击次数: {add_clicks or 0}, '
            f'删除按钮点击次数: {delete_clicks or 0}, '
            f'修改按钮点击次数: {update_clicks or 0}'
        )

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('div')

    # 测试新增按钮点击
    add_button = dash_duo.find_element(f'#{ButtonType.ADD.value}')
    add_button.click()

    # 验证输出更新
    dash_duo.wait_for_text_to_equal(
        '#output',
        '新增按钮点击次数: 1, 删除按钮点击次数: 0, 修改按钮点击次数: 0',
    )

    # 测试删除按钮点击
    delete_button = dash_duo.find_element(f'#{ButtonType.DELETE.value}')
    delete_button.click()

    # 验证输出更新
    dash_duo.wait_for_text_to_equal(
        '#output',
        '新增按钮点击次数: 1, 删除按钮点击次数: 1, 修改按钮点击次数: 0',
    )

    # 测试修改按钮点击
    update_button = dash_duo.find_element(f'#{ButtonType.UPDATE.value}')
    update_button.click()

    # 验证输出更新
    dash_duo.wait_for_text_to_equal(
        '#output',
        '新增按钮点击次数: 1, 删除按钮点击次数: 1, 修改按钮点击次数: 1',
    )

    # 验证没有浏览器错误
    assert dash_duo.get_logs() == [], '浏览器控制台应该没有错误'


def test_dict_id_all_buttons(dash_duo):
    """测试字典ID ALL按钮功能"""
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.Div('字典id-ALL测试'),
            AntdSpace(
                [
                    AntdButton(
                        id=ActionButton.ADD.value,
                        type='primary',
                        children='新增',
                    ),
                    AntdButton(
                        id=ActionButton.DELETE.value,
                        type='default',
                        danger=True,
                        children='删除',
                    ),
                    AntdButton(
                        id=ActionButton.UPDATE.value,
                        type='default',
                        children='修改',
                    ),
                ]
            ),
            html.Div(id='all-output', style={'marginTop': '20px'}),
        ]
    )

    @app.callback(
        Output('all-output', 'children'),
        Input(ActionButton.BASE.callback(index=ALL), 'nClicks'),
        prevent_initial_call=True,
    )
    def update_all_output(n_clicks):
        triggered_id = ctx.triggered_id
        return f'当前点击按钮{triggered_id}, 新增/删除/修改点击次数: {n_clicks}'

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('div')

    # 测试新增按钮点击
    add_button = dash_duo.find_element('[id*="ActionButton-ADD"]')
    add_button.click()

    # 验证输出更新
    dash_duo.wait_for_contains_text(
        '#all-output',
        f'当前点击按钮{dict(sorted(ActionButton.ADD.value.items(), key=lambda x: x[0]))}, 新增/删除/修改点击次数: [1, None, None]',
    )

    # 验证没有浏览器错误
    assert dash_duo.get_logs() == [], '浏览器控制台应该没有错误'


def test_dict_id_match_buttons(dash_duo):
    """测试字典ID MATCH按钮功能"""
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.Div('字典id-MATCH测试'),
            AntdSelect(
                id='select',
                options=['新增', '删除', '修改'],
                placeholder='请选择操作',
                style={'width': '200px'},
            ),
            html.Div(id='select-output', style={'marginTop': '20px'}),
        ]
    )

    @app.callback(
        Output('select-output', 'children'),
        Input('select', 'value'),
        prevent_initial_call=True,
    )
    def update_select_output(selected_value):
        if selected_value == '新增':
            return html.Div(
                [
                    AntdButton(
                        id=AddAction.BUTTON.value,
                        type='primary',
                        children='新增',
                    ),
                    html.Div(
                        id=AddAction.OUTPUT.value,
                        style={'marginTop': '20px'},
                    ),
                ]
            )
        elif selected_value == '删除':
            return html.Div(
                [
                    AntdButton(
                        id=DeleteAction.BUTTON.value,
                        type='default',
                        danger=True,
                        children='删除',
                    ),
                    html.Div(
                        id=DeleteAction.OUTPUT.value,
                        style={'marginTop': '20px'},
                    ),
                ]
            )
        elif selected_value == '修改':
            return html.Div(
                [
                    AntdButton(
                        id=UpdateAction.BUTTON.value,
                        type='default',
                        children='修改',
                    ),
                    html.Div(
                        id=UpdateAction.OUTPUT.value,
                        style={'marginTop': '20px'},
                    ),
                ]
            )
        return no_update

    @app.callback(
        Output(BaseAction.OUTPUT.callback(index=MATCH), 'children'),
        Input(BaseAction.BUTTON.callback(index=MATCH), 'nClicks'),
        State(BaseAction.BUTTON.callback(index=MATCH), 'id'),
        prevent_initial_call=True,
    )
    def match_update_output(n_clicks, id):
        return f'{id}按钮点击次数: {n_clicks}'

    # 启动服务器
    dash_duo.start_server(app)

    # 等待应用加载完成
    dash_duo.wait_for_element('div')

    # 点击选择框
    select = dash_duo.find_element('#select')
    select.click()

    # 点击新增选项
    add_option = dash_duo.find_element(
        'div.ant-select-item-option[title="新增"]'
    )
    add_option.click()

    # 等待新增按钮出现
    dash_duo.wait_for_element('button[id*="AddAction-BUTTON"]')

    # 点击新增按钮
    add_button = dash_duo.find_element('button[id*="AddAction-BUTTON"]')
    add_button.click()

    # 验证输出更新
    dash_duo.wait_for_element('div[id*="AddAction-BUTTON"]')
    dash_duo.wait_for_text_to_equal('div[id*="AddAction-BUTTON"]', f'{AddAction.BUTTON.value}按钮点击次数: 1')

    # 验证没有浏览器错误
    assert dash_duo.get_logs() == [], '浏览器控制台应该没有错误'
