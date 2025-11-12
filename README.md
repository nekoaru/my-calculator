# My Calculator

[中文](README_CN.md) | English

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](test_calculator.py)

A simple and elegant Python calculator library that provides basic arithmetic operations.

## Overview

This project is a lightweight calculator module written in Python that demonstrates clean code practices and proper testing. It provides basic mathematical operations with input validation and clear error handling.

### Features

- **Addition**: Calculate the sum of two numbers
- **Subtraction**: Calculate the difference between two numbers
- **Input Validation**: Ensures inputs are valid numbers (int or float)
- **Error Handling**: Raises clear exceptions for invalid inputs
- **Well-Tested**: Includes comprehensive unit tests

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nekoaru/my-calculator.git
cd my-calculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### As a Module

You can import and use the calculator functions in your Python code:

```python
from calculator import add, subtract

# Addition
result = add(10, 5)
print(result)  # Output: 15

# Subtraction
result = subtract(10, 5)
print(result)  # Output: 5
```

### Running the Demo

Execute the main script to see the calculator in action:

```bash
python main.py
```

### Running Tests

To run the unit tests:

```bash
python -m pytest test_calculator.py
```

Or using unittest:

```bash
python test_calculator.py
```

## Project Structure

```
my-calculator/
├── calculator.py      # Main calculator module with arithmetic functions
├── main.py           # Demo script showing calculator usage
├── test_calculator.py # Unit tests for calculator functions
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation
```

## API Reference

### `add(x, y)`

Calculates the sum of two numbers.

**Parameters:**
- `x` (int/float): First number
- `y` (int/float): Second number

**Returns:**
- (int/float): Sum of x and y

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = add(5, 3)  # Returns 8
```

### `subtract(x, y)`

Calculates the difference between two numbers.

**Parameters:**
- `x` (int/float): First number (minuend)
- `y` (int/float): Second number (subtrahend)

**Returns:**
- (int/float): Difference (x - y)

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = subtract(10, 3)  # Returns 7
```

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **Suggest Features**: Open an issue describing the feature you'd like to see
3. **Submit Pull Requests**: Fork the repository, make your changes, and submit a PR

### Development Guidelines

- Write clear, commented code
- Add unit tests for new features
- Ensure all tests pass before submitting
- Follow Python PEP 8 style guidelines

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please open an issue on GitHub.

---

Made with ❤️ by the My Calculator Team