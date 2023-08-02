# A06: It's in your Genes

Name 1: T. H. Molena Nguyen

Repository Link: https://github.com/2019-fall-csc-226/a06-it-s-in-your-genes-nguyent2-a06.git

## Milestone Reports

Update on progress on this assignment.

Sunday, October 6, 2019
* Fixing READMe, and answering several questions on the Google drive link.
* Adding a scratch work to run each function separately to test it clearly
* Fixing function is_nucleotide()
* There were no bugs during the coding, since I tested the function separately in the scratch work file to make sure each function works properly

Monday, October 7, 2019
* Completed debugging is_nucleotide()
* Completed function complement_strand()
* Completed debugging and testing the two functions (is_nucleotide() and complement_strand()
* There were no bugs during the code, since I tested the functions separately (with inputs) in the scratch work file

Tuesday, October 8, 2019
* Completed function mRNA()
* Completed debugging and testing the three functions (is_nucleotide(), complement_strand(), and mRNA())
* Completed filling in the Google doc
* There were no bugs during the code

Wednesday, October 9, 2019
* Completed chunk_amino_acid()
* Completed debugging and testing all of the functions
* At first, there were bugs about the index errors in the string, then I figured it out.

Wednesday, October 16,2019
* Reviewing all of the codes
* Adding more tests in the test suite and adding comments into the code
* Writing the reflection and summary (based on the format of Readme file in Project A05)
* COMPLETED THE WHOLE PROJECT

#### USING THE FORMAT OF README IN PROJECT A05 TO WRITE THE REFLECTION AND SUMMARY FOR PROJECT A06

## INITIAL DESIGN PLAN:

Summarize a plan which meets the computational requirements to solve the problem. My plan does not need to be syntactically correct. It needs to capture the flow of logic in a human readable format.
1. Function is_nucleotide(): Check if each character in the string the user put in is one of the only 4 characters A,C,G,T or not.
2. Function complement_strand():  Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs.
3. Function mRNA(): Replaces each occurrence of the nucleotide T replaced with the nucleotide U. Return the corresponding mRNA of the input
4. Function chunk_amino_acid(): Uses output of mRNA(sequence) and divides it into substrings of length 3, ignoring any "extra DNA" at the far end returning the relevant substrings in a list.
5. Function amino_acid_chunks():  Expects a three character string as a parameter and returns the corresponding single character AminoAcid
6. Function sequence_gene(): Takes a a sequence of nucleotides: A, C, G, and T and returns the corresponding amino acid sequence.  

## IMPLEMENTATIONS:

A list in bullet form of each function I created, and what is each function’s purpose.
* Function is_nucleotide()
* Function complement_strand()
* Function mRNA()
* Function chunk_amino_acid()
* Function amino_acid_chunks()
* Function sequence_gene()
 
## TESTING:

1. Test each function separately in the Scratch work file 
2. Test all functions with the test_suite file

## ERRORS:

A list in bullet form of all known errors and deficiencies in my implementation.
* IndexError: the index is not in the string  

## SUMMARY:

A brief summary description of the design and implementation, including how much my initial design plan evolved, the final result I achieved, and the amount of time I spent as a programmer in accomplishing these results. This should be no more than two paragraphs. Consider this like a report of what I did.

This program is useful for biologist or anyone who works in the lab relating to genes. Each function is a part of the program, which makes the program easier to read.
It is so easy to follow the algorithm implemented in this program, as each function serves as a part of the program.
The logic in the functions (the way the functions are designed) makes it much easier for programmers to read and understand the code.

## COMMENTS:

A paragraph or so of my own comments on and reactions to this assignment. Consider this like a reflection.

I have learned one more new way to code. I have always been calling functions inside the functions, which makes it easier to get bugs with parameters. Therefore, with this new guide,
it is much easier to write the code and debug the program. The test suites are also clear about what codes and algorithm should I make inside each small function to reach what the function does. 
