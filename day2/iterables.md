1. **filter()**: Filters elements of an iterable based on a function that returns either `True` or `False`.

    ```python
    numbers = [1, 2, 3, 4, 5]
    evens = filter(lambda x: x % 2 == 0, numbers)
    print(list(evens))  # [2, 4]
    ```

2. **reduce()**: Applies a function of two arguments cumulatively to the elements of an iterable, from left to right, to reduce the iterable to a single value. This function is found in the `functools` module.

    ```python
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)  # 120
    ```

3. **zip()**: Combines two or more iterables into tuples. The resulting iterable will have the length of the shortest input iterable.

    ```python
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    combined = zip(names, ages)
    print(list(combined))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    ```

4. **enumerate()**: Adds a counter to an iterable and returns it as an enumerate object.

    ```python
    names = ["Alice", "Bob", "Charlie"]
    enumerated_names = enumerate(names, start=1)
    print(list(enumerated_names))  # [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
    ```

5. **all()**: Returns `True` if all elements of the iterable are true (or if the iterable is empty).

    ```python
    values = [True, True, False, True]
    result = all(values)
    print(result)  # False
    ```

6. **any()**: Returns `True` if any element of the iterable is true. If the iterable is empty, it returns `False`.

    ```python
    values = [True, False, False, False]
    result = any(values)
    print(result)  # True
    ```

7. **sorted()**: Returns a new list containing all items from the original iterable in ascending order.

    ```python
    numbers = [3, 1, 4, 2]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # [1, 2, 3, 4]
    ```

These functions can be particularly powerful when combined, allowing for expressive and concise operations on data.