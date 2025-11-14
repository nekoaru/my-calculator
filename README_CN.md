# My Calculator（我的计算器）

简体中文 | [English](README.md)

[![Python application](https://github.com/nekoaru/my-calculator/workflows/Python%20application/badge.svg)](https://github.com/nekoaru/my-calculator/actions)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个简单但功能强大的 Python 计算器，可执行基本的算术运算。该项目展示了干净的代码实践、适当的测试和持续集成。

## 概述

My Calculator 是一个轻量级的 Python 库，提供包括加法和减法在内的基本算术运算。它具有输入验证、错误处理和全面的单元测试功能。

## 特性

- ✨ **基本算术运算**：加法和减法功能
- 🔒 **输入验证**：对数字输入进行类型检查
- 🧪 **经过充分测试**：使用 Python 的 unittest 框架进行全面单元测试
- 🚀 **支持 CI/CD**：通过 GitHub Actions 自动化测试
- 📝 **代码整洁**：文档完善且易于理解
- 🐍 **Python 3**：兼容 Python 3.x

## 安装

### 前置要求

- Python 3.x
- pip（Python 包管理器）

### 设置

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

### 基本用法

您可以在 Python 代码中使用计算器函数：

```python
from calculator import add, subtract

# 加法
result = add(10, 5)
# 输出：The sum of 10 and 5 is 15
# 返回值：15

# 减法
result = subtract(10, 5)
# 输出：The difference between 10 and 5 is 5
# 返回值：5
```

### 运行演示

运行包含的演示脚本：

```bash
python main.py
```

这将通过示例计算演示计算器的功能。

### API 参考

#### `add(x, y)`

计算两个数字的和。

**参数：**
- `x` (int 或 float)：第一个数字
- `y` (int 或 float)：第二个数字

**返回值：**
- (int 或 float)：x 和 y 的和

**异常：**
- `ValueError`：如果任一输入不是数字

**示例：**
```python
result = add(10, 5)  # 返回 15
```

#### `subtract(x, y)`

计算两个数字的差。

**参数：**
- `x` (int 或 float)：第一个数字
- `y` (int 或 float)：第二个数字

**返回值：**
- (int 或 float)：差值 (x - y)

**异常：**
- `ValueError`：如果任一输入不是数字

**示例：**
```python
result = subtract(10, 5)  # 返回 5
```

## 测试

该项目包含全面的单元测试以确保代码质量和可靠性。

### 运行测试

使用 unittest 执行所有测试：

```bash
python -m unittest discover
```

或运行特定的测试文件：

```bash
python test_calculator.py
```

### 测试覆盖范围

测试套件涵盖：
- ✅ 加法运算
- ✅ 减法运算
- ✅ 输入验证
- ✅ 错误处理

## 项目结构

```
my-calculator/
├── calculator.py       # 核心计算器函数
├── main.py            # 演示脚本
├── test_calculator.py # 单元测试
├── requirements.txt   # 项目依赖
├── README.md          # 英文文档
├── README_CN.md       # 中文文档
└── .github/
    └── workflows/
        └── python-app.yml  # CI/CD 配置
```

## 贡献

欢迎贡献！以下是您可以提供帮助的方式：

1. **Fork 仓库**
2. **创建特性分支**：
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **进行更改**并确保测试通过：
   ```bash
   python -m unittest discover
   ```
4. **提交更改**：
   ```bash
   git commit -m "Add: 简要描述您的更改"
   ```
5. **推送到您的 fork**：
   ```bash
   git push origin feature/your-feature-name
   ```
6. **创建 Pull Request**

### 指南

- 编写清晰简洁的提交消息
- 为新功能添加测试
- 提交前确保所有测试通过
- 遵循现有的代码风格和约定
- 根据需要更新文档

## 开发

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/nekoaru/my-calculator.git
cd my-calculator

# 安装开发依赖
pip install -r requirements.txt

# 运行测试以验证设置
python -m unittest discover
```

## CI/CD

该项目使用 GitHub Actions 进行持续集成。在每次推送和 Pull Request 时：

- 安装依赖项
- 执行单元测试
- 运行主应用程序以验证功能

在 [`.github/workflows/python-app.yml`](.github/workflows/python-app.yml) 中查看工作流配置。

## 许可证

该项目根据 MIT 许可证授权 - 有关详细信息，请参阅 LICENSE 文件。

## 作者

由 [nekoaru](https://github.com/nekoaru) 创建和维护。

## 致谢

- 使用 Python 3 构建
- 使用 unittest 框架测试
- CI/CD 由 GitHub Actions 提供支持

---

⭐ 如果您觉得这个项目有帮助，请考虑给它一个 star！
