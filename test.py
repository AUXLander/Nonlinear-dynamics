import math as Math

def sgn(position : float):
    return Math.copysign(1.0, f(position))

def f(x : float, alpha : float = -3, c_hill : float = 2):
    return alpha / (1.0 + x ** c_hill) - x

def f_(x : float, alpha : float = -3, c_hill : float = 2):
    return - (1.0 + alpha * c_hill * (x ** (c_hill - 1.0)) / (1.0 + x ** c_hill) ** 2)

class Tracker:
    def __init__(self):
        self.path = []
        self.delta = []

    def trace(self, x : float, y : float):
        
        if self.path.count() > 0:
            _x, _y = self.path[-1]
            self.delta.append( (abs(_x - x), abs(_y - y)) )

        self.path.append((x,y))

    def xdelta(self):
        return [point[0] for point in self.delta]

    def ydelta(self):
        return [point[1] for point in self.delta]

    def xpath(self):
        return [point[0] for point in self.path]

    def ypath(self):
        return [point[1] for point in self.path]

    def answer(self):
        return self.path[-1]

    def reset(self):
        self.path.clear()




def bisection(func, x_left : float, x_right : float, epsilon_x : float = 1e-3, epsilon_y : float = 1e-7):
    assert(x_right > x_left)
    assert(epsilon_x < 1e-1)
    assert(epsilon_y < 1e-1)

    recorder = Tracker()

    x = x_left

    while x_right - x_left > epsilon_x:

        x = (x_left + x_right) / 2
        y = func(x)
        
        recorder.trace(x, y)

        if (abs(y) <= epsilon_y):
            break
        elif (sgn(x) != sgn(x_left)):
            x_right = x
        else:
            x_left = x

    return recorder

def newton(func, func_, x0 : float, epsilon_x : float = 1e-3, epsilon_y : float = 1e-7):
    assert(epsilon_x < 1e-1)
    assert(epsilon_y < 1e-1)

    recorder = Tracker()

    x = x0
    y = func(x)

    slope = y / func_(x)

    while abs(slope) > epsilon_x or y > epsilon_y:
        recorder.trace(x, y)

        x = x - slope
        y = func(x)

        slope = y / func_(x)

    recorder.trace(x, y)

    return recorder


#x = bisection(f, -3, 2)



x = newton(f, f_, 10)
print(x.path)