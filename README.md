# my-calculator

A simple Python calculator that supports basic arithmetic operations.

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another  
- **Multiplication**: Multiply two numbers together

## Usage

```python
from calculator import add, subtract, multiply

# Addition
result = add(10, 5)  # Returns 15

# Subtraction  
result = subtract(10, 5)  # Returns 5

# Multiplication
result = multiply(10, 5)  # Returns 50
```

## Running the Examples

Run the main script to see the calculator in action:

```bash
python main.py
```

## Testing

Run the unit tests to verify functionality:

```bash
python test_calculator.py
```

## Functions

### add(x, y)
Calculates the sum of two numbers.

**Parameters:**
- `x` (int, float): First number
- `y` (int, float): Second number

**Returns:**
- The sum of x and y

### subtract(x, y)  
Calculates the difference between two numbers.

**Parameters:**
- `x` (int, float): First number
- `y` (int, float): Second number

**Returns:**
- The difference of x and y (x - y)

### multiply(x, y)
Calculates the product of two numbers.

**Parameters:**
- `x` (int, float): First number
- `y` (int, float): Second number

**Returns:**
- The product of x and y

All functions include input validation and will raise a `ValueError` if non-numeric inputs are provided.