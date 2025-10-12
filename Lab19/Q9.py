import math


def population_growth(initial, rate, time):
    def exponential_growth():
        return initial + math.exp(rate * time)

    population = round(exponential_growth())
    print("Population after time =", population)


# Test
population_growth(1000, 0.002, 5)
