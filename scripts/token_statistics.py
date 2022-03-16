from collections import Counter
import pandas as pd

f = open('root/001.tok', 'r')
tokens = f.read()
tokens = tokens.replace('_', ' ').replace('།', '').rstrip().split(' ')
counter = Counter(tokens).most_common()
df = pd.DataFrame(counter)
df = df.iloc[1:]
df[2] = df[1] / df[1].sum() * 100
df.columns = ['word_segment', 'instances', 'prominence']

df.to_csv('stats/word_segment_statistics.csv', index=None)