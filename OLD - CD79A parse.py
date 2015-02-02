from Bio import SeqIO
from Bio.Blast import NCBIWWW
file_gbk = raw_input("genbank file? ")
# Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
        print(seq_origin.id)
        print(repr(seq_origin.seq))
        print(len(seq_origin))
print

#Send Sequence to BLASTn
print("Running BLAST, Please Wait.")
result_handle = NCBIWWW.qblast("blastx", "nr", seq_origin.seq)
save_file = open("origin_blast.xml","w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
result_handle = open("origin_blast.xml")

print
print("Press Any Key to Exit...")
raw_input()