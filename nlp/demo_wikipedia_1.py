#pip install wikipedia
import wikipedia
wikipedia.set_lang("es")

print(wikipedia.summary("Joe Biden", sentences=3))