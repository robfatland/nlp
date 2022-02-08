from collections import Counter
from collections import defaultdict
import glob, os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from gensim import corpora, models

'''
Chunk all the Shakespeare plays into 5000 word chunks. (text processing lib)
Each chunk should be labeled in the format play_chunkno (i.e. 'merchant_of_venice_006' etc).

Topic model the chunks using 5, 10, 25, 50 topics. (gensim)

Taking each topic distribution as your set of vectors, cluster the chunks using K-Means clustering where K=3. 
Draw the results of each clustering as a color-coded scatterplot.
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

'''
    Input: list of words, chunk size
    Output: list of chunks
'''
def chunk(text, chunk_size=1000):
    chunks = []
    for start in range(0, len(text)-chunk_size+1, chunk_size):
        chunks.append(text[start:start+chunk_size])
    return chunks


#### PROCESSING ####
# 1. Get files from folder
filepath = './shakespeare/*.txt'
files = glob.glob(filepath)
# labels = [os.path.split(f)[1][:-4].replace('_', ' ').title() for f in files]

# 2. chunk all shakespeare and make labels
def make_topic_model(chunks, num):
    dictionary = corpora.Dictionary(chunks) 
    corpus = [dictionary.doc2bow(text) for text in chunks]
    # lda model
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=num)
    corpus_lda = lda[corpus]
    return corpus_lda

'''Kmeans the topics, k = 3'''
def kmean_topics(topics, labels, chunks, num):
    # Put labels, features, vectors into a single dataframe
    vectors_df = pd.DataFrame(topics, index=labels, columns=range(num)).fillna(0)
    # 4. Use K-means clustering from Scikit Learn to find two clusters. 
    n_clusters=3
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(vectors_df)
    plot_clusters(kmeans, vextors_df, num) # plot topic clustering
    return 

'''Plot clustering for each topic'''
def plot_clusters(kmeans, df, topic_num):
    pca = PCA(n_components=2)
    transformed = pca.fit_transform(df) # transform topic_num features to 2D
    x = transformed[:,0]
    y = transformed[:,1]
    col_dict = {0:'red', 1:'blue', 2:'green'}
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
    plt.title('Shakespeare works for Topic {}'.format(topic_num))
    plt.show()
	plt.savefig("shakespeare-kmeans-{}.png".format(topic_num))
    return

for f in files:
    chunks = chunk(preprocess(open(f, "r").read()), 5000) # get chunks 
    chunk_labels = ['{}_{:03}'.format(os.path.split(f)[1][:-4], i) for i, j in enumerate(chunks)] # get chunk labels
    # starting topic modeling for chunks using 5, 10, 25, 50 topics
    topic_5 = make_topic_model(chunks, 5)
    kmean_topics(topic_5, chunk_labels, chunks, 5) # plot n=5
    topic_10 = make_topic_model(chunks, 10)
    kmean_topics(topic_5, chunk_labels, chunks, 10) # plot n=10
    topic_25 = make_topic_model(chunks, 25)
    kmean_topics(topic_5, chunk_labels, chunks, 25) # plot n=25
    topic_50 = make_topic_model(chunks, 50)
    kmean_topics(topic_5, chunk_labels, chunks, 50) # plot n =50
