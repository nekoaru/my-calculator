# My Calculator

![Python application](https://github.com/nekoaru/my-calculator/workflows/Python%20application/badge.svg)

A simple Python calculator library that provides basic arithmetic operations. This project demonstrates clean code practices, unit testing, and continuous integration with GitHub Actions.

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- Input validation to ensure only numbers are processed
- Comprehensive unit tests
- Continuous Integration with GitHub Actions

## Installation

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

### Using the Calculator Module

You can import and use the calculator functions in your Python code:

```python
from calculator import add, subtract

# Addition
result = add(10, 5)  # Returns 15

# Subtraction
result = subtract(10, 5)  # Returns 5
```

### Running the Demo

Run the included demonstration script:

```bash
python main.py
```

This will display example calculations using the calculator functions.

## Running Tests

Execute the unit tests to verify functionality:

```bash
python -m unittest discover
```

Or run the test file directly:

```bash
python test_calculator.py
```

## Project Structure

```
my-calculator/
├── calculator.py         # Core calculator functions
├── main.py              # Demo script showing usage examples
├── test_calculator.py   # Unit tests for calculator functions
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## API Reference

### `add(x, y)`

Adds two numbers together.

**Parameters:**
- `x` (int or float): The first number
- `y` (int or float): The second number

**Returns:**
- (int or float): The sum of x and y

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = add(5, 3)  # Returns 8
```

### `subtract(x, y)`

Subtracts the second number from the first.

**Parameters:**
- `x` (int or float): The number to subtract from
- `y` (int or float): The number to subtract

**Returns:**
- (int or float): The difference between x and y

**Raises:**
- `ValueError`: If either input is not a number

**Example:**
```python
result = subtract(10, 3)  # Returns 7
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.