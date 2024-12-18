import spacy

class NLPModel:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_md')  # Load a medium-sized English model

    def extract_compliance_requirements(self, text):
        # Placeholder implementation
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents]  # Extract named entities as a simple example
