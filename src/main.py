import os 

from review import Review
from product_reviews import ProductReviews

def main():

    review_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'review_example','review.txt')
    
    with open(review_file, 'r') as file:
        review_examples = file.readlines()
    
    review_examples = [review.replace("\"", '') for review in review_examples]

    reviews = [Review(review,0,0,0) for review in review_examples]

    product_reviews = ProductReviews(reviews)
    product_reviews.generate_wordcloud()
    
    

if __name__ == "__main__":
    main()


