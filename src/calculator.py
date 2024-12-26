class NumCalculator:

    def plus(self, x, y):
        return x + y

    def minus(self, x , y):
        return x - y

    def mult(self, x, y):
        if type(y) is str or type(x) is str:
            raise TypeError("str type is not allowed")
        return x * y

    def div(self, x, y):
        return x/y

    def full_div(self, x, y):
        return x // y

    def end_div(self, x, y):
        if type(y) is float or type(x) is float:
            raise TypeError("float type is not allowed")
        return x % y
