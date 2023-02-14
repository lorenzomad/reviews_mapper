# reviews_mapper
Web application that creates a wordmap based on the words in the reviews for a project.

# Main functionalities

- The web app will allow to paste a link from one of the main review sites (#to be implemented amazon, google reviews) and provide a wordmap of the most common words used.
- Filler words, punctuation and articles will be removed
- Synonyms and alterations of a single word will count towards the same value
- The user will be able to filter on dates/region/value of the review
- The user can click one word and it will open the review website highlighting the word in the reviews
- (Potential) The web app will show an evaluation of the most common words: is it positive or negative) 

# architecture

review_mapper will be composed of the following modules:

- frontend - GUI for the web app
- word analysis module - to apply language analysis to the words in the reviews
- mapper - to create the wordmap graph
- web scraper - to obtain starting from the webpage a list of the words to analyze (possibly using APIs)

# continuous integration and testing

the webapp will be provided with continuous integration and the development will be testing driven
