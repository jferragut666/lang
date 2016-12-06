from spacy.en import English
parser = English()
sentence = u'This is fun!'
parsedData = parser(sentence)
sents = []


for span in parsedData.sents:
    sent = [parsedData[i] for i in range(span.start, span.end)]
    break

for token in sent:
    print(token.orth_, token.pos_, token.dep_,token.head.orth_)


