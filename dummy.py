#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a dummy Python script.

It can be used as a placeholder or a starting point for a new project.
"""

# Import statements (optional, commented out for now)
# import os
# import sys

# Global variables (if any)
DUMMY_CONSTANT = "Hello, Dummy!"

def example_function(name):
    """
    An example function that greets the provided name.
    """
    greeting = f"{DUMMY_CONSTANT} This is a function call for {name}."
    print(greeting)
    return greeting

def another_simple_function():
    """
    Another simple function.
    """
    # A simple calculation
    a = 5
    b = 10
    result = a + b
    print(f"The result of {a} + {b} is {result}")
    return result

# Main execution block
if __name__ == "__main__":
    print("Dummy script started.")

    # Call the example function
    example_function("User")

    # Call another simple function
    another_simple_function()

    print("Dummy script finished.")

# End of the dummy Python script