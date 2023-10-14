import re
import xml.etree.ElementTree as ET
import os

# Define path to the WordNet XML file
WORDNET_XML_PATH = os.path.join(os.path.dirname(__file__), '../data/english-wordnet.xml')

def sanitize_word(word):
    """
    Sanitize the word to remove any characters that might conflict with XPath syntax.
    """
    # Remove any non-alphanumeric characters
    return re.sub(r'[^\w\s]', '', word)

def load_wordnet_xml():
    """
    Load the WordNet XML into memory.
    """
    tree = ET.parse(WORDNET_XML_PATH)
    return tree.getroot()

wordnet_root = load_wordnet_xml()

def get_definitions(word):
    """
    Fetch definitions of the given word from WordNet.
    """
    word = sanitize_word(word)
    definitions = []
    for lexentry in wordnet_root.findall(".//LexicalEntry/Lemma[@writtenForm='{}']..".format(word)):
        for sense in lexentry.findall('.//Sense'):
            for definition in sense.findall('.//Definition'):
                definitions.append(definition.text)
    return definitions

def get_synonyms(word):
    """
    Fetch synonyms of the given word from WordNet.
    """
    word = sanitize_word(word)
    synonyms = []
    for lexentry in wordnet_root.findall(".//LexicalEntry/Lemma[@writtenForm='{}']..".format(word)):
        for sense in lexentry.findall('.//Sense'):
            for synonym in sense.findall('.//Synset'):
                for lemma in synonym.findall('.//Lemma'):
                    synonym_word = lemma.get('writtenForm')
                    if synonym_word != word:
                        synonyms.append(synonym_word)
    return list(set(synonyms))

def get_hypernyms(word):
    """
    Fetch hypernyms of the given word from WordNet.
    """
    word = sanitize_word(word)
    hypernyms = []
    for lexentry in wordnet_root.findall(".//LexicalEntry[Lemma/@writtenForm='{}']".format(word)):
        for sense in lexentry.findall('.//Sense'):
            for relation in sense.findall('.//Relation[@type="hypernym"]'):
                hypernym_id = relation.get('target')
                hypernym_entry = wordnet_root.find(".//LexicalEntry[@id='{}']".format(hypernym_id))
                if hypernym_entry:
                    for lemma in hypernym_entry.findall('.//Lemma'):
                        hypernyms.append(lemma.get('writtenForm'))
    return list(set(hypernyms))
