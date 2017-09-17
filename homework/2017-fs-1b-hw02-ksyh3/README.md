# Gug-inator

This project contains a Python program designed to help Norm care for his pet.
Documentation for its behavior can be found publicly here: http://cpl.mwisely.xyz
To verify that the code works properly, you must complete any partial test functions that are given.

**Note: Follow the module documentation *exactly*!**
Failure to do so will break our existing, complete test suite.

## Regarding Tests

A couple of simple tests have been implemented.
Use them as reference for the tests you write.

`pytest.raises()` is very handy for asserting that your code raises an exception as expected.

## Running Your Tests

Tests for this program have been written using [pytest](http://pytest.org).
In order to run these tests, you must have access to a pytest executable.
To make install simpler, a script has been included to install (if necessary) and run pytest automatically.
This script creates a [virtual environment][1] within the project so that no system files are affected.

To run the tests, use the script as shown below:

~~~shell
# Assuming that you are at the top directory of your project
./py.test
~~~

**Note: this will work on campus machines. If you use your own machine, you are on your own.**

## Checking Your Style

Dr. Doofenshmirtz loves PEP 0008.

Again, we realize that not everyone has access to a PEP 0008 checker.
Thus, a script has been included to install (if necessary) and run flake8 automatically.
flake8 is a PEP 0008 checker and Python linter.

To check your style with flake8, do the following:

~~~shell
# Assuming that you are at the top directory of your project
./flake8 *.py
~~~~

## Running the Program

To run the guginator, simply do the following:

~~~shell
# Assuming that you are at the top directory of your project
python3.4 guginator.py
~~~

Refer to the [usage documentation](http://cpl.mwisely.xyz/hw/2/docs/) to figure out how all of its subcommands should work.

[1]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
