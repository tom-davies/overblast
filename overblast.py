from Bio import SeqIO, SearchIO, Entrez
from Bio.Blast import NCBIWWW
import os

#os.system('cls' if os.name == 'nt' else 'clear') #clear screen

file_gbk = raw_input("genbank file? ")
# Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
        print seq_origin.id, ":", seq_origin.description
print

#Send Sequence to BLASTn
print("Running BLAST , Please Wait.")
result_handle = NCBIWWW.qblast("blastn", "nr", seq_origin.seq, entrez_query="all[filter] NOT((srcdb_refseq_model[prop] AND biomol_rna[prop]))")
save_file = open("origin_blast.xml","w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
result_handle = open("origin_blast.xml")

blast_table = SearchIO.read('origin_blast.xml', 'blast-xml')
final_hit = blast_table[-1].id.split("|")
final_id = final_hit[1]
print(final_id)

# Entrez Search
Entrez.email = "thomas.davies-7@student.manchester.ac.uk"
search = Entrez.efetch(db="nuccore", id=final_id, retmode="xml")
records = Entrez.read(search)
taxon = records[0]["GBSeq_taxonomy"].split("; ")
print (taxon)
print (len(taxon))

'''print("Press Any Key to Exit...")
raw_input()'''
