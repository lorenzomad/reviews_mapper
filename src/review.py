import nltk 

nltk.download("stopwords")
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer



"""Module containing the class Review 
and methods to perform analysis of a review"""

class Review():
    """class that contains a review for a product"""
    def __init__(self, review_text, rating, region, date ):
        self.review_text = review_text
        self.rating = rating
        self.region = region
        self.date = date
        self.collect_words()
        self.lemmatization()

    def __repr__(self):
        text = "Review text: " + self.review_text + "\nRating: " \
            + str(self.rating) + "\nRegion: "+ str(self.region) + "\nDate: " + str(self.date) 
        return text
    
    def collect_words(self):
        """creates a list containing the words associated to the review
        in the variable original_words"""
        self.original_words = []
        self.original_words = word_tokenize(self.review_text)

    def lemmatization(self):
        """creates the lemmatized words list in lemmatized_words"""
        lancaster = LancasterStemmer()
        self.lemmatized_words = []
        for word in self.original_words:
            self.lemmatized_words.append(lancaster.stem(word))
            
    

    # def word_count(self):
    #     """counts the number of times the original_words are repeated in the lemmatized 
    #     lemmatized_words list if present"""
    #     if self.lemmatized_words != None:
    #         self.words_count = {word:words_count.count(word) for word in self.lemmatized_words}
    #     else:
    #         self.words_count = {word:words_count.count(word) for word in self.original_words}

    def remove_stopwords_punctuation(self):
        """removes the punctuation and stoporiginal_words from the review original_words"""
        pass

    
