import random
from math import log


def randrange_logarithmic(lower, upper):
    lower_exp = round(log(lower) / log(10))
    upper_exp = round(log(upper) / log(10))

    rand_exp = random.randrange(lower_exp, upper_exp)

    lower_ = 10 ** rand_exp
    upper_ = lower_ * 10

    return random.randrange(lower_, upper_)
