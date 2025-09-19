'''
Step 1: Create a Package
A package in Python is simply a directory that contains a special file __init__.py and one or more modules (Python files).
'''
#1. Create a directory (folder) named mypackage. Inside this folder, create the following files:

    '''mypackage/
    __init__.py
    module1.py
    module2.py'''

#2. Add content to these files:

__init__.py
# This file can be left empty, or you can add initialization code if needed

module1.py
def greet():
    print("Hello from module1!")


module2.py
def farewell():
    print("Goodbye from module2!")

'''
Step 2: Access the Package
Now, create a Python script that imports and uses the package.
'''

main.py (this file should be outside the mypackage directory)
# Importing the package
from mypackage import module1, module2

# Accessing functions from the modules
module1.greet()       # This will print: Hello from module1!
module2.farewell()    # This will print: Goodbye from module2!


'''
Directory Structure:
    project/
    main.py
    mypackage/
        __init__.py
        module1.py
        module2.py
'''