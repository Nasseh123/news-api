from flask import render_template
from app import app
from .request import get_newssource,get_news_article
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Hello World '
    general_news_sources=get_newssource()
    # technology_news_sources=get_newssource('technology')
    # business_news_sources=get_newssource('business')
    # sports_news_sources=get_newssource('sports')
    # entertainment_news_sources=get_newssource('entertainment')
    # health_news_sources=get_newssource('health')
    # science_news_sources=get_newssource('science')
    # https://newsapi.org/v2/sources?apiKey=3a1f09f201904834870e3fdbb44430ee

    title="Home-Welcome to NEWS sources Website"
    return render_template('index.html',title=title,general=general_news_sources)

@app.route('/news/<source>')
def news(source):
    '''
    View news article function that returns the news articles page and its data
    '''
    newsarticle=get_news_article(source)
    # title=f'{newsarticle.title}'
    print(newsarticle)
    return render_template ('news.html',news=newsarticle)
