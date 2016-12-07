#!/usr/bin/python3.5

from Bio import Entrez
from Bio import Medline

MAX_COUNT = 2
TERM = 'Your name' # replace your name here

Entrez.email = 'your@email.com' # Please replace your email address here
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(h)
print('Total number of publications containing {0}: {1}\n'.format(TERM, result['Count']))

ids = result['IdList']
handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
records = Medline.parse(handle)

for record in records:
    print("title:", record.get("TI", "?"))
    print("authors:", record.get("AU", "?"))
    print("source:", record.get("SO", "?"))
    print()
