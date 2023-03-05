import io, os
import spacy
from nltk.tokenize import TreebankWordTokenizer as twt
import nltk
from spacy import displacy

nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset') 

nlp = spacy.load("en_core_web_sm")

pos_tags = ["PRON", "VERB", "NOUN", "ADJ", "ADP", "ADV", "CONJ", "DET", "NUM", "PRT"]
colors = {"PRON": "blueviolet",
          "VERB": "lightpink",
          "NOUN": "turquoise",
          "ADJ" : "lime",
          "ADP" : "khaki",
          "ADV" : "orange",
          "CONJ" : "cornflowerblue",
          "DET" : "forestgreen",
          "NUM" : "salmon",
          "PRT" : "yellow"}

class SpacyDocument:

    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tokens(self):
        return [token.lemma_ for token in self.doc]

    def get_entities(self):
        entities = []
        for e in self.doc.ents:
            entities.append((e.start_char, e.end_char, e.label_, e.text))
        return entities

    def get_doc(self):
        return self.doc

    def get_entities_with_markup(self):
        entities = self.doc.ents
        starts = {e.start_char: e.label_ for e in entities}
        ends = {e.end_char: True for e in entities}
        buffer = io.StringIO()
        for p, char in enumerate(self.text):
            if p in ends:
                buffer.write('</entity>')
            if p in starts:
                buffer.write('<entity class="%s">' % starts[p])
            buffer.write(char)
        markup = buffer.getvalue()
        return '<markup>%s</markup>' % markup

    def get_pos_tree(self):
        tokens = twt().tokenize(self.text)
        tags = nltk.pos_tag(tokens, tagset = "universal")
        span_generator = twt().span_tokenize(self.text)
        spans = [span for span in span_generator]
        toks = []
        for tag, span in zip(tags, spans):
            if tag[1] in pos_tags:
                toks.append({"start" : span[0], 
                            "end" : span[1], 
                            "label" : tag[1] })
        doc = {"text" : self.text, "ents" : toks}
        options = {"ents" : pos_tags, "colors" : colors}
        return displacy.render(doc, style = "ent", options = options, manual = True)

    def get_dep_img(self):
        svg = displacy.render(self.doc, style='dep', jupyter=False)
        return svg
        