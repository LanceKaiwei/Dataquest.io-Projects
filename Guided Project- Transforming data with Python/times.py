import read
import pandas as pd
from dateutil.parser import parse
stories = read.load_data()
time = stories["submission_time"]
hours = time.apply(lambda x: parse(x).hour)
counts = hours.value_counts()
print(counts)
#date = parse("2011-11-09T21:56:22Z")




'''time_null = pd.isnull(time)
true_time = time[time_null == False]
print(time.shape)
print(true_time.shape)'''
