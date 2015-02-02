from Bio import SeqIO
from Bio.Blast import NCBIWWW
file_gbk = raw_input("genbank file? ")
# Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
        print seq_origin.id, ":", seq_origin.description
print

#Generating smaller sequences for BLAST
u = 0
length = len(seq_origin.seq)
s = length/10

for number in range(1, 11):
	t = number*s
	print(seq_origin.seq[u : t])
	print
	u = t