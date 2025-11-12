# 我的计算器

中文 | [English](README.md)

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](test_calculator.py)

一个简单优雅的 Python 计算器库，提供基本的算术运算功能。

## 项目概述

本项目是一个用 Python 编写的轻量级计算器模块，展示了清晰的代码实践和适当的测试方法。它提供基本的数学运算，具有输入验证和清晰的错误处理机制。

### 功能特性

- **加法运算**：计算两个数字的和
- **减法运算**：计算两个数字的差
- **输入验证**：确保输入为有效的数字（整数或浮点数）
- **错误处理**：对无效输入抛出清晰的异常
- **完善测试**：包含全面的单元测试

## 安装说明

### 前置要求

- Python 3.6 或更高版本
- pip（Python 包管理器）

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/nekoaru/my-calculator.git
cd my-calculator
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 作为模块使用

您可以在 Python 代码中导入并使用计算器函数：

```python
from calculator import add, subtract

# 加法
result = add(10, 5)
print(result)  # 输出：15

# 减法
result = subtract(10, 5)
print(result)  # 输出：5
```

### 运行演示程序

执行主脚本查看计算器的实际运行效果：

```bash
python main.py
```

### 运行测试

运行单元测试：

```bash
python -m pytest test_calculator.py
```

或使用 unittest：

```bash
python test_calculator.py
```

## 项目结构

```
my-calculator/
├── calculator.py      # 主计算器模块，包含算术函数
├── main.py           # 演示脚本，展示计算器使用方法
├── test_calculator.py # 计算器函数的单元测试
├── requirements.txt  # 项目依赖
└── README.md        # 项目文档
```

## API 参考

### `add(x, y)`

计算两个数字的和。

**参数：**
- `x` (int/float)：第一个数字
- `y` (int/float)：第二个数字

**返回值：**
- (int/float)：x 和 y 的和

**异常：**
- `ValueError`：如果任一输入不是数字

**示例：**
```python
result = add(5, 3)  # 返回 8
```

### `subtract(x, y)`

计算两个数字的差。

**参数：**
- `x` (int/float)：第一个数字（被减数）
- `y` (int/float)：第二个数字（减数）

**返回值：**
- (int/float)：差值 (x - y)

**异常：**
- `ValueError`：如果任一输入不是数字

**示例：**
```python
result = subtract(10, 3)  # 返回 7
```

## 贡献指南

欢迎贡献！以下是您可以参与贡献的方式：

1. **报告 Bug**：创建 issue 描述 bug 以及如何重现
2. **建议功能**：创建 issue 描述您希望看到的功能
3. **提交 Pull Request**：Fork 仓库，进行更改，然后提交 PR

### 开发指南

- 编写清晰的、有注释的代码
- 为新功能添加单元测试
- 提交前确保所有测试通过
- 遵循 Python PEP 8 代码风格指南

## 许可证

本项目是开源的，采用 MIT 许可证。

## 联系方式

如有问题或建议，请在 GitHub 上创建 issue。

---

用 ❤️ 制作，来自 My Calculator 团队
