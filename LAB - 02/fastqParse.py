class FastqString(str):
    '''
    FastqString class takes a FASTQ sequence name line as input and provides
    a method to parse and display each field of the run information.

    Example Input:
    @EAS139:136:FC706VJ:2:2104:15343:197393
    
    Output:
    Instrument = EAS139
    Run ID = 136
    Flow Cell ID = FC706VJ
    Flow Cell Lane = 2
    Tile Number = 2104
    X-coord = 15343
    Y-coord = 197393
    '''

    def parse(self):
        '''Parse the FASTQ seqname line and display each field.'''
        fields = self.split(":")
        print(f"Instrument = {fields[0][1:]}\n" +
              f"Run ID = {fields[1]}\n" +
              f"Flow Cell ID = {fields[2]}\n" +
              f"Flow Cell Lane = {fields[3]}\n" +
              f"Tile Number = {fields[4]}\n" +
              f"X-coord = {fields[5]}\n" +
              f"Y-coord = {fields[6]}")

def main():
    '''
    Prompt the user for a FASTQ seqname line, create a FastqString object,
    and parse the information.
    '''
    seqname = input("Enter the FASTQ seqname line: ")
    fastq = FastqString(seqname)
    fastq.parse()

if __name__ == "__main__":
    main()
