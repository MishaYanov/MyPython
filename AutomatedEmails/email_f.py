import yagmail
import pandas
from news import NewsFeed
from datetime import date

today = date.today()
today_day = today.strftime("%Y-%m-%d")
df = pandas.read_excel('Book1.xlsx')
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interests'], from_date=today_day, to_date=today_day, language='en')
    email = yagmail.SMTP(user='example@example.com', password="yourpassword")
    email.send(to=row['emails'], subject=f"Hi {row['users']}! These are your {row['interests']} news!",
               contents="Your news are below!\n\n"
                        f"{news_feed.get()}")
