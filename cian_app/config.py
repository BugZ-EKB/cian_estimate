import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(os.path.join(basedir, '..', 'cian_app.db'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'cian_app.db')

SECRET_KEY = 'fansof1091g3sdgds32t32'