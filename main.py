from calculator import add, subtract, divide

def main():
    # 测试加法
    result_add = add(10, 5)
    print(f"10 + 5 = {result_add}")

    # 测试减法
    result_subtract = subtract(10, 5)
    print(f"10 - 5 = {result_subtract}")

    # 测试除法
    result_divide = divide(10, 5)
    print(f"10 / 5 = {result_divide}")

if __name__ == "__main__":
    main()