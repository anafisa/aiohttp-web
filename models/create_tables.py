import asyncio
import ssl
from models import db
from models.users import User
from models.crossroads import Crossroad
from models.votes import Vote


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


async def main():
    await db.set_bind('your_path', ssl=ctx)
    await db.gino.create_all()
    user = await User.query.gino.first()
    crossroad = await Crossroad.query.gino.first()
    vote = await Vote.query.gino.first()

    print(f'User: {user}')
    print(f'Crossroad: {crossroad}')
    print(f'Vote: {vote}')


if __name__ == '__main__':
    asyncio.run(main())
