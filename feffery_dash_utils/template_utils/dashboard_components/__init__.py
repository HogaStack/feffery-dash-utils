import feffery_antd_components as fac
from dash import html
from dash.development.base_component import Component
from feffery_dash_utils.style_utils import style
from typing import List, Sequence, Union


__all__ = ['welcome_card', 'blank_card', 'simple_chart_card', 'index_card']

_Component = Union[Component, str, int, float, None]


def welcome_card(
    title: Union[_Component, Sequence[_Component]] = None,
    description: Union[_Component, Sequence[_Component]] = None,
    avatar: _Component = None,
    extra: _Component = None,
    root_id: Union[str, dict, None] = None,
    rootStyle: Union[dict, None] = None,
    rootClassName: Union[str, None] = None,
    titleStyle: Union[dict, None] = None,
    titleClassName: Union[str, None] = None,
    descriptionStyle: Union[dict, None] = None,
    descriptionClassName: Union[str, None] = None,
) -> Component:
    """欢迎卡片

    Args:
        title (Union[_Component, Sequence[_Component]], optional): 标题元素. Defaults to None.
        description (Union[_Component, Sequence[_Component]], optional): 标题下方辅助描述元素. Defaults to None.
        avatar (_Component, optional): 头像元素. Defaults to None.
        extra (_Component, optional): 额外元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        titleStyle (dict, optional): 标题样式. Defaults to None.
        titleClassName (str, optional): 标题类名. Defaults to None.
        descriptionStyle (dict, optional): 描述样式. Defaults to None.
        descriptionClassName (str, optional): 描述类名. Defaults to None.

    Returns:
        Component: 构造完成的欢迎卡片
    """

    return html.Div(
        fac.AntdFlex(
            [
                fac.AntdSpace(
                    [
                        avatar,
                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    title,
                                    strong=True,
                                    className=titleClassName,
                                    style={
                                        **dict(fontSize=20),
                                        **(titleStyle or {}),
                                    },
                                ),
                                fac.AntdText(
                                    description,
                                    type='secondary',
                                    className=descriptionClassName,
                                    style=descriptionStyle,
                                ),
                            ],
                            size='small',
                            direction='vertical',
                        ),
                    ],
                    size=18,
                ),
                extra,
            ],
            justify='space-between',
            align='center',
        ),
        className=rootClassName,
        style={
            **dict(
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        id=root_id,
    )


def blank_card(
    children: Union[_Component, Sequence[_Component]] = None,
    root_id: Union[str, dict, None] = None,
    rootStyle: Union[dict, None] = None,
    rootClassName: Union[str, None] = None,
    backgroundImage: Union[str, None] = None,
) -> Component:
    """空白卡片

    Args:
        children (Union[_Component, Sequence[_Component]], optional): 子元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        backgroundImage (str, optional): 背景图url. Defaults to None.

    Returns:
        Component: 构造完成的卡片
    """

    return html.Div(
        children,
        className=rootClassName,
        style={
            **dict(
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
            **(
                style(
                    backgroundImage=f'url({backgroundImage})',
                    backgroundSize='cover',
                    backgroundPosition='center',
                )
                if backgroundImage
                else {}
            ),
        },
        id=root_id,
    )


def simple_chart_card(
    title: Union[_Component, Sequence[_Component]] = None,
    description: Union[_Component, Sequence[_Component]] = None,
    chart: Union[_Component, Sequence[_Component]] = None,
    extra: _Component = None,
    height: Union[int, float, str] = 300,
    root_id: Union[str, dict, None] = None,
    rootStyle: Union[dict, None] = None,
    rootClassName: Union[str, None] = None,
    titleStyle: Union[dict, None] = None,
    titleClassName: Union[str, None] = None,
    descriptionStyle: Union[dict, None] = None,
    descriptionClassName: Union[str, None] = None,
) -> Component:
    """简单图表卡片

    Args:
        title (Union[_Component, Sequence[_Component]], optional): 标题元素. Defaults to None.
        description (Union[_Component, Sequence[_Component]], optional): 标题右侧辅助描述元素. Defaults to None.
        chart (Union[_Component, Sequence[_Component]], optional): 图表元素. Defaults to None.
        extra (_Component, optional): 额外元素. Defaults to None.
        height (Union[int, float, str], optional): 卡片高度. Defaults to 300.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        titleStyle (dict, optional): 标题样式. Defaults to None.
        titleClassName (str, optional): 标题类名. Defaults to None.
        descriptionStyle (dict, optional): 描述样式. Defaults to None.
        descriptionClassName (str, optional): 描述类名. Defaults to None.

    Returns:
        Component: 构造完成的简单图表卡片
    """

    return html.Div(
        fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdText(
                                    title,
                                    strong=True,
                                    className=titleClassName,
                                    style={
                                        **dict(
                                            fontSize=20,
                                        ),
                                        **(titleStyle or {}),
                                    },
                                ),
                                (
                                    fac.AntdText(
                                        description,
                                        type='secondary',
                                        className=descriptionClassName,
                                        style=descriptionStyle,
                                    )
                                    if description
                                    else None
                                ),
                            ],
                            size=4,
                            align='baseline',
                        ),
                        extra,
                    ],
                    justify='space-between',
                ),
                fac.AntdDivider(
                    lineColor='#f0f0f0',
                    style=style(marginTop=12, marginBottom=12),
                ),
                html.Div(chart, style=style(height='100%', minHeight=0)),
            ],
            vertical=True,
            gap=0,
            style=style(width='100%', height='100%'),
        ),
        className=rootClassName,
        style={
            **dict(
                height=height,
                padding=20,
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        id=root_id,
    )


def index_card(
    index_name: _Component = None,
    index_description: Union[_Component, Sequence[_Component]] = None,
    index_value: Union[_Component, Sequence[_Component]] = None,
    extra_content: Union[_Component, Sequence[_Component]] = None,
    footer_content: Union[_Component, Sequence[_Component]] = None,
    root_id: Union[str, dict, None] = None,
    rootStyle: Union[dict, None] = None,
    rootClassName: Union[str, None] = None,
    indexNameStyle: Union[dict, None] = None,
    indexNameClassName: Union[str, None] = None,
    extraContentStyle: Union[dict, None] = None,
    extraContentClassName: Union[str, None] = None,
    footerContentStyle: Union[dict, None] = None,
    footerContentClassName: Union[str, None] = None,
) -> Component:
    """指标卡片

    Args:
        index_name (_Component, optional): 指标名称. Defaults to None.
        index_description (Union[_Component, Sequence[_Component]], optional): 指标描述内容. Defaults to None.
        index_value (Union[_Component, Sequence[_Component]], optional): 指标值元素. Defaults to None.
        extra_content (Union[_Component, Sequence[_Component]], optional): 额外元素. Defaults to None.
        footer_content (Union[_Component, Sequence[_Component]], optional): 底部元素. Defaults to None.
        root_id (Union[str, dict], optional): 根元素id. Defaults to None.
        rootStyle (dict, optional): 根元素样式. Defaults to None.
        rootClassName (str, optional): 根元素类名. Defaults to None.
        indexNameStyle (dict, optional): 指标名称样式. Defaults to None.
        indexNameClassName (str, optional): 指标名称类名. Defaults to None.
        extraContentStyle (dict, optional): 额外元素样式. Defaults to None.
        extraContentClassName (str, optional): 额外元素类名. Defaults to None.
        footerContentStyle (dict, optional): 底部元素样式. Defaults to None.
        footerContentClassName (str, optional): 底部元素类名. Defaults to None.

    Returns:
        Component: 构造完成的指标卡片
    """

    content: List[_Component] = [
        fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        index_name,
                        (
                            fac.AntdTooltip(
                                fac.AntdIcon(
                                    icon='antd-info-circle',
                                ),
                                title=index_description,
                            )
                            if index_description
                            else None
                        ),
                    ],
                    justify='space-between',
                    className=indexNameClassName,
                    style={
                        **dict(color='rgba(0, 0, 0, 0.65)', fontSize=16),
                        **(indexNameStyle or {}),
                    },
                ),
                fac.AntdText(index_value, style=style(fontSize=28)),
            ],
            vertical=True,
            justify='space-between',
            style=style(height=64, overflowY='hidden'),
        )
    ]
    if extra_content is not None:
        content.append(
            html.Div(
                html.Div(extra_content, style=style(height='100%')),
                className=extraContentClassName,
                style={
                    **dict(
                        height=56,
                        marginBottom=12,
                        overflowX='hidden',
                        overflowY='hidden',
                    ),
                    **(extraContentStyle or {}),
                },
            )
        )
    if footer_content is not None:
        content.extend(
            [
                fac.AntdDivider(style=style(marginTop=0, marginBottom=0)),
                html.Div(
                    footer_content,
                    className=footerContentClassName,
                    style={
                        **dict(
                            height=22,
                            paddingTop=9,
                            overflowY='hidden',
                        ),
                        **(footerContentStyle or {}),
                    },
                ),
            ]
        )
    return html.Div(
        fac.AntdSpace(
            content,
            size=0,
            direction='vertical',
            style=style(width='100%'),
        ),
        className=rootClassName,
        style={
            **dict(
                padding='20px 20px 8px',
                background='#fff',
                borderRadius=8,
                boxSizing='border-box',
                boxShadow='0 1px 2px 0 rgba(0, 0, 0, 0.03),0 1px 6px -1px rgba(0, 0, 0, 0.02),0 2px 4px 0 rgba(0, 0, 0, 0.02)',
            ),
            **(rootStyle or {}),
        },
        id=root_id,
    )
