import pytest
import os
from feffery_dash_utils.version_utils import (
    check_python_version,
    check_dependencies_version,
    PythonVersionError,
    DependencyNotFoundError,
)


class TestVersionUtils:
    """版本工具测试类"""

    def test_check_python_version_valid(self):
        """测试有效的Python版本检查"""
        # 这应该不会抛出异常
        check_python_version(min_version='3.8', max_version='3.13')

    def test_check_python_version_invalid_min(self):
        """测试无效的Python最小版本检查"""
        # 这应该抛出PythonVersionError异常
        with pytest.raises(PythonVersionError):
            # 使用一个远高于当前版本的最小版本要求
            check_python_version(min_version='99.99')

    def test_check_python_version_invalid_max(self):
        """测试无效的Python最大版本检查"""
        # 这应该抛出PythonVersionError异常
        with pytest.raises(PythonVersionError):
            # 使用一个远低于当前版本的最大版本要求
            check_python_version(max_version='2.0')

    def test_check_dependencies_version_with_rules(self):
        """测试使用规则检查依赖版本"""
        # 这应该不会抛出异常（假设dash已安装）
        check_dependencies_version(
            rules=[{'name': 'dash', 'specifier': '>=2.18.2'}]
        )

    def test_check_dependencies_version_with_invalid_dependency(self):
        """测试检查不存在的依赖"""
        # 这应该抛出DependencyNotFoundError异常
        with pytest.raises(DependencyNotFoundError):
            check_dependencies_version(
                rules=[{'name': 'non-existent-package', 'specifier': '>=1.0.0'}]
            )

    def test_check_dependencies_version_with_requirements_file(self):
        """测试使用requirements文件检查依赖版本"""
        # 获取requirements.txt文件的正确路径
        requirements_path = os.path.join(
            os.path.dirname(__file__), 'requirements.txt'
        )
        # 这应该不会抛出异常
        check_dependencies_version(requirements_file=requirements_path)
