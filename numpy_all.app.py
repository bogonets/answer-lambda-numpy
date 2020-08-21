# -*- coding: utf-8 -*-
# https://numpy.org/doc/stable/reference/generated/numpy.all.html

import numpy as np


class ConditionIsFalse(Exception):
    pass


def on_run(condition, data):
    if np.all(condition):
        return {'result': data}
    else:
        raise ConditionIsFalse


if __name__ == '__main__':
    pass
