from Bio import SeqIO, Entrez
from Bio.Blast import NCBIWWW, NCBIXML
from prettytable import PrettyTable as pt
import os

os.system('cls' if os.name == 'nt' else 'clear') #clear screen

file_gbk = raw_input("genbank file? ")
#Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
    print seq_origin.id, ":", seq_origin.description
print

def blast(sequence, run, addn):
    "Send Sequence to BLASTn"
    print("Running BLAST , Please Wait.")
    result_handle = NCBIWWW.qblast("blastn", "nr", sequence, entrez_query="all[filter] NOT((srcdb_refseq_model[prop] AND biomol_rna[prop])) %s" %addn)
    blast_file = open("blast%s.xml","w" %run)
    blast_file.write(result_handle.read())
    blast_file.close()
    result_handle.close()
    return;

def tax(run):
    result_handle = open("blast%s.xml" %run)
    blast_record = NCBIXML.read(result_handle)
    print("\aTaxonomy Search in Progress, Please Wait.")
    names = []
    taxons = []
    seqs = []
    for alignment in blast_record.alignments:
        hit = alignment.title.split("|")
        the_id = hit[1]
        # Entrez Search
        Entrez.email = "thomas.davies-7@student.manchester.ac.uk"
        search = Entrez.efetch(db="nuccore", id=the_id, rettype="gb", retmode="text")
        for record in SeqIO.parse(search, "genbank"):
            name = record.annotations['organism']
            names.append(name)
            taxon = record.annotations['taxonomy']
            taxons.append(len(taxon))
        search.close()
        #seqs.append(hsp.sbjct)
        print(".")
    return;

def dist_table():
    table = pt()
    table.add_column("Names", names)
    table.add_column("Taxon Length", taxons)
    table.add_column("HSP", seqs)
    table.align = "l"
    print(table)

#blast(sequence = seq_origin.seq, run = "01", addn = "")

#tax(1)

#dist_table()

#Run Mammalian BLAST
#blast(sequence = , run = "02", addn = "tx40674[orgn]")

print("Press Any Key to Exit...")
raw_input()
