# Any pytest file should start with -> test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in one method only
# Method name should have sense
# -k stands for method names execution, - s logs  in output, -v stands for more info metadata
#  you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup adn tear down methods for test cases- conftest file to generalize fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():  # function
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_addition():
    assert 1 + 1 == 2


def test_subtraction():
    assert 3 - 2 == 1


def test_multiplication():
    assert 2 * 3 == 6


def test_division():
    assert 6 / 3 == 2


def test_string_length():
    string = "pytest"
    assert len(string) == 6


def test_string_concatenation():
    str1 = "Hello"
    str2 = " "
    str3 = "Pytest"
    result = str1 + str2 + str3
    assert result == "Hello Pytest"
