### 1. Modules:

A module is simply a Python file that contains functions, classes, or variables. Others can then import and use the functionality defined in the module.

**Steps to create a module:**
1. Create a new Python file, e.g., `mymodule.py`.
2. Define functions, classes, or variables in this file.
   
   ```python
   # mymodule.py
   def my_function():
       return "Hello from my module!"
   ```
3. Save the file.

You can now use this module in another Python script:

```python
import mymodule

print(mymodule.my_function())  # Outputs: Hello from my module!
```

### 2. Packages:

A package is a way of organizing related modules into a single directory hierarchy. The primary purpose of Python packages is to organize and provide a unique namespace for collections of modules.

**Steps to create a package:**
1. Create a new directory for your package, e.g., `mypackage`.
2. Inside this directory, create a special file named `__init__.py`. This file can be empty, but it must exist for Python to recognize the directory as a package. It can also contain initialization code for your package.
3. Add modules to this directory. For instance, you could add `mymodule.py` from the previous example.

Your directory structure should look like:

```
mypackage/
│
├── __init__.py
└── mymodule.py
```

You can now use the module from the package in another Python script:

```python
from mypackage import mymodule

print(mymodule.my_function())  # Outputs: Hello from my module!
```

### Sub-packages:

Packages can also contain sub-packages. To create a sub-package:

1. Create a new directory inside your main package directory, e.g., `sub_package`.
2. Add an `__init__.py` file to this directory.
3. Add modules to this directory as needed.

The directory structure would then be:

```
mypackage/
│
├── __init__.py
├── mymodule.py
│
└── sub_package/
    ├── __init__.py
    └── another_module.py
```

To use the module from the sub-package:

```python
from mypackage.sub_package import another_module

# Use functions/classes from another_module
```

By organizing modules into packages and sub-packages, you can develop scalable and well-organized Python projects.