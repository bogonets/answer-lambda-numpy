# -*- coding: utf-8 -*-

import importlib.util
import unittest
import numpy as np


def import_module(name):
    spec = importlib.util.spec_from_file_location(name, f'{name}.app.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# noinspection PyCallingNonCallable
class BaseLambdaTestCase:

    def __init__(self, module_name):
        self.lib = import_module(module_name)

    def set(self, key, val):
        if hasattr(self.lib, 'on_set'):
            self.lib.on_set(key, val)

    def set_dict(self, **kwargs):
        for key, val in kwargs.items():
            self.set(key, val)

    def get(self, key):
        if hasattr(self.lib, 'on_get'):
            return self.lib.on_get(key)
        else:
            return None

    def init(self):
        if hasattr(self.lib, 'on_init'):
            return self.lib.on_init()
        else:
            return True

    def valid(self):
        if hasattr(self.lib, 'on_valid'):
            return self.lib.on_valid()
        else:
            return True

    def run(self, *args, **kwargs):
        assert hasattr(self.lib, 'on_run')
        return self.lib.on_run(*args, **kwargs)

    def destroy(self):
        if hasattr(self.lib, 'on_destroy'):
            self.lib.on_destroy()


class TestNumpyAll(unittest.TestCase):

    def __init__(self, test_method_name='runTest'):
        super().__init__(test_method_name)
        self.module = BaseLambdaTestCase('numpy_array')

    def setUp(self):
        self.module.set_dict(elements='0,1,2,3,4,5', shape='2,3')
        self.assertTrue(self.module.init())
        self.assertTrue(self.module.valid())

    def tearDown(self):
        self.module.destroy()

    def test_default(self):
        result = self.module.run()
        self.assertIsInstance(result['result'], np.ndarray)
        self.assertEqual((2, 3,), result['result'].shape)
        self.assertEqual(6, result['result'].size)
        self.assertEqual(0, result['result'][0, 0])
        self.assertEqual(1, result['result'][0, 1])
        self.assertEqual(2, result['result'][0, 2])
        self.assertEqual(3, result['result'][1, 0])
        self.assertEqual(4, result['result'][1, 1])
        self.assertEqual(5, result['result'][1, 2])


if __name__ == '__main__':
    unittest.main()
