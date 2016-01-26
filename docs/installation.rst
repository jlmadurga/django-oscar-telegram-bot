============
Installation
============

At the command line::

    $ pip install django-oscar-telegram-bot

Add it to your INSTALLED_APPS::

	INSTALLED_APPS = [
		...
		'oscar_telegrambot', # this app
		'telegrambot', #  django-telegram-bot
		'rest_framework', # django-telegram-bot uses django-rest-framework
		...
	]
	



