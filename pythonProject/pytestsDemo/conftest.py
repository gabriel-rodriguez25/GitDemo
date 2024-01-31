import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield # Everything after yield is going to be executed at the end(e.g.: close a browser)
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Gabriel","Rodriguez","rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome","Gabriel","Rodriguez"),("Firefox","Rodriguez"),"Edge"])
def crossBrowser(request):
    return request.param
