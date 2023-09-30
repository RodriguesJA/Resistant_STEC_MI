
import os
import urllib
import re

genome_file = open("[directory] Genomes.txt")
read_genome_file = genome_file.readlines()


for i in read_genome_file:
	i = i.rstrip("\n")
	i = i.rstrip("\r")
	i = str(i) #Similar to the above code, we are reading the genomes and stripping the tabs and spaces to set up a loop for all the genomes

	os.system("staramr search --pointfinder-organism    -o [path]" + i + "--mlst-scheme  [path]/" + i + ".fasta")

	print ("done " + i)
