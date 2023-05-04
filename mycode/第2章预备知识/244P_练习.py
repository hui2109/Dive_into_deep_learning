import numpy as np
from d2l import torch as d2l


def f(x):
    return x ** 3 - 1 / x


x = np.arange(0.1, 3, 0.1)
d2l.plot(x, [f(x), 4 * x - 4], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
d2l.plt.show()
