# ---<{ Twitter Miner HelloWorld }>---
# ---<{ Made to practice the basics of data mining }>---
# ---<{ http://docs.tweepy.org/en/latest/getting_started.html }>---
# Dec. 10, 2020

# IMPORTS
import tweepy

# AUTHENTICATION SETUP 
auth = tweepy.OAuthHandler("zxulxRjPhgddUv5CdnLOH8Yur", "LdrailulMLEdEgroJuFntz464P4TtkU8GRVKxyVjWvDHAUw8cl")
auth.set_access_token("1337216469419978752-5HIEJozDrJtLFKZngVPq8Hcl88bw23", "6nyeO0k9JohJnHt7I73SXlrvaRtJ7zgSVKr2155xbs6o7")

api = tweepy.API(auth)

user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)