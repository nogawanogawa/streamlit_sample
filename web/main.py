import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
from lib.es.document import Document
import nlplot

document = Document()

st.title('Japanese Text Analysis')

#### Input
search = st.sidebar.text_input("Search", "")

df = pd.DataFrame(document.search_all())
labels = df['category'].unique()
labels = np.insert(labels, 0, "")
category = st.sidebar.selectbox(
    'Category', labels)

#### Input -> Output

result = pd.DataFrame(document.search(search, category))

#### Output

'You selected:', category
if len(result) == 0 :
  pass
else:
  if len(result) > 100:
    result = result.iloc[:70,:]
  npt = nlplot.NLPlot(result, target_col='wakati')
  # Stopword calculations can be performed.
  stopwords = npt.get_stopword(top_n=30, min_freq=0)
  # 1. N-gram bar chart
  unigram = npt.bar_ngram(title='uni-gram', ngram=1, top_n=50, stopwords=stopwords)
  st.write(unigram)

  bigram = npt.bar_ngram(title='bi-gram', ngram=2, top_n=50, stopwords=stopwords)
  st.write(bigram)

  # 2. N-gram tree Map
  tree_map = npt.treemap(title='Tree of Most Common Words', ngram=1, top_n=30, stopwords=stopwords)
  st.write(tree_map)

  # 3. Histogram of the word count
  dist = npt.word_distribution(title='words distribution')
  st.write(dist)

  # plotlyじゃ無いものは、今回は除外

  # 4. wordcloud
  # npt.wordcloud(stopwords=stopwords, colormap='tab20_r')

  # 5. co-occurrence networks
  #npt.build_graph(stopwords=stopwords, min_edge_frequency=10)
  # The number of nodes and edges to which this output is plotted.
  # If this number is too large, plotting will take a long time, so adjust the [min_edge_frequency] well.
  #>> node_size:70, edge_size:166
  # st.write(npt.co_network(title='Co-occurrence network'))

  # 6. sunburst chart
  #npt.sunburst(title='sunburst chart')

  # 7. pyLDAvis
  # If you want to run it in a notebook environment, you need to use the import and magic commands
  #import pyLDAvis
  #pyLDAvis.enable_notebook()
  #npt.ldavis(num_topics=5, passes=5, save=False)

