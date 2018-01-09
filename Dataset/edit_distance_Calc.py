from nltk.metrics.distance import edit_distance
def my_edit_distance(str1, str2):
 m=len(str1)+1
 n=len(str2)+1
 table = {}
 for i in range(m): 
     table[i,0]=i
 for j in range(n): 
    table[0,j]=j
    
