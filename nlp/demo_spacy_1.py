#!pip install spacy
#!python -m spacy download es_core_news_md

import spacy

print(spacy.__version__)
nlp = spacy.load("es_core_news_md")

text = """El presidente de Estados Unidos, Joe Biden, 
considera que hay que ir más allá en una reforma que establezca restricciones 
a las armas de fuego y prohibir los fusiles de asalto,
 tras el tiroteo del lunes en Illinois, con siete muertos y una treintena de heridos."""

doc = nlp(text)

for token in doc:
    print(token.text,token.pos_)
    
    #token.lemma_,token.is_stop,token.pos_