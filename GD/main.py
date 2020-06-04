import random

from repo.reader import Reader


from service.gd import GradientDescentMethod


def main():
    reader = Reader("2017.csv")
    inputs1, inputs2, outputs = reader.read("Economy..GDP.per.Capita.", "Freedom", "Happiness.Score")

    # inputs = [ [gdp1, gdp2, ..., gdpn], [freedom1, freedom2, ..., freedomn]]
    # outputs = [ happiness1, happiness2, ..., happinessn]
    inputs = [inputs1]
    gd = GradientDescentMethod(0.01, 100)
    gd.gradient_descent(inputs, outputs)


main()