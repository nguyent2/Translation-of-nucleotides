######################################################################
# Author: Thy H. Nguyen     TODO: Change this to your names
# Username: nguyent2        TODO: Change this to your usernames
#
# Assignment: A06: It's in your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

# TODO   I highly suggest starting by building more test cases for each function in the test suite file.
# TODO   If you can build accurate test cases, you can be confident that you understand
# TODO   the intended functionality of each function.


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: input of the user (the string that needs checking the validity)
    :return: True, if the sequence puts in is a DNA; False, if it is not a DNA.
    """
    # FIXME: Finish the docstring above
    #Completed

    # FIXME: Add your code here to complete this function
    for i in range((len(sequence))): #For each character in the input
        if sequence[i] == "A" or sequence[i] == "C" or sequence[i] == "G" or sequence[i] == "T":
            i+=1
        #Check to see if the character is the letter A, C, G, or T
        #If it passes, do it again with the next character in the input
        else:
        #If any character does not pass, immediately return False and end the function
            return False

    # FIXME: Clearly this should not always return True
    return True
    #If all of the characters pass the test, return True
    #The function is already fixed above


def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence: the string the user puts in
    :return: complement: the second strand of the DNA sequence corresponding to the user's input
    """
    # FIXME: Finish the docstring above
    #Completed

    complement = ""         # This can be used to "build" the complement

    # FIXME: Add your code here to complete this function
    original = ["A","T","G","C"]
    # create an original list of valid character
    new = ["T","A","C","G"]
    # create a new list after transfering the input into the second strand of the DNA sequence
    if is_nucleotide(sequence) == True:
        # if the input has exactly only A, T, G, C
        for i in range(len(sequence)):
            #loop the times corresponding to the numbers of characters in the input sequence
            for j in range(4):
                #loop 4 times to check each character in the original list
                if sequence[i] == original[j]: #Check to see the order of the character in the list original
                    complement = complement+new[j]
                    #replace the character at jth position in original list with the jth position in new list and saves the new under the variable complement
    else:
        complement = "Sequencing Error"
        # If the input has any character other than A, T, G, C, print out Sequencing Error since those other characters cannot be transferred.

    # FIXME: Obviously, this should not always return ""
    return complement


def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence:the variable complement, which is returned from the function complement_strand() above
    :return: mRNA (The sequence of mRNA)
    """
    # FIXME: Finish the docstring above
    #Completed
    # FIXME: Add your code here to complete this function

    mrna = ""
    for i in range(len(sequence)):
    # Looping through all characters in the sequence (sequence is whatever returned from the function complement_strand())
        if sequence[i] == "T":
            #If there is a T , that position of T will become U in mrna
            mrna = mrna + "U"
            #Saving the new letter U in mrna (at the same position of T in sequence)
        elif sequence[i] == "A" or sequence[i] == "G" or sequence[i] == "C":
        # If there is any A, G, C, saving the same position of A,G,C in mrna
            mrna = mrna + sequence[i]
        else:
            #if any letter other than A,G,C,T, add the string "Sequencing Error" into mrna
            mrna = mrna + "Sequencing Error"
    # FIXME: Obviously, this should not always return ""
    if mrna.count("Sequencing Error") > 0:
    #Count the Sequencing Error in mrna, if the count is greater than 0 (which means at least has 1 Sequencing Error)
        mrna = "Sequencing Error"
        #Replace mrna to the new string: "Sequencing Error"
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: the mrna returned from the function mRNA()
    :return: list_of_chunks, the substrings of length 3, from mrna, ignoring any "extra DNA"
    """
    # FIXME: Finish the docstring above
    #Completed

    # FIXME: Add your code here to complete this function

    list_of_chunks = []
    i = 0 #Start at the 0-position (the first character) in the string
    while i < (len(sequence) - 2): #As long as the count of i is less than the length of the string minus 2,
        #push the three_characters into the list
        three_characters = sequence[i]+sequence[i+1]+sequence[i+2]
        list_of_chunks.append(three_characters)
        i +=3   #Since three characters are already taken, the next one will be i+3
    # FIXME: Obviously, this should not always return an empty string
    return list_of_chunks

def amino_acid_chunks(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character AminoAcid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    # We haven't learned about dictionaries yet, but here is one for the extra curious.
    # You aren't expected to know what this is yet.
    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a a sequence of nucleotides:
    A, C, G, and T and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + amino_acid_chunks(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """

    # TODO When your code is fixed, the following line will print correctly.
    # TODO You do not need to modify the sequence_gene() function; it is correct already.
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))


if __name__ == "__main__":
    main()          # call to main() function
