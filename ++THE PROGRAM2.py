from Bio import SeqIO
from Bio.Blast import NCBIWWW
import sys, threading, time

#Set Up Spinner
class ProgressBase(threading.Thread):
    #"Base class - not to be instanciated.#"

    def __init__(self):
        self.rlock = threading.RLock()
        self.cv = threading.Condition()
        threading.Thread.__init__(self)
        self.setDaemon(1)

    def __backStep(self):
        if self.inplace: sys.stdout.write('\b \b')

    def __call__(self):
        self.start()

    def start(self):
        self.stopFlag = 0
        threading.Thread.start(self)

    def stop(self):
        #"To be called by the 'main' thread: Method will block and wait for the thread to stop before returning control to 'main'.#"

        self.stopFlag = 1

        # Wake up 'Sleeping Beauty' ahead of time (if it needs to)...
        self.cv.acquire()
        self.cv.notify()
        self.cv.release()

        # Block and wait here untill thread fully exits its run method.
        self.rlock.acquire()
class Spinner(ProgressBase):
    #"Print 'animated' /|\ sequence to stdout in separate thread#"

    def __init__(self, speed=0.1):
        self.__seq = [chr(47), chr(45), chr(92), chr(124)]
        self.__speed = speed
        self.inplace = 1
        ProgressBase.__init__(self)

    def run(self):
        self.rlock.acquire()
        self.cv.acquire()
        sys.stdout.write(' ')
        while 1:
            for char in self.__seq:
                self.cv.wait(self.__speed)  # 'Sleeping Beauty' part
                if self.stopFlag:
                    self._ProgressBase__backStep()
                    try :
                        return                          ### >>>
                    finally :
                        # release lock immediatley after returning
                        self.rlock.release()
                if self.inplace: sys.stdout.write('\b')
                sys.stdout.write(char)

file_gbk = raw_input("genbank file? ")
# Parse genbank files
for seq_origin in SeqIO.parse(file_gbk, "genbank"):
        print seq_origin.id, ":", seq_origin.description
print

#Generating smaller sequences for BLAST
u = 0
length = len(seq_origin.seq)
s = length/10

for cycle in range(1, 11):
	t = cycle*s
	#Send Sequence to BLASTx
	indicator = Spinner(speed=0.1)
	indicator.start()
	print("Running BLAST %d , Please Wait." % cycle)
	result_handle = NCBIWWW.qblast("blastx", "nr", seq_origin.seq[u:t])
	save_file = open("origin_blast" + str(cycle) + ".xml","w")
	save_file.write(result_handle.read())
	save_file.close()
	result_handle.close()
	result_handle = open("origin_blast" + str(cycle) + ".xml")
	indicator.stop()
	print
	u = t


#print("Press Any Key to Exit...")
#raw_input()