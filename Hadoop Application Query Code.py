#python3
#run in python
import tweepy as tw
from datetime import datetime


consumer_key = 'T1ff8SfN5pN3bCWTSz9XyCKwY'
consumer_secret = '1LFsVIaKpVybmJRLkjvHH38dYivdwT94NIQ8uPlB3XEnLDqq3z' 

access_token = '1161449271528427520-isgg5ssfMN2JcAOvesaGH7cv9W7vHK' 
access_token_secret = 'nmhfVkmYAbOoAsTplcwyeEzqdnTZH5D7xAzNF2XqVdLXi'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tw.API(auth)


###QUESTION 1
#The query (or queries) to compute which celebrity has been the most tweeted about in 
		#the specified time frame
#CHANGE THIS TO ONLY PULL TWEETS FROM ONE HOUR -- datetime???
#******* FIX ABOVE ISSUE BEFORE SUBMITTING****** 

#beginTime = 2019-08-13T12:00:00Z
#endTime = 2019-08-13T13:00:00Z

kp_tweets_count = 0
for x in tw.Cursor(api.search,q='@katyperry',since='2019-08-15', count=200).items():
		kp_tweets_count+=1	

jb_tweets_count = 0
for x in tw.Cursor(api.search,q='@justinbieber',since='2019-08-15',count=200).items():
	jb_tweets_count+=1	

bo_tweets_count = 0
for x in tw.Cursor(api.search,q='@barackobama',since='2019-08-15', count=200).items():
	bo_tweets_count+=1		

rih_tweets_count = 0
for x in tw.Cursor(api.search,q='@rihanna',since='2019-08-15', count=200).items():
	rih_tweets_count+=1		

ts_tweets_count = 0
for x in tw.Cursor(api.search,q='@taylorswift13',since='2019-08-15', count=200).items():
	ts_tweets_count+=1		

gaga_tweets_count = 0
for x in tw.Cursor(api.search,q='@ladygaga',since='2019-08-15', count=200).items():
	gaga_tweets_count+=1

ellen_tweets_count = 0
for x in tw.Cursor(api.search,q='@theellenshow',since='2019-08-15', count=200).items():
	ellen_tweets_count+=1

cr_tweets_count = 0
for x in tw.Cursor(api.search,q='@cristiano',since='2019-08-15', count=200).items():
	cr_tweets_count+=1

jt_tweets_count = 0
for x in tw.Cursor(api.search,q='@jtimberlake',since='2019-08-15', count=200).items():
	jt_tweets_count+=1

ari_tweets_count = 0
for x in tw.Cursor(api.search,q='@arianagrande',since='2019-08-15', count=200).items():
	ari_tweets_count+=1

celeb_tweet_counts = {
'@katyperry':kp_tweets_count,
'@justinbieber':jb_tweets_count,
'@barackobama':bo_tweets_count,
'@rihanna':rih_tweets_count,
'@taylorswift13':ts_tweets_count,
'@ladygaga':gaga_tweets_count,
'@theellenshow':ellen_tweets_count,
'@cristiano':cr_tweets_count,
'@jtimberlake':jt_tweets_count,
'@arianagrande':ari_tweets_count
}

max_num_tweets = max(celeb_tweet_counts, key=celeb_tweet_counts.get)
print('The celebrity with the most tweets about him or her is:')
print(max_num_tweets,celeb_tweet_counts[max_num_tweets])



###QUESTION 2
#The query (queries) to compute for the most celebrity tweeted about, 
		#who has tweeted the most about that celebrity in the time specified
max_celeb = max_num_tweets

max_celeb_tweets = tw.Cursor(api.search,
	q=max_celeb,
	since="2019-08-15").items(19)

users = []
for tweet in max_celeb_tweets:
    users.append(tweet.user.screen_name)

user_count_dict = {x:users.count(x) for x in users}
max_user_tweets = max(user_count_dict, key=user_count_dict.get) 
print("The user who has tweeted the most about " + max_celeb + " is: " + max_user_tweets+ ", with count of: " + str(user_count_dict[max_user_tweets]))



###QUESTION 3
#The results of executing these queries. Additionally, in a table, show the 
		#total number of tweets for each of these celebrities.
import pandas as pd

celeb_tweet_df = pd.DataFrame(list(celeb_tweet_counts.items()),columns = ['celebrity_handle','num_tweets'])
print(celeb_tweet_df)



