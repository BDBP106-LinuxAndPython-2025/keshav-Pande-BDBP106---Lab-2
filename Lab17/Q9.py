def extract_codons(sequence, start_position):
    # Adjust start position to zero-based index
    start_index = start_position - 1
    codons = []

    # Loop through sequence in steps of 3
    for i in range(start_index, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        codons.append(codon)

    return codons


# Test case
sequence = "GTTTCGATTATAACG"

print("DNA Sequence:", sequence)
print("Codons from 1st position:", extract_codons(sequence, 1))
print("Codons from 3rd position:", extract_codons(sequence, 3))
