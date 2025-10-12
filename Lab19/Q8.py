import random


def protein_energy(temp):
    def calculate_free_energy(enthalpy, entropy):
        return enthalpy - (temp * entropy)

    ΔH = float(input("Enter enthalpy change (ΔH): "))
    ΔS = float(input("Enter entropy change (ΔS): "))

    ΔG = calculate_free_energy(ΔH, ΔS)
    if ΔG < 0:
        return f"ΔG = {ΔG:.2f}, Protein is stable"
    else:
        return f"ΔG = {ΔG:.2f}, Protein is unstable"


print(protein_energy(298))
