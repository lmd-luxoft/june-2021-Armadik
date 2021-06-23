# coding=utf-8
import os
import shutil

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

        Ожидаемый результат: текущая папка не должна измениться
        """
        fs.create_dir('.')

    def test_incorrect_value2(self):
        """Передать .. в качестве значения

        Ожидаемый результат: возбуждение исключения ValueError
        """
        fs.create_dir('..')

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_incorrect_value3(self):
        """Передать ../something в качестве значения

        Ожидаемый результат: возбуждение исключения ValueError
        """
        assert False

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_existing_dir_no_create(self):
        """Перейти в каталог, который уже существует и autocreate=False

        Ожидаемый результат: текущая папка имеет имя ExistingDirectory
        """
        assert False

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_existing_dir_create(self):
        """Перейти в каталог, который уже существует и autocreate=True

        Ожидаемый результат: текущая папка имеет имя ExistingDirectory
        """
        assert False

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_non_existing_dir_no_create(self):
        """Перейти в каталог, который не существует и autocreate=False

        Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
        """
        assert False

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_non_existing_dir_create(self):
        """Перейти в каталог, который не существует и autocreate=True

        Ожидаемый результат: текущая папка имеет имя отличное от NotExistingDirectory
        """
        assert False
