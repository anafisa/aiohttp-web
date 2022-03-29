from aiohttp import web
from config import get_config
from main import create_app


if __name__ == '__main__':
    config = get_config()
    web.run_app(create_app(config), port=config['port'])
