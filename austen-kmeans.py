from collections import Counter
from collections import defaultdict
import glob, os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 



'''
The 'austen_alcott' folder contains a set of novels by Jane Austen and Louisa May Alcott. 

Read these files and create a vector table with the top 50 most frequent words in the 
corpus as your feature-set. So each text will be represented as a set of relative frequencies 
over these words. Use K-means clustering from Scikit Learn to find two clusters. Plot with labels 
and color the dots in the two clusters differently 
'''

##### TEXT PROCESSING LIB ####
def tokenize(s):
    """
    Input: 
        string s
    Output: 
        list of strings
    """
    return s.split()

def preprocess(s, lowercase=True, strip_punctuation=True):
    """
    Input:
        string s
        boolean lowercase
        boolean strip_punctuation
    Return:
        list of strings
    """
    punctuation = '.,?<>:;"\'!%'
    if isinstance(s, str):
        s = tokenize(s)
    if lowercase:
        s = [t.lower() for t in s]
    if strip_punctuation:
        s = [t.strip(punctuation) for t in s]
        
    return s

def token_frequency(tokens=None, tf={}, relative=False):
    """
    Input:
        tokens = list of strings or None
        tf = dict or None
        relative = boolean
    Return:
        dictionary of token frequencies
    """
    for t in tokens:
        if t in tf:
            tf[t]+=1
        else:
            tf[t]=1
    if relative:
        total = sum([c for t, c in tf.items()])
        tf = {t:tf[t]/total for t in tf}
    return tf

#### PROCESSING ####
# 1. Get files from folder
filepath = './austen_alcott/*.txt'
files = glob.glob(filepath)
labels = [os.path.split(f)[1][:-4].replace('_', ' ').title() for f in files]

# 2. Get 50 most freq words in corpus for feature set (wk5 assignment)
word_freq = dict()
for f in files:
    file = open(f, "r")
    word_list = preprocess(file.read()) # process list of words from file
    word_freq = token_frequency(word_list, tf=word_freq) # get freq for new list of words

    # sort dict in decreasing order by frequencies (v) and print first 50 tokens
features = [word for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)][0:50]

# 3. Vectorize over feature set
vectors = []
for file_name in files:
    text = preprocess(open(file_name, 'r').read())
    freqs = token_frequency(text, relative=True)
    vectors.append({k:freqs[k] for k in freqs if k in features})

    # Put labels, features, vectors into a single dataframe
vectors_df = pd.DataFrame(vectors, index=labels, columns=features).fillna(0)

# 4. Use K-means clustering from Scikit Learn to find two clusters. 
n_clusters=2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(vectors_df)

# 5. Plot with labels and color the dots in the two clusters differently (from text processing lib)
pca = PCA(n_components=2)
transformed = pca.fit_transform(vectors_df)
x = transformed[:,0]
y = transformed[:,1]
col_dict = {0:'green', 1:'blue'}
cols = [col_dict[l] for l in kmeans.labels_]
plt.figure(figsize=(15,10))
plt.scatter(x,y, c=cols, s=100, alpha=.5)
for i, l in enumerate(labels):
    plt.text(x[i]+.0003,y[i]-.0001, l)
for i, c in enumerate(pca.components_.transpose()):
    plt.arrow(0,0, c[0]/50, c[1]/50, alpha=.3, width=.0001)
    plt.text(c[0]/50, c[1]/50, features[i])
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('Austen works in space of 50 most freq words')
plt.show()

plt.savefig("kmeans-clustering.png")
