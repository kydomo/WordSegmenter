from wordsegment import load, segment

class WordSegment:
    def __init__(self):
        load()

    def getWords(self, domain_list):
        return segment(domain_list)
