import os, glob, sys
from Bio import SearchIO
from Bio.Blast import NCBIWWW

input = sys.argv[1]
output = sys.argv[2]

# /home/mark/PycharmProjects/MultiBlast/demoFASTAs

with open(output, 'a+') as output_handle:
    for filename in glob.glob(os.path.join(input, '*.fasta')):
        print(filename)
        with open(filename, 'rU') as fasta_handle:
            with open(filename, 'rU') as fasta_handle:
                result_handle = NCBIWWW.qblast('blastn', 'nt',
                                               fasta_handle.read(), hitlist_size=5)
                blast_results = SearchIO.parse(result_handle, 'blast-xml')
                for result in blast_results:
                    for hsp in result.hsps:
                        output_handle.write(str(hsp) + '\n\n')
        fasta_handle.close()
print('Done')