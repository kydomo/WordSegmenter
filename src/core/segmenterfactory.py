from src.core.segementers.wordsegment.wordsegment import WordSegment

segmenter = "WS"

class SegmenterFactory:

    __instance = None
    
    @staticmethod
    def getInstance():
        # Static Access Method
        if SegmenterFactory.__instance == None:
            SegmenterFactory()
    def __init__(self):
        if SegmenterFactory.__instance != None:
            raise Exception("Segmenter Factory is a singleton class")
        else:
            SegmenterFactory.__instance = self 


    # This will return the appropriate Algo
    def getSegmenter(self):
        global segmenter
        if segmenter == "WS":
            return WordSegment()
        else:
            print ("{segementer} not supported".format(segmenter=segmenter))
            raise ValueError(algo)