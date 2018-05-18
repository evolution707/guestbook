# guestbook
django实现带分页功能的留言簿

![Travis](https://img.shields.io/travis/USER/REPO.svg)

配置自己的mysql数据库
__
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guestbook',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
'''

通过模型类生成数据库表
__
python manage.py makemigrations
python manage.py migrate

