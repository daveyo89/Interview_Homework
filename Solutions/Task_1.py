import nltk
import pickle
from nltk import sent_tokenize, word_tokenize

sentence = """ Jim likes Larry and Jean, but hates Kim.  
Bob loves Jean, and likes Larry and Kim.  
Jean loves Bob, likes Jim, but hates Kim.  
Kim hates Jim, likes Larry and Bob.  
Larry loves Martin, and hates Karl and Jean. """


def named_ent():
    try:
        for x in nltk.sent_tokenize(sentence):
            words = word_tokenize(x)
            tagged = nltk.pos_tag(words)

            name_ent = nltk.ne_chunk(tagged)
            name_ent.draw()

    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    named_ent()
