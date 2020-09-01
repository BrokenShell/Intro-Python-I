import sys
import os

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html


# Print out the command line arguments in sys.argv, one per line:
for itm in sys.argv:
    print(itm)

# Print out the OS platform you're using:
print(sys.platform)

# Print out the version of Python you're using:
print(sys.version)

# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.getlogin())
