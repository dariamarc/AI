from random import uniform

class Utils:
    def generateNewValue(self, lim1, lim2):
        return uniform(lim1, lim2)

    def binToInt(self, x):
        val = 0
        # x.reverse()
        for bit in x:
            val = val * 2 + bit
        return val