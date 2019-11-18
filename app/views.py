from flask import render_template
from app import app
from .request import get_news
# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    
    # Getting popular news
    trending_news = get_news()
    
    
    # breaking_news = get_news('breaking')

    title = 'Home -News Highlights'
    return render_template('index.html', title = title, trending =trending_news)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view news page function that returns the news highlight page and its data
    '''
    return render_template('news.html',id = news_id)
    