# wsgi.py

from apps import create_app

application = create_app('config.ini')

if __name__ == '__main__':
    application.run()