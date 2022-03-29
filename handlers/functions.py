import aiohttp_jinja2
from datetime import datetime
from components.add_data import add_user, add_crossroad, add_vote
from components.add_data import get_user, get_crossroads, get_user_crossroads, get_user_votes


async def main_page(request):
    applications = await get_crossroads()
    return aiohttp_jinja2.render_template('index.html', request, {'applications': applications})


async def account_page(request):
    if request.method == 'POST':
        data = await request.post()
        crossroad_id = int(data['card_id'])
        await add_vote(current_user, crossroad_id)
    applications = await get_crossroads()
    return aiohttp_jinja2.render_template('account_page.html', request, {'user_name': name,
                                                                         'user_city': city,
                                                                         'user_role': role,
                                                                         'user_address': address,
                                                                         'user_mobile': mobile,
                                                                         'user_sex': sex,
                                                                         'applications': applications})


async def user_applications(request):
    applications = await get_user_crossroads(current_user)
    return aiohttp_jinja2.render_template('user_applications.html', request, {'applications': applications})


async def user_votes(request):
    applications = await get_user_votes(current_user)
    return aiohttp_jinja2.render_template('user_votes.html', request, {'applications': applications})


async def sign_up(request):
    if request.method == 'POST':
        try:
            data = await request.post()
            name = data['name']
            role = data['role']
            city = data['city']
            address = data['address']
            mobile = data['mobile']
            sex = data['sex']
            login = data['login']
            password = data['password']
            await add_user(login, password, name, sex, city, address, mobile, role)
            status = 'Пользователь зарегестрирован'
        except:
            status = 'Произошла ошибка регистации, попробуйте снова'

        return aiohttp_jinja2.render_template('signup_form.html', request, {'status': status})
    else:
        return aiohttp_jinja2.render_template('signup_form.html', request, {'': ''})


async def sign_in(request):
    if request.method == 'POST':
        data = await request.post()
        login = data['login']
        password = data['password']
        record = await get_user(login, password)
        if record:
            global current_user, name, city, role, address, mobile, sex
            name = record.name
            city = record.city
            role = record.role
            address = record.address
            mobile = record.mobile
            sex = record.sex
            current_user = record.user_id
            applications = await get_crossroads()
            return aiohttp_jinja2.render_template('account_page.html', request, {'user_name': name,
                                                                                 'user_city': city,
                                                                                 'user_role': role,
                                                                                 'user_address': address,
                                                                                 'user_mobile': mobile,
                                                                                 'user_sex': sex,
                                                                                 'applications': applications})
        else:
            status = 'Неверно введен логин или пароль'
            return aiohttp_jinja2.render_template('signin_form.html', request, {'status': status})
    else:
        return aiohttp_jinja2.render_template('signin_form.html', request, {'': ''})


async def create_application(request):
    if request.method == 'POST':
        try:
            data = await request.post()
            date = datetime.today().date()
            location = data['location']
            longitude = float(data['longitude'])
            latitude = float(data['latitude'])
            map = bytearray("test".encode("ascii"))
            description = data['description']
            votes_number = 1
            status = data['status']
            user_id = current_user
            await add_crossroad(date, location, longitude, latitude, map, description, votes_number, status, user_id)
            status = 'Обращение подано'
            return aiohttp_jinja2.render_template('crossroad_form.html', request, {'status': status})
        except:
            status = 'Произошла ошибка, попробуйте снова'
            return aiohttp_jinja2.render_template('crossroad_form.html', request, {'status': status})

    else:
        return aiohttp_jinja2.render_template('crossroad_form.html', request, {'': ''})
