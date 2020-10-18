import math
import os
import re
from document import Document


class SearchEngine:
    """
    This class manages Documents and computes the relevance of a Document to
    a given term
    """
    def __init__(self, dir_name):
        """
        Initializer for SearchEngine class: takes in path name of a directory
        """
        # Number of total documents in SearchEngine
        self._total_docs = len(os.listdir(dir_name))
        self._ii = self._build_dict(dir_name)  # inverse index == ii

    def _build_dict(self, dir_name):
        """
        Helper function that builds up the inverse index
        """
        index = dict()
        # Builds dictionary as word -> Document object
        for file_name in os.listdir(dir_name):
            doc = Document(dir_name + '/' + file_name)
            for word in doc.get_words():
                if word not in index:
                    index[word] = list()
                index[word].append(doc)
        return index

    def _calculate_idf(self, term):
        """
        Helper function that calculates the IDF for a given term
        """
        term = re.sub(r'\W+', '', term).lower()
        if term not in self._ii:
            return 0
        else:
            return math.log((self._total_docs) / (len(self._ii[term])))

    def search(self, term):
        """
        Given a term, returns a list of document names ranked by relevancy
        of that term
        """
        words = [re.sub(r'\W+', '', word).lower() for word in term.split()]
        # Dictionary maps document name -> total tfidf
        docs = dict()
        for word in words:

            # Checks that word is in the inverse index
            if word in self._ii:
                for doc in self._ii[word]:
                    doc_name = doc.get_path()
                    if doc in docs:
                        docs[doc_name] = (docs[doc_name] +
                                          self._calculate_tfidf(word, doc))
                    else:
                        docs[doc_name] = self._calculate_tfidf(word, doc)

        # Convert dictionary to list of tuples
        docs = list(docs.items())
        # Sort list of tuples by decreasing tfidf
        docs = sorted(docs, key=lambda t: t[1], reverse=True)
        # Returns only the names in each tuple
        return [tup[0] for tup in docs] if len(docs) != 0 else None

    def _calculate_tfidf(self, term, doc):
        """
        Helper function that calculates the tfidf for a single term and single
        document
        """
        return doc.term_frequency(term) * self._calculate_idf(term)