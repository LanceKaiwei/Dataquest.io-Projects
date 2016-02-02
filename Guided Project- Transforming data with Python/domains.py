import read
import pandas as pd
stories = read.load_data()
url = stories["url"]
url_null = pd.isnull(url)
true_url = url[url_null == False]
domains_url = true_url.apply(lambda s: '.'.join(s.split(".")[-2:]))
counts = domains_url.value_counts()
print(counts[:100])

#following gives the same output but the codes are longer and uglier
'''import read
import pandas as pd
from collections import Counter
stories = read.load_data()
url = stories["url"]
l=[]
for u in url:
    l.append(u)
l2 = []
for s in l:
    if type(s) == float:
        l2.append(str(s))
    else:
        l2.append(s)
def remove_subdomains(s):
    s = '.'.join(s.split(".")[-2:])
    return s
l3 = []
for s in l2:
    l3.append(remove_subdomains(s))
s3 = pd.Series(l3)
updated_s3 = s3[s3!="nan"]
counts = updated_s3.value_counts()
print(counts[:5])'''
#counts = Counter(l3)
#print(counts.most_common(5))
#url_domains_only = url2.apply(lambda s: remove_subdomains(s))