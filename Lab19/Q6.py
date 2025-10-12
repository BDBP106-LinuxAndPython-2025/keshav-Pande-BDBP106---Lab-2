def analyse_dna(sequence):
    def gc_content(seq):
        g = seq.count('G')
        c = seq.count('C')
        gc = ((g + c) / len(seq)) * 100
        return gc

    gc_percent = gc_content(sequence.upper())  
    if gc_percent > 50:
        print("GC-rich sequence (GC% = {:.2f})".format(gc_percent))
    else:
        print("AT-rich sequence (GC% = {:.2f})".format(gc_percent))

seq = input("Enter a DNA sequence: ")
analyse_dna(seq)

