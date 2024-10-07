import pytest

from testing_pythonrepos_3 import *

def test_status_code():
    """Check that status code is 200"""
    assert r.status_code == 200