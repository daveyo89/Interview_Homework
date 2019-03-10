import re
from IPython.display import display
import pandas as pd

text = """ Jim likes Larry and Jean, but hates Kim.  
Bob loves Jean, and likes Larry and Kim.  
Jean loves Bob, likes Jim, but hates Kim.  
Kim hates Jim, likes Larry and Bob.  
Larry loves Martin, and hates Karl and Jean """

text = text.splitlines()
all_names = []
relations = {}


def get_names_from_sentence(sentence):
    names_in_sentence = []
    sentence = sentence.split()
    for word in sentence:
        word = re.sub('[(){}<>.,?!]', '', word)
        if word.istitle():
            names_in_sentence.append(word)
            if word not in all_names:
                all_names.append(word)


def weighing_relations(sentence):
    key = sentence[0]
    relation_value = 0
    relations[key] = [key]

    for i in range(len(sentence) - 1):
        curr_word = sentence[i + 1]
        curr_name = ''
        if curr_word.istitle():
            curr_name = curr_word
        if curr_word == 'likes':
            relation_value = 3
        if curr_word == 'loves':
            relation_value = 5
        if curr_word == 'hates':
            relation_value = 1

        # print(curr_word + ' ' + str(relation_value)+ " current name is : " + curr_name )

        if len(curr_name) > 0:
            relations[key].append(curr_name)
            relations[key].append(relation_value)


if __name__ == '__main__':
    # Filling up all names array.
    for i in range(len(text)):
        get_names_from_sentence(text[i])

    # Clearing sentences from unnecessary words.
    for i in range(len(text)):
        clear_sentence = text[i].replace('and', '').replace('but', '').replace(',', '').replace('.', '')
        clear_sentence = re.sub(' +', ' ', clear_sentence).split()
        weighing_relations(clear_sentence)

    df = pd.DataFrame(relations).T.fillna(0)
    df = df.drop(0, axis=1)
    df.columns = ['1.', '1#', '2.', '2#', '3.', '3#']
    display(df)
