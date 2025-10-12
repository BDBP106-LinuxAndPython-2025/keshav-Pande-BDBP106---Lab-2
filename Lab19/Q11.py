def log_function_call_alt(func):
    def wrapper(sequence):
        print("Running DNA analysis....")
        result = func(sequence)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call_alt
def analyse_dna(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100

sequence = "ATGCGCGTAACG"
print(f"GC %: {analyse_dna(sequence):.2f}%")
