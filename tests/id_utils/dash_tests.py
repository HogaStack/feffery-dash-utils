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


app = Dash(__name__)

app.layout = [
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
                id=ButtonType.UPDATE.value, type='default', children='修改'
            ),
        ]
    ),
    html.Div(id='output', style={'marginTop': '20px'}),
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
    html.Div('字典id-MATCH测试'),
    AntdSelect(
        id='select',
        options=[
            {'label': '新增', 'value': AddAction.BUTTON.index},
            {'label': '删除', 'value': DeleteAction.BUTTON.index},
            {'label': '修改', 'value': UpdateAction.BUTTON.index},
        ],
        placeholder='请选择操作',
        style={'width': '200px'},
    ),
    html.Div(id='select-output', style={'marginTop': '20px'}),
]


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
        f'新增按钮点击次数: {add_clicks}, '
        f'删除按钮点击次数: {delete_clicks}, '
        f'修改按钮点击次数: {update_clicks}'
    )


@app.callback(
    Output('all-output', 'children'),
    Input(ActionButton.BASE.callback(index=ALL), 'nClicks'),
    prevent_initial_call=True,
)
def update_all_output(n_clicks):
    triggered_id = ctx.triggered_id
    return f'当前点击按钮{triggered_id}, 新增/删除/修改点击次数: {n_clicks}'


@app.callback(
    Output('select-output', 'children'),
    Input('select', 'value'),
    prevent_initial_call=True,
)
def update_select_output(selected_value):
    if selected_value == AddAction.BUTTON.index:
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
    elif selected_value == DeleteAction.BUTTON.index:
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
    elif selected_value == UpdateAction.BUTTON.index:
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


if __name__ == '__main__':
    app.run(debug=True)
