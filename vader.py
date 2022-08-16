# This is apip
review = input("enter a sentence")
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def vader_analysis(review):
    analyzer = SentimentIntensityAnalyzer()
    rating = analyzer.polarity_scores(review)
    ratings = rating['compound']
    if ratings > 0.05:
        a = 'positive'
    elif ratings < -0.05:
        a = 'negative'
    else:
        a = 'neutral'
    return a



rating = vader_analysis(review)

print(rating)