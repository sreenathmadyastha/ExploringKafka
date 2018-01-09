import nltk
from nltk.corpus import CategorizedPlaintextCorpusReader

reader = CategorizedPlaintextCorpusReader(r'/home/smadyastha/Projects/PythonCheck/Dataset/Reviews/tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')


posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

from random import randint
fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0, len(posFiles) - 1)]
print(fileP)
print(fileN)

for w in reader.words(fileP):
    print(w + "")
    if (w is '.'):
        print()



# /home/smadyastha/Projects/PythonCheck/Dataset/Reviews