######################################################################
# Author: Thy H. Nguyen     TODO: Change this to your names
# Username: nguyent2        TODO: Change this to your usernames
#
# Assignment: A06: It's in your Genes
#
# Purpose: A test suite to test the a6_genes code
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

import sys
from a6_genes import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def genomics_test_suite():
    """
    The genomics_test_suite() is designed to test the following:
      is_nucleotide(sequence)
      complement_strand()
      mRNA()
      chunk_amino_acid()
      amino_acid_chunks()
      sequence_gene()


    :return: None
    """

    # TODO   We highly suggest starting by building more test cases for each function.
    # TODO   If you can build accurate test cases, you can be confident that you understand
    # TODO   the intended functionality of each function.

    # The following tests test the is_nucleotide() function
    print("Testing is_nucleotide()")
    testit(is_nucleotide("CGTAGGCAT") == True)
    testit(is_nucleotide("CGTAFLCAT") == False)
    testit(is_nucleotide("TAG") == True)
    testit(is_nucleotide("CAB")== False)
    testit(is_nucleotide("THY")==False)
    testit(is_nucleotide("CSC226")==False)
    testit(is_nucleotide("ScottHeggen")==False)
    testit(is_nucleotide("ATGX")==False)
    testit(is_nucleotide("ATGC")==True)
    testit(is_nucleotide("ATGCATGCATGCGCGCGCGC")==True)
    testit(is_nucleotide("CGTCGTCGTCGTCCCCAAAAAAAAAAAA")==True)
    # FIXME: Add your own tests here
    # Completed adding the tests

    # Testing the complement_strand() function
    print("\nTesting complement_strand()")
    testit(complement_strand("CC") == "GG")
    testit(complement_strand("CA") == "GT")
    testit(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    testit(complement_strand("CGTAFLCAT") == "Sequencing Error")
    testit(complement_strand("CAT")=="GTA")
    testit(complement_strand("GTG") == "CAC")
    testit(complement_strand("ThyIsTheCutestGirl")== "Sequencing Error")
    testit(complement_strand("CATCATCATCAT")=="GTAGTAGTAGTA")
    testit(complement_strand("ILoveCSC226")=="Sequencing Error")
    testit(complement_strand("CGTAGGCATTTTTTTTTTT") == "GCATCCGTAAAAAAAAAAA")
    testit(complement_strand("cat")=="Sequencing Error")
    testit(complement_strand("gtg")=="Sequencing Error")
    # FIXME: Add your own tests here
    # Completed adding the tests

    # Testing the mRNA() function
    print("\nTesting mRNA()")
    testit(mRNA("GCATCCGTA") == "GCAUCCGUA")
    testit(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    testit(mRNA("AAGCACCG") == "AAGCACCG")
    testit(mRNA("CGTAFLCAT") == "Sequencing Error")
    testit(mRNA("CAT") =="CAU")
    testit(mRNA("TTA") == "UUA")
    testit(mRNA("THYISTHECUTESTGIRL") == "Sequencing Error")
    testit(mRNA("GCATCCGTACCATTGGGTTCCGTACCATTGGGCCGTACCATTGGGCCGTACCATTGGGCCGTACCATTGGGTHY") == "Sequencing Error")
    testit(mRNA("CATCATCATCAT") == "CAUCAUCAUCAU")
    testit(mRNA("cat")=="Sequencing Error")
    testit(mRNA("tta")=="Sequencing Error")
    # FIXME: Add your own tests here
    # Completed adding the tests


    # Testing chunk_amino_acid()
    print("\nTesting chunk_amino_acid()")
    testit(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    testit(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded
    testit(chunk_amino_acid("CAGUACGAT")==["CAG", "UAC", "GAT"])
    testit(chunk_amino_acid("CCGUGGGATAT") ==["CCG","UGG","GAT"])
    # These tests belows show that actually chunk_amino_acid() works well with all strings.
    testit(chunk_amino_acid("XuanThy")==["Xua","nTh"])
    testit(chunk_amino_acid("ILoveCSC226")==["ILo","veC","SC2"])
    testit(chunk_amino_acid("[1234]")==["[12","34]"])
    # FIXME: Add your own tests here
    # Completed adding the tests

    # Testing amino_acid_chunks()
    print("\nTesting amino_acid_chunks()")
    testit(amino_acid_chunks('AGA') == 'R')
    testit(amino_acid_chunks('AFA') == '?')
    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME: understand the dictionary in this function to write more of these tests

    # Testing sequence_gene()
    print("\nTesting sequence_gene()")
    testit(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    testit(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    testit(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                # and ignoring the last two "extra" nucleotides,
                                                # this returns amino acid "V".
    testit(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                # taking the complement and then replacing the T nucleotide with U.
                                                # Grouping into triples, we  get the "ASV" amino acid sequence.

    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME  understand the dictionary in amino_acid_chunks() to write more of these tests


def main():
    genomics_test_suite()


main()
