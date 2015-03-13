from Bio import SeqIO, SearchIO, Entrez
from Bio.Blast import NCBIWWW
import os

os.system('cls' if os.name == 'nt' else 'clear') #clear screen

# file_gbk = raw_input("genbank file? ")
# # Parse genbank files
# for seq_origin in SeqIO.parse(file_gbk, "genbank"):
#     print seq_origin.id, ":", seq_origin.description
#     print seq_origin
# print
#
# #Send Sequence to BLASTn
# print("Running BLAST , Please Wait.")
# result_handle = NCBIWWW.qblast("blastn", "nr", seq_origin.seq, entrez_query="all[filter] NOT((srcdb_refseq_model[prop] AND biomol_rna[prop]))")
# blast_file = open("origin_blast.xml","w")
# blast_file.write(result_handle.read())
# blast_file.close()
# result_handle.close()
# result_handle = open("origin_blast.xml")

blast_table = SearchIO.read('origin_blast.xml', 'blast-xml')
print("Taxonomy Search in Progress, Please Wait.")
names = []
taxons = []
for x in xrange(50):
    hit = blast_table[x].id.split("|")
    the_id = hit[1]
    print(x+1),
    # Entrez Search
    Entrez.email = "thomas.davies-7@student.manchester.ac.uk"
    search = Entrez.efetch(db="nuccore", id=the_id, rettype="gb", retmode="text")
    for record in SeqIO.parse(search, "genbank"):
        name = record.annotations['organism']
        names.append(name)
        taxon = record.annotations['taxonomy']
        taxons.append(len(taxon))
        print("\t" +name),
        print("\t\t"),
        print(len(taxon))
    search.close()

print("Press Any Key to Exit...")
raw_input()
