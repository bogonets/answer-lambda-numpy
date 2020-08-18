# -*- coding: utf-8 -*-

import numpy as np


DTYPE_NAME_TO_TYPE = {
    "int8": np.int8,
    "int16": np.int16,
    "int32": np.int32,
    "int64": np.int64,
    "uint8": np.uint8,
    "uint16": np.uint16,
    "uint32": np.uint32,
    "uint64": np.uint64,
    "float32": np.float32,
    "float64": np.float64,
}
DTYPE_TYPE_TO_NAME = {v: k for k, v in DTYPE_NAME_TO_TYPE.items()}
ORDER_NAMES = ['K', 'A', 'C', 'F']

elements = ()
shape = (0,)
dtype = np.int32
order = 'K'
subok = True
ndmin = 0


def on_set(key, val):
    global dtype
    if key == 'elements':
        global elements
        if dtype == np.float32 or dtype == np.float64:
            elements = list(map(lambda x: float(x), str(val).split(',')))
        else:
            elements = list(map(lambda x: int(x), str(val).split(',')))
    elif key == 'shape':
        global shape
        shape = list(map(lambda x: int(x), str(val).split(',')))
    elif key == 'dtype':
        dtype = DTYPE_NAME_TO_TYPE[val]
    elif key == 'order':
        global order
        order = val
        assert order in ORDER_NAMES
    elif key == 'subok':
        global subok
        subok = val.lower() in ['y', 'yes', 'true']
    elif key == 'ndmin':
        global ndmin
        ndmin = int(val)


def on_get(key):
    if key == 'elements':
        return ','.join(list(map(lambda x: str(x), elements)))
    elif key == 'shape':
        return ','.join(list(map(lambda x: str(x), shape)))
    elif key == 'dtype':
        return DTYPE_TYPE_TO_NAME[dtype]
    elif key == 'order':
        return order
    elif key == 'subok':
        return subok
    elif key == 'ndmin':
        return ndmin


def on_run():
    return {
        "result": np.array(elements, dtype=dtype, order=order, subok=subok, ndmin=ndmin).reshape(shape)
    }


if __name__ == '__main__':
    pass
