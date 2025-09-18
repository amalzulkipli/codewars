# mine
def DNA_strand(dna):
    dna_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    result = ''
    for amino_acid in dna:
        result += dna_dict[amino_acid]
    return result

# pythonic
def DNA_strand(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))
