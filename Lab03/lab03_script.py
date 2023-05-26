
#!/usr/bin/python

num_genes = 23000 #protein coding genes
avg_length = 3000.0 #avg. base pairs
total_genome = 3E9 #total base pairs

#Approximate total gene coding length
total_gene_length = num_genes * avg_length

#Proportion of codin genes in genome
proportion_gene = total_gene_length / total_genome

#Print answers
print "total_gene_length",total_gene_length,"\n",
"coding part of the genome", 100*proportion_gene, "%"

#Indexing example with strings
sequence = 'ASDFQWERTY'
first_aa = sequence[0]		#potions/indices start with 0, NOT 1
sec_aa = sequence [1]
last_aa = sequence[-1]		#read backwards with negatie indices
sec2_last_aa = sequence[-2]
print sequence,first_aa, sec_aa, last_aa, sec2_last_aa, "\n"
#"\n" is a "newline" character. You can use it to visually separate print statements

#Indexing example with lists
positions = [1, 3, 7, 11, 22, 'one million', '42', "\n"]
first_pos = positions[0]
sec_pos = positions[1]
last_pos = positions[-1]
sec2_last_pos = positions[-2]
print positions, first_pos, sec_pos, last_pos, sec2_last_pos

#You can access multiple sequential elements. This is called slicing.
#In Python you always specify the starting index
# and the index AFTER the stopping index
mid_two_aa = sequence[4:6] #This will give the 5th and 6th element 
first_3_aa = sequence[0:3] #0 is optional: sequence[:3]
sec_two_pos = positions[1:3] 
last_two_pos = positions[-3:]
print mid_two_aa, first_3_aa, sec_two_pos, last_two_pos, "\n"


