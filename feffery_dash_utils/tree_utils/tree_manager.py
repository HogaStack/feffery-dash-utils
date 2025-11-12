from copy import deepcopy
from typing import Union, Literal


class TreeManager:
    """
    针对`AntdTree`组件对应的树形数据结构进行快捷管理\n
    Manage the tree data structure of `AntdTree` easily.
    """

    @classmethod
    def update_tree_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        mode: Literal['replace', 'overlay'] = 'replace',
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        对key值等于node_key的节点进行整体替换或增量更新

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 更新目标节点key值
            new_node (dict): 更新目标节点新数据字典
            mode (Literal['replace', 'overlay'], default 'replace'): 更新模式，'replace'表示整体替换，'overlay'表示增量更新
            data_type (Literal['tree', 'menu'], default 'tree'): 数据类型，'tree'表示树形数据，'menu'表示菜单数据

        Returns:
            list: 完成更新后的treeData
        """

        return cls.__update_tree_node(
            deepcopy(input_object), node_key, new_node, mode, data_type
        )

    @classmethod
    def __update_tree_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        mode: Literal['replace', 'overlay'] = 'replace',
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        对应update_tree_node()的私有方法
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(input_object, (list, dict)), (
            'input_object类型需为列表或字典\nthe type of input_object must be list or dict'
        )

        if isinstance(input_object, list):
            return [
                cls.__update_tree_node(
                    node, node_key, new_node, mode, data_type
                )
                for node in input_object
            ]

        elif isinstance(input_object, dict):
            if data_type == 'menu':
                if input_object.get('props', {}).get('key') == node_key:
                    if mode == 'replace':
                        return new_node
                    else:
                        return {**input_object, **new_node}
                else:
                    if input_object.get('children'):
                        input_object['children'] = [
                            cls.__update_tree_node(
                                child, node_key, new_node, mode, data_type
                            )
                            for child in input_object['children']
                        ]
                    return input_object

            else:
                if input_object.get('key') == node_key:
                    if mode == 'replace':
                        return new_node
                    else:
                        return {**input_object, **new_node}
                else:
                    if input_object.get('children'):
                        input_object['children'] = [
                            cls.__update_tree_node(
                                child, node_key, new_node, mode, data_type
                            )
                            for child in input_object['children']
                        ]
                    return input_object

    @classmethod
    def add_node_before(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        在key值等于node_key的节点之前插入平级新节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 插入目标节点key值
            new_node (dict): 要插入的新节点数据字典
            data_type (Literal['tree', 'menu'], default 'tree'): 数据类型，'tree'表示树形数据，'menu'表示菜单数据

        Returns:
            dict: 完成插入后的treeData
        """

        return cls.__add_node_before(
            deepcopy(input_object), node_key, new_node, data_type
        )

    @classmethod
    def __add_node_before(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        对应add_node_before()的私有方法
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(input_object, (list, dict)), (
            'input_object类型需为列表或字典\nthe type of input_object must be list or dict'
        )

        if isinstance(input_object, list):
            if data_type == 'menu':
                current_layer_keys = [
                    node.get('props', {}).get('key') for node in input_object
                ]
            else:
                current_layer_keys = [node.get('key') for node in input_object]
            if node_key in current_layer_keys:
                return [
                    *input_object[: current_layer_keys.index(node_key)],
                    new_node,
                    *input_object[current_layer_keys.index(node_key) :],
                ]
            else:
                return [
                    cls.__add_node_before(node, node_key, new_node, data_type)
                    for node in input_object
                ]

        elif isinstance(input_object, dict):
            if input_object.get('children'):
                input_object['children'] = cls.__add_node_before(
                    input_object['children'], node_key, new_node, data_type
                )

        return input_object

    @classmethod
    def add_node_after(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        在key值等于node_key的节点之后插入平级新节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 插入目标节点key值
            new_node (dict): 要插入的新节点数据字典
            data_type (Literal['tree', 'menu'], default 'tree'): 数据类型，'tree'表示树形数据，'menu'表示菜单数据

        Returns:
            dict: 完成插入后的treeData
        """

        return cls.__add_node_after(
            deepcopy(input_object), node_key, new_node, data_type
        )

    @classmethod
    def __add_node_after(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict]:
        """
        对应add_node_after()的私有方法
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(input_object, (list, dict)), (
            'input_object类型需为列表或字典\nthe type of input_object must be list or dict'
        )

        if isinstance(input_object, list):
            if data_type == 'menu':
                current_layer_keys = [
                    node.get('props', {}).get('key') for node in input_object
                ]
            else:
                current_layer_keys = [node.get('key') for node in input_object]
            if node_key in current_layer_keys:
                return [
                    *input_object[: current_layer_keys.index(node_key) + 1],
                    new_node,
                    *input_object[current_layer_keys.index(node_key) + 1 :],
                ]
            else:
                return [
                    cls.__add_node_after(node, node_key, new_node, data_type)
                    for node in input_object
                ]

        elif isinstance(input_object, dict):
            if input_object.get('children'):
                input_object['children'] = cls.__add_node_after(
                    input_object['children'], node_key, new_node, data_type
                )

        return input_object

    @classmethod
    def delete_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        data_type: Literal['tree', 'menu'] = 'tree',
        keep_empty_children_node: bool = True,
    ) -> Union[list, dict]:
        """
        删除key值等于node_key的节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 删除目标节点key值
            data_type (Literal['tree', 'menu'], default 'tree'): 数据类型，'tree'表示树形数据，'menu'表示菜单数据
            keep_empty_children_node (bool, default True): 是否保留children字段为空列表的节点

        Returns:
            dict: 完成删除后的treeData
        """

        return cls.__delete_node(
            deepcopy(input_object),
            node_key,
            data_type,
            keep_empty_children_node,
        )

    @classmethod
    def __delete_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        data_type: Literal['tree', 'menu'] = 'tree',
        keep_empty_children_node: bool = True,
    ) -> Union[list, dict]:
        """
        对应delete_node()的私有方法
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(input_object, (list, dict)), (
            'input_object类型需为列表或字典\nthe type of input_object must be list or dict'
        )

        if isinstance(input_object, list):
            delete_result = []
            for node in input_object:
                if (
                    node.get('props', {}).get('key') != node_key
                    if data_type == 'menu'
                    else node.get('key') != node_key
                ):
                    if node.get('children'):
                        # 节点有children时，判断删除后是否为空，为空则不添加进结果
                        tmp_children = cls.__delete_node(
                            node['children'],
                            node_key,
                            data_type,
                            keep_empty_children_node,
                        )
                        # 选择性添加
                        if keep_empty_children_node or tmp_children:
                            delete_result.append(
                                {**node, 'children': tmp_children}
                            )
                    else:
                        delete_result.append(node)
            return delete_result
        return input_object

    @classmethod
    def get_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        data_type: Literal['tree', 'menu'] = 'tree',
    ) -> Union[list, dict, None]:
        """
        查询key值等于node_key的节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 查询目标节点key值
            data_type (Literal['tree', 'menu'], default 'tree'): 数据类型，'tree'表示树形数据，'menu'表示菜单数据

        Returns:
            dict: 目标节点数据字典
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(input_object, (list, dict)), (
            'input_object类型需为列表或字典\nthe type of input_object must be list or dict'
        )

        # 若当前节点为列表
        if isinstance(input_object, list):
            # 依次检查子节点
            for node in input_object:
                if (
                    node.get('props', {}).get('key') == node_key
                    if data_type == 'menu'
                    else node.get('key') == node_key
                ):
                    return node
                # 否则递归检查子节点的children
                if 'children' in node:
                    found_node = cls.get_node(
                        node['children'], node_key, data_type
                    )
                    if found_node:
                        return found_node

        # 若当前节点为字典
        elif isinstance(input_object, dict):
            if (
                input_object.get('props', {}).get('key') == node_key
                if data_type == 'menu'
                else input_object.get('key') == node_key
            ):
                return input_object
            # 否则递归检查子节点的children
            if 'children' in input_object:
                return cls.get_node(
                    input_object['children'], node_key, data_type
                )
        # 若未找到则返回None
        return None
