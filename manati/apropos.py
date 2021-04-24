

def help_tests():
    help_text = """

How to run tests
****************

   python -m unittest discover tests
    
"""

    print(help_text)


def help_install():
    help_text = """

How to install project for development
**************************************

In order to install your own project for development, install it in
development mode (a.k.a editable mode). From the project root directory,
submit:

    pip install -e .

or

    python setup.py develop
    
"""
    print(help_text)