import random

def rand_int(min, max):
    return random.randint(min, max)

def rand_float(min, max):

    r = random.uniform(min, max)
    r *= 10 ** round
    r = int(r)
    r = float(r)
    r /= 10 ** round
    return r

def chance(percent):

    if percent <= 0:
        return False
    elif percent >= 100:
        return True

    r = rand_float(0, 100)
    if r <= percent:
        return True

    return False

def rand_rgb():
    return [rand_int(0, 255), rand_int(0, 255), rand_int(0, 255)]

def rand_point(rect):

    x = rand_int(rect[0], rect[2])
    y = rand_int(rect[1], rect[3])

    return [x, y]