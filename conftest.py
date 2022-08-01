import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if not language:
        raise pytest.UsageError("--language can not be empty!")
    return request.config.getoption("--language")