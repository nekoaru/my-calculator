# My Calculator

[简体中文](README_CN.md) | English

[![Python application](https://github.com/nekoaru/my-calculator/workflows/Python%20application/badge.svg)](https://github.com/nekoaru/my-calculator/actions)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A simple yet powerful Python calculator that performs basic arithmetic operations. This project demonstrates clean code practices, proper testing, and continuous integration.

## Overview

My Calculator is a lightweight Python library that provides basic arithmetic operations including addition and subtraction. It features input validation, error handling, and comprehensive unit tests.

## Features

- ✨ **Basic Arithmetic Operations**: Addition and subtraction functions
- 🔒 **Input Validation**: Type checking for numeric inputs
- 🧪 **Well-Tested**: Comprehensive unit tests using Python's unittest framework
- 🚀 **CI/CD Ready**: Automated testing with GitHub Actions
- 📝 **Clean Code**: Well-documented and easy to understand
- 🐍 **Python 3**: Compatible with Python 3.x

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

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

### Basic Usage

You can use the calculator functions in your Python code:

```python
from calculator import add, subtract

# Addition
result = add(10, 5)
# Output: The sum of 10 and 5 is 15
# Returns: 15

# Subtraction
result = subtract(10, 5)
# Output: The difference between 10 and 5 is 5
# Returns: 5
```

### Running the Demo

Run the included demo script:

```bash
python main.py
```

This will demonstrate the calculator's functionality with sample calculations.

### API Reference

#### `add(x, y)`

Calculates the sum of two numbers.

**Parameters:**
- `x` (int or float): The first number
- `y` (int or float): The second number

**Returns:**
- (int or float): The sum of x and y

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = add(10, 5)  # Returns 15
```

#### `subtract(x, y)`

Calculates the difference between two numbers.

**Parameters:**
- `x` (int or float): The first number
- `y` (int or float): The second number

**Returns:**
- (int or float): The difference (x - y)

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = subtract(10, 5)  # Returns 5
```

## Testing

The project includes comprehensive unit tests to ensure code quality and reliability.

### Run Tests

Execute all tests using unittest:

```bash
python -m unittest discover
```

Or run specific test files:

```bash
python test_calculator.py
```

### Test Coverage

The test suite covers:
- ✅ Addition operations
- ✅ Subtraction operations
- ✅ Input validation
- ✅ Error handling

## Project Structure

```
my-calculator/
├── calculator.py       # Core calculator functions
├── main.py            # Demo script
├── test_calculator.py # Unit tests
├── requirements.txt   # Project dependencies
├── README.md          # English documentation
├── README_CN.md       # Chinese documentation
└── .github/
    └── workflows/
        └── python-app.yml  # CI/CD configuration
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and ensure tests pass:
   ```bash
   python -m unittest discover
   ```
4. **Commit your changes**:
   ```bash
   git commit -m "Add: brief description of your changes"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

### Guidelines

- Write clear, concise commit messages
- Add tests for new functionality
- Ensure all tests pass before submitting
- Follow existing code style and conventions
- Update documentation as needed

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/nekoaru/my-calculator.git
cd my-calculator

# Install development dependencies
pip install -r requirements.txt

# Run tests to verify setup
python -m unittest discover
```

## CI/CD

This project uses GitHub Actions for continuous integration. On every push and pull request:

- Dependencies are installed
- Unit tests are executed
- The main application is run to verify functionality

View the workflow configuration in [`.github/workflows/python-app.yml`](.github/workflows/python-app.yml).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created and maintained by [nekoaru](https://github.com/nekoaru).

## Acknowledgments

- Built with Python 3
- Tested with unittest framework
- CI/CD powered by GitHub Actions

---

⭐ If you find this project helpful, please consider giving it a star!