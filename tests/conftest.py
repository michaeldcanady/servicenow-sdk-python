
def pytest_addoption(parser):
    parser.addoption("--username", action="store", default="username")
    parser.addoption("--password", action="store", default="password")
