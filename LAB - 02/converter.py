'''
This script converts between different codon and amino acid representations.
It uses DNA and RNA codon tables as well as mappings between short and long amino acid codes.
'''

short_AA = {
    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
}

# Creating a reverse mapping for long amino acid names to short names
long_AA = {value: key for key, value in short_AA.items()}

RNA_codon_table = {
# Second Base
# U C A G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---'
, 'UGA': '---'
,
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---'
, 'UGG': 'Trp',
#C
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}

# Creating a DNA codon table from the RNA codon table
dnaCodonTable = {key.replace('U', 'T'): value for key, value in RNA_codon_table.items()}

def main():
    '''
    Converts DNA/RNA codons or amino acid codes to their respective translations.
    '''

    input_code = input("Enter a DNA/RNA codon or an amino acid code: ").upper()

    # DNA/RNA codon conversion
    if input_code in dnaCodonTable:
        # For DNA codons, convert to uppercase amino acid name
        print(f"{input_code} = {dnaCodonTable[input_code].upper()}")
    elif input_code in RNA_codon_table:
        # For RNA codons, similarly convert to uppercase amino acid name
        print(f"{input_code} = {RNA_codon_table[input_code].upper()}")
    elif len(input_code) == 1:
        # For one-letter amino acid codes, find the three-letter equivalent
        if input_code in long_AA:
            print(f"{input_code} = {long_AA[input_code].upper()}")
        else:
            print("Unknown code")
    elif len(input_code) == 3:
        # For three-letter amino acid codes, convert to one-letter code
        # input_code = input_code.capitalize()  # Correct the casing for dictionary lookup
        if input_code in short_AA:
            print(f"{input_code.upper()} = {short_AA[input_code]}")
        else:
            print("Unknown code")
    else:
        print("Unknown code")

if __name__ == "__main__":
    main()
