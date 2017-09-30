## Docu
- [中国极地科学数据共享平台专用元数据标准](http://211.95.58.188:4000/wulizong/Chinare_v2/wikis/meta_by_wulizong)
- [chinare_v2-元数据库设计_与v1字段对应关系](http://211.95.58.188:4000/wulizong/Chinare_v2/wikis/chinare_v2-%E5%85%83%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1_%E4%B8%8Ev1%E5%AD%97%E6%AE%B5%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB)

## Installment

- python 3.6
- django 1.11
- postgresql 9.6

## Database Structure Initial

```sh
cd src/chinare
python manage.py makemigrations
python manage.py migrate
```

## Database Configuration
src/chinare/chinare/settings.py:
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chinare',
        'USER': 'chinare',
        'PASSWORD': 'chinare',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'v1': {
        'ENGINE': 'django.db.backends.oracle', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'orcl',                      # Or path to database file if using sqlite3.
        'USER': 'CHINARE',                      # Not used with sqlite3.
        'PASSWORD': 'chinare',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'threaded': True}, 
    },
}
```
## Database Migration from V1 
```sh
cd src/chinare/migrate
python importDataFromV1.py
```


## Run

```sh
cd src/chinare
python manage.py runserver
```

## Integration with Wagtail CMS

```sh

python manage.py installtasks

crontab -l

```

## Integration with kronos

```sh

pip install wagtail

```

[configuration references **ignore it**](http://docs.wagtail.io/en/latest/getting_started/integrating_into_django.html)

login with superuser and visit http://localhost:8000/cms

[ten minutes develop guide](http://docs.wagtail.io/en/latest/getting_started/tutorial.html)