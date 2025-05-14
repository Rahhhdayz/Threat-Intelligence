import spacy
from functools import lru_cache

# Load spaCy model only once, even if called multiple times
@lru_cache(maxsize=1)
def get_nlp():
    return spacy.load("en_core_web_sm")

def extract_entities(text, labels=None):
    """
    Extract named entities from text.

    Args:
        text (str): The input text to extract entities from.
        labels (list, optional): A list of entity labels to include. Defaults to ORG, PERSON, NORP, PRODUCT.

    Returns:
        List[str]: A list of unique entity strings.
    """
    if labels is None:
        labels = ["ORG", "PERSON", "NORP", "PRODUCT"]

    doc = get_nlp()(text)
    entities = {ent.text.strip() for ent in doc.ents if ent.label_ in labels}
    return list(entities)