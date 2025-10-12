import time

def measure_time(func):
    def wrapper(initial, rate, time_period):  # fixed parameters
        start = time.perf_counter()
        result = func(initial, rate, time_period)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@measure_time
def population_growth(initial, rate, time_period):
    for _ in range(10**6):
        pass
    print("Population simulated.")

population_growth(1000, 0.002, 5)
