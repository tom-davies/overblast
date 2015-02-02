from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta","fasta"):
        if seq_record.id=="gi|2765658|emb|Z78533.1|CIZ78533":
                print(seq_record.id)
                print(seq_record.seq)
                print(len(seq_record))
                print
for seq_genbank in SeqIO.parse("ls_orchid.gbk", "genbank"):
        if seq_genbank.id=="Z78533.1":
                print(seq_genbank.id)
                print(seq_genbank.seq)
                print(len(seq_genbank))

