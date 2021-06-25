from wordsegment import load, segment

class WordSegment:
    def __init__(self):
        load()

    def getWords(self, domain_list):
        domain_info = {}
        for domain in domain_list:
            domain_info[domain] = segment(domain)
        return domain_info
