from pprint import pprint

import requests


class NewsFeed:
    """ Representing multiple options for news feed."""
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'apiKey=8faa0de902864f4eaf19b6a2034bff03'

    def __init__(self, interest, from_date, to_date, language):
        self.language = language
        self.from_date = from_date
        self.to_date = to_date
        self.interest = interest

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&to={self.to_date}&' \
              f'language={self.language}&' \
              f'{self.api_key}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body = ''

        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body


