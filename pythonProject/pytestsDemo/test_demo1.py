# Any pytest file should start with -> test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in one method only
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):  #function
    print("Hello")


@pytest.mark.xfail
def test_secondProgram():
    print("Good morning!")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
