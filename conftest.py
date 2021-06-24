# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fix():
    """Test fixture session"""
    fixture_s_test = "fixture_session"
    print(fixture_s_test)
    return fixture_s_test


@pytest.fixture(scope='function', autouse=True)
def function_fix1():
    """Test fixture function"""
    fixture_f_test = "fixture_function"
    print(fixture_f_test)
    return fixture_f_test


@pytest.fixture(scope='function', autouse=False)
def function_fix2():
    """Test fixture function 2"""
    fixture_f_test2 = "fixture_function2"
    print(fixture_f_test2)
    return fixture_f_test2
