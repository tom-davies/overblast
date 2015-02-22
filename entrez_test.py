from Bio import SeqIO, SearchIO, Entrez
import os
import pdb

os.system('cls' if os.name == 'nt' else 'clear')

blast_table = SearchIO.read('origin_blast.xml', 'blast-xml')
names = []
tax_length = []
print("Taxonomy Search in Progress, Please Wait."),
for x in range(50):
    hit = blast_table[x].id.split("|")
    the_id = hit[1]
    print(the_id)
    # Entrez Search
    #pdb.set_trace()
    Entrez.email = "thomas.davies-7@student.manchester.ac.uk"
    search = Entrez.efetch(db="nuccore", id=the_id, retmode="xml")
    records = Entrez.parse(search)
    for record in records:
        #print(record["GBSeq_taxonomy"].split("; "))
        name = record['GBSeq_source']
        names.append(name)
        tax_length.append(record["GBSeq_taxonomy"].split("; "))
    print('.'),

print(names)
print(tax_length)
