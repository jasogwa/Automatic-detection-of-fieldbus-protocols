import Levenshtein
from query.query import *  

test = "BCE0362E094C000080"
#test = "BCE0FFFFFFFFFFFFFF"
db = QUERY()

#score two sequences
def get_score(seq1, seq2):
    score = Levenshtein.ratio(seq1.replace('-',''),seq2.replace('-','')) * 100
    return score

rows = db.select()

result = []

for row in rows:
    seqA = row[2]
    score = get_score(seqA,test)    
    if score >= 60:
        print("{} {}{}\n".format(row[1],"Score: ",score))
    else:
        result.append("No sequence found")

if(len(result) != 0):
    print(result[0])
else:
    print("")