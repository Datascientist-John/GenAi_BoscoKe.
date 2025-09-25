# This script imports and uses a function from a Jac file.

# Import the Jac Lang module, which is necessary to run Jac code within Python.
import jaclang

# Import the 'lovejac' function from the 'first.jac' file.
# The 'first' here refers to the name of the file without the '.jac' extension.
from first import lovejac

# Call the 'lovejac' function and print its return value alongside a string.
print(f"Python is awesome. But, {lovejac()}")