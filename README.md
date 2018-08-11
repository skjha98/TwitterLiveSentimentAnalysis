# Twitter Live Sentiment Analysis
This is a NLP based project, uses NLTK Library

## Objectives
This project fetched the live twitter tweets for the selected "Text" and processes them to the txt file by classifying them as positive or negative. On the basis of the txt file, the live graph is plotted showing the responses from the tweets. 
This can be used in various ways like:
1. Getting the current trending topic on twitter, and what people's response about it.
2. Getting any relevant product review, or public opinion easily and effectively.
3. Helps in showing the trending business by doing business analysis.
4. Helps in predicting the trend over hot-topics over time-to-time.
5. Shows live fresh data, so you will get correct prediction and analysis.

## Requirements 
```
python3.5 or above
pip 10 or above
```
Packages or Libraries:
```
sklearn
nltk
pickle
statistics
tweepy
json
```
### For the requirements, just do:
Run the below command in CMD (base python as python3.5 or above)<br />
```pip install <library>```<br />
Run the below command in Terminal<br />
```pip3 install <library>```<br />

## Files
1. *first_run_classifier.py:* This is the initializing file. It initializes the pickled_algo dir and checks various classifiers.<br />

2. *sentiment_mod.py:* This is a module file fetched the pickled classifiers from the pickled_algo dir.<br />

3. *twitter_credentials:* This is the file containing the credentials authentication token for you twitter account. **Please Do not forgot to modify this file before running the analysis**.<br />

4. *tweet_live_fetch.py:* This is the file will fetches the tweets using the *twitter_credentials.py and sentiment_mod* module, to classify the tweets as positive and negative and saves them in the *twitter-out.txt* file.<br />

5. *live_analysis.py:* This is the file will initialize the live graph, **Run only after the initialization of *twitter-out.txt* file**.<br />


## How to Run
**Step 1**: Modify the *twitter_credentials.py* variables with your own twitter credential tokens.<br />

**Step 2**: Modiy the *tweet_live_fetch.py* file, `twitterStream.filter(track=["PUBG"])` replace "PUBG" with any of your favorite text, company name, product, political leader, movie, book, and so on, to do analysis on that specific thing.<br />

**Step 3**: Run the *tweet_live_fetch.py*.<br />

**Step 4**: Watch your directory, if *twitter-out.txt* has been initialized, run *live_analysis.py*.<br />


## Things to remember
If you run `tweet_live_fetch.py` again and again repeatively many times (10-25 times in 5min), may twitter would stop service for 1hr (I don't know the exact time though).

# HAPPY CODE PASTING
