import re
from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

text = """ Jim likes Larry and Jean, but hates Kim.  
Bob loves Jean, and likes Larry and Kim.  
Jean loves Bob, likes Jim, but hates Kim.  
Kim hates Jim, likes Larry and Bob.  
Larry loves Martin, and hates Karl and Jean """

text = text.splitlines()
all_names = []


def get_names_from_sentence(sentence):
    names_in_sentence = []
    sentence = sentence.split()
    for word in sentence:
        word = re.sub('[(){}<>.,?!]', '', word)
        if word.istitle():
            names_in_sentence.append(word)
            if word not in all_names:
                all_names.append(word)


def weighing_relations(sentence, df):
    key = sentence[0]
    curr_name = ''
    curr_rel = ''

    for i in range(len(sentence) - 1):
        curr_word = sentence[i + 1]

        if curr_word.istitle():
            curr_name = curr_word
        else:
            curr_rel = curr_word
            continue

        if len(curr_name) > 0 and len(curr_rel) > 0:
            rel_value = 0
            if curr_rel == 'likes':
                rel_value = 5
            if curr_rel == 'loves':
                rel_value = 10
            if curr_rel == 'hates':
                rel_value = -7
            # df.ix[key, curr_name] = curr_rel
            df.ix[key, curr_name] = rel_value


if __name__ == '__main__':
    # Filling up all names array.
    for i in range(len(text)):
        get_names_from_sentence(text[i])

    size = len(all_names)
    df = pd.DataFrame(0, columns=all_names, index=all_names)

    # Clearing sentences from unnecessary words.
    for i in range(len(text)):
        clear_sentence = text[i].replace('and', '').replace('but', '').replace(',', '').replace('.', '')
        clear_sentence = re.sub(' +', ' ', clear_sentence).split()
        weighing_relations(clear_sentence, df)

    # df = df.cumsum()
    df[all_names][all_names].plot()

    #Show averages.
    df.mean().plot(kind='bar')
    plt.show()

    # Display has to be read by rows.
    display(df)
