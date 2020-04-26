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
    general_news_sources=get_newssource('general')
    technology_news_sources=get_newssource('technology')
    business_news_sources=get_newssource('business')
    sports_news_sources=get_newssource('sports')
    entertainment_news_sources=get_newssource('entertainment')
    health_news_sources=get_newssource('health')
    science_news_sources=get_newssource('science')

    title="Home-Welcome to NEWS sources Website"
    return render_template('index.html',title=title,general=general_news_sources,
    technolgy=technology_news_sources,business=business_news_sources,sports=sports_news_sources,entertainment=entertainment_news_sources,health=health_news_sources,
    science=science_news_sources)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news article function that returns the news articles page and its data
    '''
    
    title=news_id
    return render_template ('news.html',id=news_id,title=title)