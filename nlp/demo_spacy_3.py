#!pip install spacy
#!python -m spacy download es_core_news_md

import spacy
nlp = spacy.load("es_core_news_md")

text = """El presidente de Estados Unidos, Joe Biden, 
considera que hay que ir más allá en una reforma que establezca restricciones 
a las armas de fuego y prohibir los fusiles de asalto,
 tras el tiroteo del lunes en Illinois, con siete muertos y una treintena de heridos."""

doc = nlp(text)

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# pattern: NOUN-de-NOUN
pattern_1 = [{"POS": "NOUN"},{"LOWER": "de"}, {"POS": "NOUN"}]
matcher.add("NOUN-de-NOUN", [pattern_1])

# pattern: NOUN-ADJ
pattern_2 = [{"POS": "NOUN"}, {"POS": "ADJ"}]
matcher.add("NOUN-ADJ", [pattern_2])

matches = matcher(doc)

for match_id, start, end in matches:
    #string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]  # The matched span
    #print(match_id, string_id, start, end, span.text)
    print(span.text.lower())