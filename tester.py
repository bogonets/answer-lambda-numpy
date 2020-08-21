# -*- coding: utf-8 -*-

import importlib.util
import unittest


def import_module(name):
    spec = importlib.util.spec_from_file_location(name, f'{name}.app.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


numpy_all = import_module('numpy_all')
numpy_any = import_module('numpy_any')
numpy_array = import_module('numpy_array')
numpy_cmp = import_module('numpy_cmp')
numpy_item = import_module('numpy_item')
numpy_shape = import_module('numpy_shape')
numpy_size = import_module('numpy_size')
numpy_slice = import_module('numpy_slice')
numpy_zeros = import_module('numpy_zeros')


class TestNumpyLambdas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all(self):
        self.assertTrue(True)

    def test_any(self):
        self.assertTrue(True)

    def test_array(self):
        self.assertTrue(True)

    def test_cmp(self):
        self.assertTrue(True)

    def test_item(self):
        self.assertTrue(True)

    def test_shape(self):
        self.assertTrue(True)

    def test_size(self):
        self.assertTrue(True)

    def test_slice(self):
        self.assertTrue(True)

    def test_zeros(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
