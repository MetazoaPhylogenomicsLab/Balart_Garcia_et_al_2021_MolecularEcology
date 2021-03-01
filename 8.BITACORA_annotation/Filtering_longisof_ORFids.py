
##Script for filtering longest isoforms of Bitacora hits with Transdecoder headings. First delete ".p*" and "_i*", then last "_" ("output_file") and finally get the longest unique gene.
###Install SeqIO (Biopython)
####Command to execute it: python3 Filtering_longisof_ORFids.py > out_longest_isof.fasta

from Bio import SeqIO

input_file = "<path to hits-bitacora.fasta>"
output_file = "<path for output_file>"

input_file = list(SeqIO.parse(input_file, 'fasta'))

output = open(output_file, "w")

for i in input_file:
	if (i.id.endswith('.p', 0, -1)):
		output.write(">" + i.id[:-6] + "\n") 
		output.write(str(i.seq) + "\n")

output.close()

input_file = list(SeqIO.parse(output_file, 'fasta'))

output = open(output_file, "w")

for i in input_file:
	if (i.id.endswith('_')):
		output.write(">" + i.id[:-1] + "\n")
		output.write(str(i.seq) + "\n")
	else:
		output.write(">" + i.id + "\n")
		output.write(str(i.seq) + "\n")


output.close() 

from Bio import SeqIO
import sys

lastGene = None
longest = (None, None)
for rec in SeqIO.parse(output_file, "fasta"):
    gene = "_".join(rec.id.split("n/"))
    l = len(rec)
    if lastGene is not None:
        if gene == lastGene:
            if longest[0] < l:
                longest = (l, rec)
        else:
            lastGene = gene
            SeqIO.write(longest[1], sys.stdout, "fasta")
            longest = (l, rec)
    else:
        lastGene = gene
        longest = (l, rec)
SeqIO.write(longest[1], sys.stdout, "fasta")