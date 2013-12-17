import nltk

entries = nltk.corpus.cmudict.entries()
print len(entries)

# for word, pron in entries:
#     if len(pron) == 3:
#         ph1, ph2, ph3 = pron
#         if ph1 == 'P' and ph3 == 'T':
#             print word, ph2,

syllable = ['N', 'IH0', 'K', 'S']

print [word for word, pron in entries if pron[-4:] == syllable]
