import math

import numpy as np
from d2l import torch as d2l


def f(x):
    return math.pow(x, 3.0) - math.pow(x, -1.0)


x = np.arange(-1, 2, 0.01)
d2l.plot(x, [f(x), 4 * x - 4], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
d2l.plt.show()
