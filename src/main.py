import os 


from word_analysis import Review

def main():

    review_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'review_example','review.txt')
    
    with open(review_file, 'r') as file:
        review_example = file.read()

    
    review = Review(review_example,0,0,0)

    print(review)
    review.collect_words()
    print(review.review_text)
    # review.collect_words()
    # review.remove_useless()
    # review.simplify()
    # review.word_count()

    #word_analysis.


if __name__ == "__main__":
    main()


