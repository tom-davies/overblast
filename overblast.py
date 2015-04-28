from Bio import SeqIO, Entrez, Phylo, AlignIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Align.Applications import MuscleCommandline
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from prettytable import PrettyTable as pt
import os
import pdb

os.system('cls' if os.name == 'nt' else 'clear') #clear screen

file_gbk = raw_input("Genbank Filename? ")
cycles = input("How many cycles before mammalian search? ")
#Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
    print seq_origin.id, ":", seq_origin.description

def blast(sequence, run, addn):
    #Send Sequence to BLASTn
    print
    print
    print("Running BLAST cycle #%s , Please Wait." % run)
    result_handle = NCBIWWW.qblast("blastn", "nr", sequence, entrez_query="all[filter] 500:20000[slen] NOT((srcdb_refseq_model[prop] AND biomol_rna[prop]) OR environmental_samples[organism] OR metagenomes[orgn]) %s" % addn, megablast=True)
    blast_file = open("blast%s.xml" % run,"w")
    blast_file.write(result_handle.read())
    blast_file.close()
    result_handle.close()
    return;

def phylo(run):
    #Draw phylogenic tree from BLAST
    result_handle = open("blast%s.xml" % run)
    blast_record = NCBIXML.read(result_handle)
    print("\tCollecting Sequences")		#Extract sequences from BLAST result
    def get_seqs(source):
            for aln in source:
                for hsp in aln.hsps:
                    yield SeqRecord(Seq(hsp.sbjct), id=aln.accession)
                    break
    seqs = get_seqs(blast_record.alignments,)
    SeqIO.write(seqs, 'Phylo/family.fasta', 'fasta')
    print("\tAligning Sequences")
    cmdline = MuscleCommandline(input="Phylo/family.fasta", out="Phylo/family.aln", clw=True)
    cmdline()
    AlignIO.convert("Phylo/family.aln", "clustal", "Phylo/family.phy", "phylip-relaxed")
    print("\tGenerating Tree...")
    cmdline = PhymlCommandline(input="Phylo/family.phy")
    out_log, err_log = cmdline()
    print("\tDrawing Tree")
    tree = Phylo.read("Phylo/family.phy_phyml_tree.txt", "newick")
    Phylo.draw_ascii(tree)
    return;

f = open("hits.txt","a")	#Make a place to store sequence IDs
used_ids = []				#Setup for duplicate checking
point = 0

#Run first Cycle
blast(sequence = seq_origin.id, run = "01", addn = "")
phylo(run = "01")
tree_out = open("Phylo/family.phy_phyml_tree.txt")
tree_out.seek(1)
new_id = tree_out.read().replace(",",":").split(":")
true_id = new_id[point].replace("(","")
#Duplicate Checking
for ids in used_ids:
    if true_id == ids:
        point += 2
        true_id = new_id[point].replace("(","")
        print(true_id)	#If the ID is a dupe, add 2 to the index to find the next one
        used_ids.append(true_id)
    else:
        print(true_id)	#If the ID isn't duped, use it, and add it to the used_ids list
        used_ids.append(true_id)
        break;
f.write(true_id)
f.close()

#Run all other cycles
for x in xrange(2, cycles):
    blast(sequence = true_id, run = "%02d" % x, addn= "")
    phylo(run = "%02d" % x)
    tree_out = open("Phylo/family.phy_phyml_tree.txt")
    tree_out.seek(1)
    new_id = tree_out.read().replace(",",":").split(":")
    point = 0
    true_id = new_id[point].replace("(","")
	#Duplicate Checking
    for ids in used_ids:
        if true_id == ids:
            point += 2		#If the ID is a dupe, add 2 to the index to find the next one
            true_id = new_id[point].replace("(","")
            print(true_id)
            used_ids.append(true_id)
        else:
            print(true_id)	#If the ID isn't duped, use it, and add it to the used_ids list
            used_ids.append(true_id)
            break;
    f = open("hits.txt","a")
    f.write("\n")
    f.write(true_id)
    f.close()
    print(used_ids)

#Run Mammalian BLAST
blast(sequence = true_id, run = "LAST", addn = "tx40674[orgn]")
phylo(run = "LAST")
tree = Phylo.read("Phylo/family.phy_phyml_tree.txt", "newick")
Phylo.draw_ascii(tree)

f.close()

print("Press Any Key to Exit...")
raw_input()
