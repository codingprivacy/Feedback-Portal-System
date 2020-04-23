import data_calculation
import itertools
from wordcloud import WordCloud, STOPWORDS
import matplotlib
import pandas as pd
matplotlib.use('Agg')

def generate_graph():
    df=data_calculation.save_data()
    comment_words = ' '
    stopwords = set(STOPWORDS)
    single_list=list(itertools.chain.from_iterable(df))
    #print()
    print(single_list)

    for val in single_list:
        val = str(val)
        tokens = val.split()

        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
          comment_words = comment_words + words + ' '
          #print(comment_words)


    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)


    matplotlib.pyplot.figure(figsize = (6, 6), facecolor = None,frameon=False)
    matplotlib.pyplot.imshow(wordcloud)
    matplotlib.pyplot.axis("off")
    matplotlib.pyplot.tight_layout(pad = 0)
    matplotlib.pyplot.savefig('/var/www/FPSU/FPSU/static/images/wordcloud.png')
    