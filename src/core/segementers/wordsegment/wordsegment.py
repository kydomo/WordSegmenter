from wordsegment import load, segment

class WordSegment:
    def __init__(self):
        doamin_info = {}
        load()

    def getWords(self, domain_list):
        for domain in domain_list:
            self.domain_info[domain] = segment(domain)
        return self.domain_info
