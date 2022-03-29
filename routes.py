from aiohttp import web
import aiohttp_jinja2
import jinja2
from handlers.functions import main_page, sign_up, sign_in, create_application, account_page, user_applications, user_votes


def setup_routes(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
    app.add_routes([
        web.get('/', main_page),
        web.get('/sign_up', sign_up),
        web.post('/sign_up', sign_up),
        web.get('/sign_in', sign_in),
        web.post('/sign_in', sign_in),
        web.get('/create_application', create_application),
        web.post('/create_application', create_application),
        web.get('/account_page', account_page),
        web.post('/account_page', account_page),
        web.get('/user_applications', user_applications),
        web.post('/user_applications', user_applications),
        web.get('/user_votes', user_votes),
        web.static('/static', 'static')
    ])
