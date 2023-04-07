import spacy
nlp = spacy.load("en_core_web_sm")
list_of_strings=
for string in list_of_strings:
    doc = nlp(string)
    for entity in doc.ents:
        if entity.label_ == "ORG":
            print(entity.text)