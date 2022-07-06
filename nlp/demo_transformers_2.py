#pip install transformers
# o pip install transformers[torch]

from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline

text="""Joseph Robinette Biden Jr. (Scranton, Pensilvania, 20 de noviembre de 1942), ( /dʒoʊ ˈbaɪdən/) 
es un político estadounidense que es el 46.º y actual presidente de los Estados Unidos."""

ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)

q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)

result = q_a_es(question="¿Cuál es su profesión?", context=text)
print(result["answer"])

result = q_a_es(question="¿Cuál es su nacionalidad?", context=text)
print(result["answer"])
