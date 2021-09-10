class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost:5432/test_db'


	# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

	# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@hostname/database_name'

	SQLALCHEMY_DATABASE_URI = 'postgresql://zamer:1@localhost:5432/test'
	# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost:5432/test_db'