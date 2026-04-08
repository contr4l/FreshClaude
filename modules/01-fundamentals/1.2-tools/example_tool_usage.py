"""
工具使用示例
演示 Claude Code 工具的基本用法
"""

def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数 - 由 Edit 工具添加"""
    return a * b

if __name__ == "__main__":
    print(greet("World"))
    print(add(1, 2))
