# coding=utf-8
import pytest

import server.FileService as fs


class Test_change_dir:

    def test_incorrect_type1(self):
        """Передать None в качестве значения

        Ожидаемый результат: возбуждение исключения TypeError
        """
        with pytest.raises(TypeError):
            fs.create_dir(None)

    def test_incorrect_type2(self):
        """Передать значение типа int

        Ожидаемый результат: возбуждение исключения TypeError
        """
        with pytest.raises(TypeError):
            fs.create_dir(12345)

    def test_dot_dir(self):
        """Передать . в качестве значения,

        Ожидаемый результат: успешная отработка
        """
        fs.create_dir('.')

    def test_incorrect_value2(self, function_fix2):
        """Передать .. в качестве значения

        Ожидаемый результат: успешная отработка
        """
        fs.create_dir('..')

    def test_incorrect_value3(self):
        """Передать ../something в качестве значения

        Ожидаемый результат: успешная отработка и создание директории something
        """
        fs.create_dir('../something')


    @pytest.mark.skip(reason="no way of currently testing this")
    def test_skip_sun(self):
        """Test skip fun"""
        assert False

