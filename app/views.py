from flask import render_template
from app import app

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Home -News Highlights'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view news page function that returns the news highlight page and its data
    '''
    return render_template('news.html',id = news_id)