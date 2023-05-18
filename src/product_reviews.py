import stylecloud

from review import Review


class ProductReviews:
    def __init__(self, reviews : Review) -> None:
        self.reviews = reviews
        self.words = self.unwrap_reviews()

    def unwrap_reviews(self):
        words = [' '.join(review.lemmatized_words) for review in self.reviews]
        return '\n'.join([string for string in words])


    def generate_wordcloud(self):
        """generates an image of the wordcloud for the product"""
        stylecloud.gen_stylecloud(
            text = self.words,
            icon_name = 'fas fa-flag'
        )


