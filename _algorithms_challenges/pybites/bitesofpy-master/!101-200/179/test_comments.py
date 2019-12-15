import pytest

from comments import strip_comments

# comment code snippets from:
# https://realpython.com/documenting-python-code/

single_comment = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
'''
single_comment_after_strip = '''
def hello_world():
    print("Hello World")
'''

single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''
single_docstring_after_strip = '''
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")
'''

class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''
class_with_method_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')
'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''
multiline_docstring_after_strip = '''
def __init__(self, name, sound, num_legs):
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''
code_bite_description_after_strip = '''
import re

def hello(name):
    return f'hello {name}'
'''

class_three_indents = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''
class_three_indents_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')

        def func_in_method(self):
            pass
'''

false_positive = '''
def foo():
    # this is a comment
    print('this is not a #comment')
'''
false_positive_after_strip = '''
def foo():
    print('this is not a #comment')
'''


@pytest.mark.parametrize('arg, expected', [
    (single_comment, single_comment_after_strip),
    (single_docstring, single_docstring_after_strip),
    (class_with_method, class_with_method_after_strip),
    (multiline_docstring, multiline_docstring_after_strip),
    (code_bite_description, code_bite_description_after_strip),
    (class_three_indents, class_three_indents_after_strip),
    (false_positive, false_positive_after_strip),
])
def test_strip_comments(arg, expected):
    assert strip_comments(arg).strip() == expected.strip()