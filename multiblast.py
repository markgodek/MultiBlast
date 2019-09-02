import os, glob, sys

input = sys.argv[1]

# /home/mark/PycharmProjects/MultiBlast/demoFASTAs

for filename in glob.glob(os.path.join(input, '*.fasta')):
    print(filename)

