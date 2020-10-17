import re


class Document:
    """
    This class represents a Document, which represents a file in a
    SearchEngine
    """
    def __init__(self, path):
        """
        Initializer for Document class: takes in path name of target document
        """
        self._path = path
        self._frequencies = self._build_dict(path)

    def _build_dict(self, path):
        """
        Helper function that builds up the dictionary of
        words -> word frequency
        """
        frequencies = dict()
        total = 0  # Records total words in document

        # Builds dictionary as word -> word count
        with open(path) as file:
            lines = file.readlines()

            for line in lines:
                for word in line.split():
                    word = re.sub(r'\W+', '', word).lower()  # Strips word
                    total += 1
                    if word not in frequencies:
                        frequencies[word] = 1
                    else:
                        frequencies[word] = frequencies[word] + 1

        # Modifies dictionary to record word -> word frequency
        for key in frequencies:
            frequencies[key] = frequencies[key] / total

        return frequencies

    def get_path(self):
        """
        Returns the path of this Document
        """
        return self._path

    def term_frequency(self, term):
        """
        Returns the term frequency of a given term for this Document
        """
        return self._frequencies[re.sub(r'\W+', '', term).lower()]

    def get_words(self):
        """
        Returns a list of every unique word in this Document
        """
        return list(self._frequencies.keys())