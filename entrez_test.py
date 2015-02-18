from Bio import SeqIO, SearchIO, Entrez
import os

os.system('cls' if os.name == 'nt' else 'clear')

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
    records = Entrez.parse(search)
    print('dong')
    for record in records:
        taxon = record["GBSeq_taxonomy"].split("; ")
        print('the witch')
        name = record["GBSeq_source"]
        print('is dead')
        names.append(name)
        tax_length.append(len(taxon))
    print('.'),

print(names)
print(tax_length)
