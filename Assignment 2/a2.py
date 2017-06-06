def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.count(dna2) > 0

def is_valid_sequence(dna):
    """(str) -> bool
    
    Return True if DNA sequence contains only letters 'A, T, C or G'
    
    >>>is_valid_sequence('A432')
    False
    """
    for c in dna:
        if c != 'A' or c != 'T' or c != 'C' or c != 'G':
            return False
    return True

def insert_sequence(dna1, dna2, pos):
    """(str,str,int) -> str
    
    Return sequence of dna1 inserted dna2 in position pos
    >>>insert_sequence("CCGG","AT",2)
    CCATGG
    """
    newdna = dna1[:pos] + dna2 + dna1[pos:]
    return newdna
    
    
def get_complement(nucleotide):
    """(str)->str
    Return the complement of nucleotide
    >>>get_complement("ACGTACG")
    TGCATGC
    """
    complementDNA = ""
    for c in nucleotide:
        if(c == "A"):
            complementDNA = complementDNA + "T"
        elif(c == "T"):
            complementDNA = complementDNA + "A"  
        elif(c == "G"):
            complementDNA = complementDNA + "C"  
        elif(c == "C"):
            complementDNA = complementDNA + "G"
        
    return complementDNA

def get_complementary_sequence(dna):
    """(str)->str
        Return the complement of nucleotide
        >>>get_complement("ACGTACG")
        TGCATGC
        """
    complementDNA = ""
    for c in dna:
        if(c == "A"):
            complementDNA = complementDNA + "T"
        elif(c == "T"):
            complementDNA = complementDNA + "A"  
        elif(c == "G"):
            complementDNA = complementDNA + "C"  
        elif(c == "C"):
            complementDNA = complementDNA + "G"
        
    return complementDNA

        
        
        
        
        
        
        
        
        
        
        
        