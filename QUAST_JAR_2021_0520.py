import os
import urllib
import re


Campy_Genomes_file = open( "/mnt/gs18/scratch/groups/manninglab/merged_ecoli_genomes.txt" ) #Text file with all the genomes to be used in this pipeline. File is used instead of a directory in order to easily edit which genomes are utilized
Campy_Genomes_pair = Campy_Genomes_file.readlines() #Here you are reading all of the file names within a specific folder readlines enables this fx 

for i in Campy_Genomes_pair: #Here we are stripping tabs and spaces from file names 
	i = i.rstrip("\n")
	i = i.rstrip("\r") 
	print (i)
	pairGenome = i.split("\t")  
	RefGenome = str(pairGenome[0])  #Here we place all of the integers within our file that we read and stripped into an array. In this case each TW# Will be in an array that is called RefGenome
	os.system("quast.py -o /mnt/gs18/scratch/groups/manninglab/quast_results/" + RefGenome + "  /mnt/gs18/scratch/groups/manninglab/Genomes_Query/"+ RefGenome +".fasta")
	print(RefGenome + "_DONE")
#The above loop using the shell command to inact prokka while out putting the the files in the directory .../Prokka as well as appending the RefGenome loop. Therefore each TW# will run through this loop and the last line prints which TW# is being utilized