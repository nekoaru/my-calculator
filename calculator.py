# 计算2个数字的和的函数
def add(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    result = x + y
    print(f"The sum of {x} and {y} is {result}")
    return result

# 计算2个数字的差的函数
def subtract(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be numbers")
    result = x - y
    print(f"The difference between {x} and {y} is {result}")
    return result