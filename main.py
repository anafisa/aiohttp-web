import ssl
from models import db
from aiohttp import web
from routes import setup_routes


async def before_server_start(app):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    await db.set_bind(app['config']['db_path'], ssl=ctx)
    await db.gino.create_all()


async def after_server_stop(_):
    await db.pop_bind().close()


async def create_app(config):
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    app.on_startup.append(before_server_start)
    app.on_cleanup.append(after_server_stop)
    return app



