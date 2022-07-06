#!pip install spacy
#!python -m spacy download es_core_news_md

import spacy
nlp = spacy.load("es_core_news_md")

text = """El presidente de Estados Unidos, Joe Biden, 
considera que hay que ir más allá en una reforma que establezca restricciones 
a las armas de fuego y prohibir los fusiles de asalto,
 tras el tiroteo del lunes en Illinois, con siete muertos y una treintena de heridos."""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)