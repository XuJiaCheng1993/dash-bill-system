# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdResult(Component):
    """An AntdResult component.
结果组件AntdResult

Keyword arguments:

- id (string; optional):
    组件唯一id.

- aria-* (string; optional):
    `aria-*`格式属性通配.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- data-* (string; optional):
    `data-*`格式属性通配.

- extra (a list of or a singular dash component, string or number; optional):
    组件型，操作区域.

- icon (a list of or a singular dash component, string or number; optional):
    组件型，图标内容.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- status (a value equal to: 'success', 'error', 'info', 'warning', '404', '403', '500', 'loading'; default 'info'):
    状态，可选项有`'success'`、`'error'`、`'info'`、`'warning'`、`'404'`、`'403'`、`'500'`
    默认值：`'info'`.

- style (dict; optional):
    当前组件css样式.

- subTitle (a list of or a singular dash component, string or number; optional):
    组件型，副标题内容.

- title (a list of or a singular dash component, string or number; optional):
    组件型，标题内容."""
    _children_props = ['extra', 'title', 'subTitle', 'icon']
    _base_nodes = ['extra', 'title', 'subTitle', 'icon', 'children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdResult'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, extra=Component.UNDEFINED, status=Component.UNDEFINED, title=Component.UNDEFINED, subTitle=Component.UNDEFINED, icon=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aria-*', 'className', 'data-*', 'extra', 'icon', 'key', 'loading_state', 'status', 'style', 'subTitle', 'title']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'className', 'data-*', 'extra', 'icon', 'key', 'loading_state', 'status', 'style', 'subTitle', 'title']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdResult, self).__init__(**args)
