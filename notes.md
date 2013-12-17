corpus - structure collection of text. NLTK has many corpora.

word sense disambiguation - which sense of a word was intended in a given context

collocation - sequence of words that occur together unusually often (e.g. *red wine*)

hapaxe - word that occurs only once in a given text

frequency distribution - the frequency of each vocabulary item within a text

condition frequency distribution - collection of frequency distributions, each one for a different *condition*. The condition will often be the category of the text.

anaphora resoltion - identifying what a pronoun or noun phrase refers to

semantic role labeling - identifying how a noun phrase relates to the verb (agent, patient, instrument, etc.)

bigram - word pair

lexical entry - consists of a *headword* (also known as a *lemma*), as well as additional information such as the part-of-speech and the sense definition

stopwords - high frequency words (the, to, also) with little lexical content. Their presence fails to distinguish the text from other texts.

phones - contain digits to represent primary stress (1), secondary stress (2), no stress (0)

comparative wordlist - Swadesh wordlists, lists of about 200 common words in several languages

phonemes - contrastive sounds

synset - synonyms set, collection of synonymous words (or "lemmas")

hypernym/hyponym relation (*lexical relations*) - i.e. the superordinate and subordinate relationships. (e.g. motocar.hyponyms() # => ["Model T", "SUV", "Ambulance" ....], motorcar.hypernms() #=> "motor_vehicle")

meronyms - components of items (tree meronyms: trunk, crown, etc.)

holonyms - things items are contained in (forest), member_holonyms()

entailments - has to do with verbs. walking *entails* stepping, eating *entails* chewing



