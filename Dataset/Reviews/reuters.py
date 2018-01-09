from nltk.corpus import reuters
files = reuters.fileids()
words16 = reuters.words(['test/16097'])[:20]

requestGenres = reuters.categories()
print (words16)

print(requestGenres)

for w in reuters.words(categories=['bop','cocoa']):
  print(w+' ',end='')
  if (w is '.'):
      print()