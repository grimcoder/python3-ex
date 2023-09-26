## Day 2: Intermediate Python

### 1. **Lists, Tuples, and Dictionaries**

#### Lists:
- **Definition**: Ordered, mutable sequences of elements.
- **Creation**: `my_list = [1, 2, 3]`
- **Indexing**: Access elements with `my_list[0]` (gets the first element).
- **Methods**: `.append()`, `.remove()`, `.pop()`, `.sort()`, etc.

#### Tuples:
- **Definition**: Ordered, immutable sequences.
- **Creation**: `my_tuple = (1, 2, 3)`
- **Usage**: Often for data that shouldn't be changed, like coordinates or RGB colors.

#### Dictionaries:
- **Definition**: Unordered collections of key-value pairs.
- **Creation**: `my_dict = {'key1': 'value1', 'key2': 'value2'}`
- **Access**: `my_dict['key1']` will return `'value1'`.
- **Methods**: `.keys()`, `.values()`, `.items()`, `.get()`, etc.

### 2. **Functions**
- **Definition**: Reusable blocks of code.
- **Syntax**:
    ```python
    def function_name(parameters):
        # code here
        return result
    ```

- **Example**:
    ```python
    def add(a, b):
        return a + b
    ```

### 3. **Modules and Packages**
- **Modules**: A module is a file containing Python code. For example, `math` is a module with mathematical functions and constants.
    ```python
    import math
    math.sqrt(16)  # returns 4.0
    ```

- **Packages**: A package is a way of organizing related modules into a single directory hierarchy. For example, the `os` and `sys` modules are part of the standard library.

### 4. **File I/O**
- **Reading**:
    ```python
    with open('file.txt', 'r') as file:
        content = file.read()
    ```

- **Writing**:
    ```python
    with open('file.txt', 'w') as file:
        file.write("Hello, World!")
    ```

### 5. **Basic Exception Handling**
- **Try/Except**:
    ```python

    try:
    # some potentially problematic code
        x = 1 / 0
    except Exception as e:
        print(f"An error occurred: {e}")


    try:
        # code that might raise an exception
        x = 1 / 0
    except ZeroDivisionError:
        print("Can't divide by zero!")
    ```

### 6. **Intro to Libraries**:
- Explore standard libraries like `datetime`, `os`, and `sys`.
- Introduction to installing third-party libraries using `pip`.

---

### **Exercises for Day 2**:

1. **Data Structures**: Given a list of numbers, write a function that returns a list containing only the even numbers.
2. **Functions**: Write a function that takes two strings and returns the concatenated result.
3. **Modules**: Use the `math` module to compute the factorial of a number.
4. **File I/O**: Write a program that reads a file, modifies its content (e.g., converting all text to uppercase), and writes the modified content back to the file.
5. **Exception Handling**: Write a function that takes two numbers as strings, converts them to integers, divides them, and returns the result. Handle any exceptions that may arise.
6. **Libraries**: Use the `datetime` library to determine how many days have passed since the start of the year.

This concludes Day 2. After completing the exercises, you'll be well-versed with intermediate Python concepts!