from app import app
import urllib.request,json
from .models import news, sources

News = news.News
Sources = sources.Sources

# Getting api key

api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL1"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results 
    
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        title = news_item.get('title')
        desc = news_item.get('description')
        poster = news_item.get('urlToImage')
        url = news_item.get('url')
        category = news_item.get('category')

        if desc:
            news_object = News(source, title, desc, poster, url,category)
            news_results.append(news_object)

    return news_results