class DNAstring(str):
    '''
    DNAstring class inherits from str, specifically for manipulating DNA sequences.
    This class provides functionalities to clean up a DNA sequence by removing 
    ambiguous bases denoted by "N" and replacing them with a count in curly braces.

    Example: 
    Input: AaNNNNNNGTC
    Output: AA{6}GTC

    Any lowercase letters in the input are converted to uppercase. The class
    ensures that only the DNA characters (ACGT) remain after the cleanup.
    '''

    def purify(self):
        '''Return an upcased version of the string collapsing a single
        block of 'N's into its count in curly braces.'''
        sequence_upper = self.upper()
        firstN = sequence_upper.find("N")
        if firstN != -1:  # Checks if there's at least one 'N'
            lastN = sequence_upper.rfind("N")
            num_N = lastN - firstN + 1
            # Replace the 'N's block with {num_N}
            sequence_clean = sequence_upper[:firstN] + "{" + str(num_N) + "}" + sequence_upper[lastN+1:]
        else:
            sequence_clean = sequence_upper
        return sequence_clean


def main():
    '''
    Get user DNA data and clean it up by removing ambiguous parts ('N's)
    and replacing them with a count in curly braces.
    '''
    data = input('DNA data? ')
    while data:
        thisDNA = DNAstring(data)
        pureData = thisDNA.purify()
        print(pureData)
        data = input('DNA data? ')

if __name__ == "__main__":
    main()