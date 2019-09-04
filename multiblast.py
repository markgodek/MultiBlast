import os, glob, click
from Bio import SearchIO
from Bio.Blast import NCBIWWW
from datetime import datetime

filename = 'blastresult-' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S')  # default output filename

@click.command()
@click.argument('input', type=click.Path(exists=False, readable=True))
@click.option('-o', '--output', type=click.File('a+'), default=filename,
              required=False, help='The output file in txt format')

def cli(input, output):
    """Simple program that BLAST searches all FASTA files in a directory
    and writes the top 5 hits for each query to a text file."""

    # open each file and print the filename to the terminal
    for filename in glob.glob(os.path.join(input, '*.fasta')):
        print(filename)
        with open(filename, 'rU') as fasta_handle:
            result_handle = NCBIWWW.qblast('blastn', 'nt',
                                           fasta_handle.read(), hitlist_size=5)  # do the actual blast search
            blast_results = SearchIO.parse(result_handle, 'blast-xml')  # parse the results without storing them
            for result in blast_results:
                i = 1
                for hsp in result.hsps:
                    output.write('Result #' + str(i) + '\n')
                    output.write(str(hsp) + '\n\n')
                    i += 1
        fasta_handle.close()
    print('Done')
