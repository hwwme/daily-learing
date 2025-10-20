class Calculator:
    """一个简单的计算器类，支持加减乘除运算。"""

    def __init__(self):
        # 可以用来存储状态，比如历史记录、是否启用科学模式等
        self._history = []  # 私有属性：记录运算历史

    def add(self, a, b):
        """加法"""
        return a+b

    def subtract(self, a, b):
        """减法"""
        return a-b

    def multiply(self, a, b):
        """乘法"""
        return a*b

    def divide(self, a, b):
        """除法（含除零检查）"""
        if b ==0:
            raise ValueError("除数不能为0")
        return a/b

    def get_history(self):
        """获取运算历史"""
        return self._history.copy()
    
    def add_to_history(self, operation, a, b, result):
        """将运算记录添加到历史记录中"""
        self._history.append({
            "operation": operation,
            "operands": (a, b),
            "result": result
        })
    
    def clean_history(self):
        """清空运算历史"""
        self._history.clear()
