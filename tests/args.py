# coding=utf-8
import sys

import main
import pytest


class Test_Parser:
    def test_error(self):
        """Test error args"""
        with pytest.raises(SystemExit) as e:
            sys.argv = ['main.py', '-12412412']
            main.main()
        print(type(e.value.code))
        assert e.value.code == 2

    def test_version(self):
        """Test version args"""

        with pytest.raises(SystemExit) as e:
            sys.argv = ['main.py', '-v']
            main.main()
        print(type(e.value.code))
        assert e.value.code == 0
