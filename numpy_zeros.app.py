# -*- coding: utf-8 -*-
# @see <https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html>

import numpy as np

DTYPE_INT8_NAME = "int8"
DTYPE_INT16_NAME = "int16"
DTYPE_INT32_NAME = "int32"
DTYPE_INT64_NAME = "int64"
DTYPE_UINT8_NAME = "uint8"
DTYPE_UINT16_NAME = "uint16"
DTYPE_UINT32_NAME = "uint32"
DTYPE_UINT64_NAME = "uint64"
DTYPE_FLOAT32_NAME = "float32"
DTYPE_FLOAT64_NAME = "float64"
DTYPE_NAME_TO_TYPE = {
    DTYPE_INT8_NAME: np.int8,
    DTYPE_INT16_NAME: np.int16,
    DTYPE_INT32_NAME: np.int32,
    DTYPE_INT64_NAME: np.int64,
    DTYPE_UINT8_NAME: np.uint8,
    DTYPE_UINT16_NAME: np.uint16,
    DTYPE_UINT32_NAME: np.uint32,
    DTYPE_UINT64_NAME: np.uint64,
    DTYPE_FLOAT32_NAME: np.float32,
    DTYPE_FLOAT64_NAME: np.float64,
}
DTYPE_TYPE_TO_NAME = {v: k for k, v in DTYPE_NAME_TO_TYPE.items()}

shape = (0,)
dtype = np.int32


def on_set(key, val):
    if key == 'shape':
        global shape
        shape = list(map(lambda x: int(x), str(val).split(',')))
    elif key == 'dtype':
        global dtype
        dtype = DTYPE_NAME_TO_TYPE[val]


def on_get(key):
    if key == 'shape':
        return ','.join(list(map(lambda x: str(x), shape)))
    elif key == 'dtype':
        return DTYPE_TYPE_TO_NAME[dtype]


def on_create():
    return True


def on_init():
    return True


def on_valid():
    return True


def on_run():
    return {
        "result": np.zeros(shape, dtype)
    }


def on_destroy():
    return True


if __name__ == '__main__':
    pass
