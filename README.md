# MultiBlast

$ multiblastcli

  multiblastcli is a script that can read each FASTA
  file in a directory, single or multiple sequences from
  the files, and conduct an online BLAST search.
  The top 5 results from each query are returned.
  
  A demo directory is included as demoFASTAs.
  The output text file can be named, however the
  default is 'blastresult-date-time'.

Usage:

  $ pip install --editable .
  
  $ multiblastcli PATHto/demoFASTAs -o PATHto/my_results.txt
