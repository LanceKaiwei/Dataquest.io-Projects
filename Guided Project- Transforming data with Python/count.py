import read
from collections import Counter
stories = read.load_data()
l = []
headline = stories["headline"]
for head in headline:
    l.append(head)
l2 = []
for s in l:
    if type(s) == float:
        l2.append(str(s))
    else:
        l2.append(s)
s = ' '.join(l2)
slist = s.split(" ")
slist_lower = []
for s in slist:
    slist_lower.append(s.lower())
counts = Counter(slist_lower)
print(counts.most_common(100))
