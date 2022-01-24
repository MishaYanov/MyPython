import datetime
import time
import yagmail
import pandas
from news import NewsFeed
from datetime import *

def getInfo(users, emails, interests):
    print(users, emails, interests)
    today = date.today()
    today_day = today.strftime("%Y-%m-%d")
    news_feed = NewsFeed(interest=interests, from_date=today_day, to_date=today_day, language='en')
    email = yagmail.SMTP(user='misha.news.feed@gmail.com', password="DragOn666")
    email.send(to=emails, subject=f"Hi {users}! These are your {interests} news!",
    contents="Your news are below!\n\n"
         f"{news_feed.get()}")                                          

