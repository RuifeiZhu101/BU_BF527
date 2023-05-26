#!/usr/bin/python

#The task is to identify non-standard amino acids in the protein sequence:'BACKTOTHEFUTURE'
#'B','J','O','U','X',and 'Z' are not amino acids

sequence = 'BACKTOTHEFUTURE'	  #store the sequence as a string
not_aas = ['B','J','O','U','X','Z']	#store the non-standard amino acids in a list

#Looping through the sequence
for aa in sequence:
	if aa in not_aas:	#check if the amino acid is non-standard
		print (aa)


