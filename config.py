class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Potolock@localhost:5432/postgres'

	SECRET_KEY = 'topsecret'


	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'bcrypt'


	SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
