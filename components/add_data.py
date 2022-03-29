from models.users import User
from models.crossroads import Crossroad
from models.votes import Vote
import gino


async def add_user(login, password, name, sex, city, address, mobile, role):
    user = User(login=login,
                password=password,
                name=name,
                sex=sex,
                city=city,
                address=address,
                mobile=mobile,
                role=role)
    await user.create()


async def add_crossroad(date, location, longitude, latitude, map, description, votes_number, status, user_id):
    crossroad = Crossroad(date=date,
                          location=location,
                          longitude=longitude,
                          latitude=latitude,
                          map=map,
                          description=description,
                          votes_number=votes_number,
                          status=status,
                          user_id=user_id)
    await crossroad.create()


async def add_vote(user_id, crossroad_id):
    exist = await Vote.query.where((Vote.user_id == user_id) &
                                   (Vote.crossroad_id == crossroad_id)).gino.first()
    if not exist:
        vote = Vote(user_id=user_id, crossroad_id=crossroad_id)
        record = await Crossroad.query.where((Crossroad.crossroad_id == crossroad_id)).gino.first()
        n = record.votes_number + 1

        await vote.create()
        await record.update(votes_number=n).apply()


async def get_user(login, password):
    record = await User.query.where((User.login == login) &
                                    (User.password == password)).gino.first()
    return record


async def get_crossroads():
    all_crossroads = await Crossroad.query.order_by(Crossroad.date.desc()).gino.all()
    return all_crossroads


async def get_user_crossroads(user_id):
    all_crossroads = await Crossroad.query.where(Crossroad.user_id == user_id).order_by(Crossroad.date.desc()).gino.all()
    return all_crossroads


async def get_user_votes(current_user):
    all_crossroads = []
    all_votes = await Vote.query.where(Vote.user_id == current_user).gino.all()
    for i in all_votes:
        res = await Crossroad.query.where(Crossroad.crossroad_id == i.crossroad_id).gino.first()
        all_crossroads.append(res)

    return all_crossroads
