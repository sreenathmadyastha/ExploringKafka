import nltk
from nltk.corpus import brown
print (brown.categories())

genres = ['fiction', 'humor', 'romance', 'sreenath']
whwords = ['What','what','which', 'how', 'why', 'when', 'where', 'who']

for i in range(0,len(genres)):
    genre = genres[i]
    print()
    print("Analysing '"+ genre + "' wh words")
    genre_text = brown.words(categories = genre)
    fdist = nltk.FreqDist(genre_text)
    print fdist
    for wh in whwords:
        print(wh + ':', fdist[wh])
        
