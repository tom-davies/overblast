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

for cycle in range(1, 11):
	t = cycle*s
	#Send Sequence to BLASTx
	print("Running BLAST %d , Please Wait." % cycle)
	result_handle = NCBIWWW.qblast("blastx", "nr", seq_origin.seq[u:t])
	save_file = open("origin_blast" + str(cycle) + ".xml","w")
	save_file.write(result_handle.read())
	save_file.close()
	result_handle.close()
	result_handle = open("origin_blast" + str(cycle) + ".xml")
	print
	u = t

print("Press Any Key to Exit...")
raw_input()