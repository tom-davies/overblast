from Bio import SeqIO, SearchIO, Entrez
from Bio.Blast import NCBIWWW
import os
#import texttable as tt

os.system('cls' if os.name == 'nt' else 'clear') #clear screen

'''file_gbk = raw_input("genbank file? ")
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
result_handle = open("origin_blast.xml")'''

blast_table = SearchIO.read('origin_blast.xml', 'blast-xml')
names = []
tax_length = []
print("Taxonomy Search in Progress, Please Wait."),
for x in range(50):
    hit = blast_table[x].id.split("|")
    the_id = hit[1]
    # Entrez Search
    Entrez.email = "thomas.davies-7@student.manchester.ac.uk"
    search = Entrez.efetch(db="nuccore", id=the_id, retmode="xml")
    print('ding')
    records = Entrez.read(search)
    print('dong')
    taxon = records[0]["GBSeq_taxonomy"].split("; ")
    print('the witch')
    name = records[0]["GBSeq_source"]
    print('is dead')
    names.append(name)
    tax_length.append(len(taxon))
    print('.'),

print(names)
print(tax_length)

print("Press Any Key to Exit...")
raw_input()
