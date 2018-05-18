# guestbook
django实现带分页功能的留言簿

![Travis](https://img.shields.io/travis/USER/REPO.svg)

<h3>配置自己的mysql数据库</h3>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guestbook',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

执行
python manage.py makemigrations
python manage.py migrate
通过模型类生成数据库表
