from Bio import SeqIO, SearchIO, Entrez
from Bio.Blast import NCBIWWW
import sys
print(sys.version)
file_gbk = raw_input("genbank file? ")
# Parse genbank files
'''for seq_origin in SeqIO.parse(file_gbk, "genbank"):
        print seq_origin.id, ":", seq_origin.description
print

print("Running Mammalian BLAST , Please Wait.")
result_handle = NCBIWWW.qblast("blastn", "nr", seq_origin.seq, entrez_query="all[filter] txid40674[ORGN] NOT((srcdb_refseq_model[prop] AND biomol_rna[prop]))")
blast_file = open("origin_blast.xml","w")
blast_file.write(result_handle.read())
blast_file.close()
result_handle.close()
result_handle = open("origin_blast.xml")'''

blast_table = SearchIO.read('origin_blast.xml', 'blast-xml')
print("\aTaxonomy Search in Progress, Please Wait.")
names = []
taxons = []
for x in blast_table:
    hit = blast_table[x].id.split("|")
    the_id = hit[1]
    print("\a")
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
print(list(set(names)))
print(list(set(taxons)))
print("\a\a\a\a\a")
