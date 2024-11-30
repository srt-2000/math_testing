class Fcalc:

    def factor(self, x):
        if x == 1 or x == 0:
            return 1
        else:
            return x * self.factor(x - 1)
