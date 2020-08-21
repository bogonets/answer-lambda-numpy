# -*- coding: utf-8 -*-

import numpy as np


def on_run(array: np.ndarray, index: np.ndarray):
    return {'result': array.item(index.tolist())}
