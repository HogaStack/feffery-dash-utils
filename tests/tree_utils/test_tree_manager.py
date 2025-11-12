from feffery_dash_utils.tree_utils import TreeManager


class TestTreeManager:
    """树形数据管理器测试类"""

    def setup_method(self):
        """测试前准备示例树形数据"""
        self.demo_tree = [
            {
                'title': '节点1',
                'key': '节点1',
                'children': [
                    {
                        'title': '节点1-1',
                        'key': '节点1-1',
                        'children': [
                            {
                                'title': '节点1-1-1',
                                'key': '节点1-1-1',
                            },
                            {
                                'title': '节点1-1-2',
                                'key': '节点1-1-2',
                            },
                        ],
                    }
                ],
            },
            {
                'title': '节点2',
                'key': '节点2',
                'children': [{'title': '节点2-1', 'key': '节点2-1'}],
            },
        ]

    def test_update_tree_node(self):
        """测试节点更新功能"""
        result = TreeManager.update_tree_node(
            self.demo_tree,
            '节点1-1',
            {'title': '节点1-1', 'key': '节点1-1'},
        )
        # 验证节点标题是否正确更新
        updated_node = TreeManager.get_node(result, '节点1-1')
        assert updated_node is not None
        assert isinstance(updated_node, dict)
        assert updated_node['title'] == '节点1-1'

    def test_update_tree_node_overlay(self):
        """测试节点增量更新功能"""
        result = TreeManager.update_tree_node(
            self.demo_tree,
            '节点1-1',
            {'title': '节点1-1new'},
            'overlay',
        )
        # 验证节点标题是否正确更新
        updated_node = TreeManager.get_node(result, '节点1-1')
        assert updated_node is not None
        assert isinstance(updated_node, dict)
        assert updated_node['title'] == '节点1-1new'

    def test_add_node_before(self):
        """测试节点前置新增功能"""
        result = TreeManager.add_node_before(
            self.demo_tree,
            '节点1-1',
            {'title': '节点1-0', 'key': '节点1-0'},
        )
        # 验证新节点是否正确添加
        new_node = TreeManager.get_node(result, '节点1-0')
        assert new_node is not None
        assert isinstance(new_node, dict)
        assert new_node['title'] == '节点1-0'

    def test_add_node_after(self):
        """测试节点后置新增功能"""
        result = TreeManager.add_node_after(
            self.demo_tree,
            '节点1-1',
            {'title': '节点1-2', 'key': '节点1-2'},
        )
        # 验证新节点是否正确添加
        new_node = TreeManager.get_node(result, '节点1-2')
        assert new_node is not None
        assert isinstance(new_node, dict)
        assert new_node['title'] == '节点1-2'

    def test_delete_node(self):
        """测试节点删除功能"""
        result = TreeManager.delete_node(self.demo_tree, '节点2')
        # 验证节点是否被删除
        deleted_node = TreeManager.get_node(result, '节点2')
        assert deleted_node is None

    def test_get_node(self):
        """测试节点查询功能"""
        node = TreeManager.get_node(self.demo_tree, '节点1-1')
        # 验证节点是否正确查询
        assert node is not None
        assert isinstance(node, dict)
        assert node['key'] == '节点1-1'

    def test_get_node_not_found(self):
        """测试不存在节点查询功能"""
        node = TreeManager.get_node(self.demo_tree, '节点1-666')
        # 验证不存在的节点返回None
        assert node is None

    def test_update_tree_node_with_children(self):
        """测试节点查询+节点增量更新功能"""
        # 先获取原始节点的子节点
        original_node = TreeManager.get_node(self.demo_tree, '节点1-1')
        assert original_node is not None
        assert isinstance(original_node, dict)
        original_children = original_node['children']

        result = TreeManager.update_tree_node(
            self.demo_tree,
            '节点1-1',
            {
                'children': [
                    *original_children,
                    {
                        'title': '节点1-1-3',
                        'key': '节点1-1-3',
                    },
                ]
            },
            'overlay',
        )
        # 验证子节点是否正确添加
        updated_node = TreeManager.get_node(result, '节点1-1')
        assert updated_node is not None
        assert isinstance(updated_node, dict)
        assert len(updated_node['children']) == 3

    def test_delete_node_keep_empty_children(self):
        """测试删除后空列表children处理功能"""
        # keep_empty_children_node=True (默认)
        result1 = TreeManager.delete_node(self.demo_tree, '节点2-1')
        parent_node = TreeManager.get_node(result1, '节点2')
        assert parent_node is not None
        assert isinstance(parent_node, dict)
        assert 'children' in parent_node
        assert len(parent_node['children']) == 0

        # keep_empty_children_node=False
        # 当删除节点后父节点的children列表为空时，父节点也会被删除
        result2 = TreeManager.delete_node(
            self.demo_tree, '节点2-1', keep_empty_children_node=False
        )
        parent_node = TreeManager.get_node(result2, '节点2')
        # 在这种情况下，父节点应该被删除
        assert parent_node is None
