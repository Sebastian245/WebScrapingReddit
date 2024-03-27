import requests
from bs4 import BeautifulSoup
from database.db import db
from models.WebScrapperModel import WebScrapper

class WebScrapperService:
    @classmethod
    def createWebScrapping(cls):
        try:
            url = 'https://www.reddit.com/t/nba/'
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('article', class_='w-full m-0')
            for article in articles:
                title_element = article.find('shreddit-post').get('post-title')
                author_element = article.find('shreddit-post').get('author')
                created_timestamp = article.find('shreddit-post').get('created-timestamp')
                if title_element and author_element and created_timestamp:
                    title = title_element.strip()
                    author = author_element.strip()
                    creation_date = created_timestamp.split('T')[0] 
                    web_scrapper = WebScrapper(title=title, author=author, creationDate=creation_date)
                    web_scrapper.description="Description"
                    db.session.add(web_scrapper)
                    db.session.commit()

            return True, "Web scraping completed successfully"
        except Exception as ex:
            db.session.rollback()
            return False, f"An error occurred: {str(ex)}"


    @classmethod
    def getWebScrapping(cls):
        try:
            web_scrappers = WebScrapper.query.all()
            serialized_web_scrappers = [{
                'id': web_scrapper.id,
                'title': web_scrapper.title,
                'author': web_scrapper.author,
                'creationDate': web_scrapper.creationDate,
                'description': web_scrapper.description
            } for web_scrapper in web_scrappers]
            return True, serialized_web_scrappers
        except Exception as ex:
            return False, f"An error occurred: {str(ex)}"
