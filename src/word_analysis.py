import nltk 

nltk.download("stopwords")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class Review():
    def __init__(self, review_text, rating, region, date ):
        self.review_text = review_text
        self.rating = rating
        self.region = region
        self.date = date

    def __repr__(self):
        text = "Review text: " + self.review_text + "\nRating: " \
            + str(self.rating) + "\nRegion: "+ str(self.region) + "\nDate: " + str(self.date) 
        return text
    
    def collect_words(self):
        """creates a list containing the words associated to the review"""
        self.words = []
        self.words = word_tokenize(self.review_text)
        

    
