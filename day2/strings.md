1. **capitalize()**: Capitalizes the first character of the string.
    ```python
    print("hello".capitalize())  # Hello
    ```

2. **upper()**: Converts all characters in the string to uppercase.
    ```python
    print("hello".upper())  # HELLO
    ```

3. **lower()**: Converts all characters in the string to lowercase.
    ```python
    print("HELLO".lower())  # hello
    ```

4. **title()**: Converts the first character of each word to uppercase.
    ```python
    print("hello world".title())  # Hello World
    ```

5. **startswith(substring)**: Returns `True` if the string starts with the specified substring.
    ```python
    print("hello".startswith("he"))  # True
    ```

6. **endswith(substring)**: Returns `True` if the string ends with the specified substring.
    ```python
    print("hello".endswith("lo"))  # True
    ```

7. **find(substring)**: Returns the position of the first occurrence of the substring. If not found, returns `-1`.
    ```python
    print("hello".find("l"))  # 2
    ```

8. **replace(old, new)**: Replaces all occurrences of `old` with `new`.
    ```python
    print("hello world".replace("world", "Python"))  # hello Python
    ```

9. **split(delimiter)**: Splits the string into a list using the specified delimiter.
    ```python
    print("hello,world".split(","))  # ['hello', 'world']
    ```

10. **join(iterable)**: Joins an iterable using the string as a delimiter.
    ```python
    delimiter = "-"
    my_list = ["hello", "world"]
    print(delimiter.join(my_list))  # hello-world
    ```

11. **strip()**: Removes whitespace from the beginning and end of the string.
    ```python
    print("  hello  ".strip())  # hello
    ```

12. **lstrip()**: Removes whitespace from the beginning of the string.
    ```python
    print("  hello  ".lstrip())  # "hello  "
    ```

13. **rstrip()**: Removes whitespace from the end of the string.
    ```python
    print("  hello  ".rstrip())  # "  hello"
    ```

14. **isalpha()**: Returns `True` if all characters in the string are alphabetic.
    ```python
    print("hello".isalpha())  # True
    ```

15. **isdigit()**: Returns `True` if all characters in the string are digits.
    ```python
    print("1234".isdigit())  # True
    ```

16. **isspace()**: Returns `True` if all characters in the string are whitespace characters.
    ```python
    print("    ".isspace())  # True
    ```

17. **len(string)**: Although not a string method per se, the built-in `len()` function returns the length of the string.
    ```python
    print(len("hello"))  # 5
    ```

These are just a subset of the methods available for strings in Python. You can always use the `dir()` function on a string to get a list of all the associated methods:

```python
print(dir(str))
```

To learn more about any specific method, use the `help()` function:

```python
help(str.upper)
```

This will provide a detailed description of the method, its parameters, and its return value.