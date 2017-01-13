import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'BUBKLE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	BLOG_ADMIN = os.environ.get('BLOG_ADMIN')
	MAIL_SUBJECT_PREFIX = '[BLOG]'
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_SENDER = 'BLOG ADMIN <testonly01@163.com>'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
