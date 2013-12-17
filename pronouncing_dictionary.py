import nltk

entries = nltk.corpus.cmudict.entries()
print len(entries)

for entry in entries[39943:39951]:
    print entry
