from flask import render_template
from app import app
from .request import get_newssource 
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Hello World '
    news_sources=get_newssource()
    title="Home-Welcome to NEWS sources Website"
    return render_template('index.html',title=title,newssource=news_sources)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news article function that returns the news articles page and its data
    '''
    
    title=news_id
    return render_template ('news.html',id=news_id,title=title)