Certainly! Let's delve deeper into the topics for Day 3.

### Day 3: Advanced Topics

#### 1. **Object-Oriented Programming (OOP)**:

**Class & Objects**:
Python is an object-oriented language. A class creates a new type where objects are instances of the class. 

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} barks!"

# Usage:
dog1 = Dog("Buddy")
print(dog1.bark())  # Output: Buddy barks!
```

**Inheritance**:
Inheritance allows us to define a class that inherits all the methods and properties from another class.

```python
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name

    def bark(self):
        return f"{self.name} barks!"

dog1 = Dog("Buddy", "Canine")
print(dog1.species)  # Output: Canine
```

**Encapsulation**:
It prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single `_` or double `__`.

```python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def set_max_price(self, price):
        self.__maxprice = price

c = Computer()
c.sell()  # Output: Selling Price: 900
```

**Polymorphism**:
It allows us to define methods in the child class with the same name as defined in their parent class.

```python
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

bird = Bird()
sparrow = Sparrow()
bird.flight()  # Output: Most of the birds can fly but some cannot.
sparrow.flight()  # Output: Sparrows can fly.
```

#### 2. **File Handling**:
Python allows you to read and write files with the `open()` function. Remember to close the file with the `close()` function after usage.

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Working with JSON**:
The `json` module allows you to convert Python objects into JSON strings and vice versa.

```python
import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
print(json_string)  # Output: '{"name": "John", "age": 30}'
```

#### 3. **Error and Exception Handling**:
Use `try...except` blocks to catch exceptions.

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Raising Exceptions**:
Use the `raise` keyword to trigger an exception.

```python
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
```

#### 4. **Comprehensions**:
List comprehensions provide a concise way to create lists.

```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 5. **Generators**:
Generators are iterators but can only be iterated over once. They yield values using the `yield` keyword.

```python
def gen_func():
    for i in range(3):
        yield i

gen = gen_func()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
```

#### 6. **Decorators**:
Decorators provide a way to modify functions using another function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
