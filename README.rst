=============================
django-oscar-telegram-bot
=============================

CI:

.. image:: https://img.shields.io/travis/jlmadurga/django-oscar-telegram-bot.svg
        :target: https://travis-ci.org/jlmadurga/django-oscar-telegram-bot

.. image:: https://coveralls.io/repos/jlmadurga/django-oscar-telegram-bot/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/jlmadurga/django-oscar-telegram-bot?branch=master
   :alt: Coveralls
  
.. image:: https://requires.io/github/jlmadurga/django-oscar-telegram-bot/requirements.svg?branch=master
     :target: https://requires.io/github/jlmadurga/django-oscar-telegram-bot/requirements/?branch=master
     :alt: Requirements Status
     
PyPI:


.. image:: https://img.shields.io/pypi/v/django-oscar-telegram-bot.svg
        :target: https://pypi.python.org/pypi/django-oscar-telegram-bot

Docs:

.. image:: https://readthedocs.org/projects/django-oscar-telegram-bot/badge/?version=latest
        :target: https://readthedocs.org/projects/django-oscar-telegram-bot/?badge=latest
        :alt: Documentation Status


Telegram Bot for Django-Oscar ecommerce.

Documentation
-------------

The full documentation is at https://django-oscar-telegram-bot.readthedocs.org.

This package uses django-telegram-bot, take a look to https://github.com/jlmadurga/django-telegram-bot


Quickstart
----------

Install django-oscar-telegram-bot::

    pip install django-oscar-telegram-bot

Add it to your INSTALLED_APPS::

	INSTALLED_APPS = [
		...
		'oscar_telegrambot', # this app
		'telegrambot', #  django-telegram-bot
		'rest_framework', # django-telegram-bot uses django-rest-framework
		...
	]
	
Configure in settings::

	TELEGRAM_BOT_COMMANDS_CONF = "oscar_telegrambot.commands"
	
As other django-telegram-bot app set your bot token::

	TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', None)
	
Add url to have webhook::

	url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
	
Use command  ``set_webhook`` to specify the url to receive the incoming updates via webhook::

	$ python manage.py set_webhook
	
To set the webhook for telegram you need ``django.contrib.sites`` installed, ``SITE_ID`` configured in settings and
with it correct value in the DB.

You can take a look to a demo repo using the sandbox in https://github.com/jlmadurga/django-oscar-telegram-bot-demo.
This demo is already installed in http://django-oscar-telegram-bot-demo.herokuapp.com/en-gb/ and you can test the
bot https://telegram.me/djangooscartelegrambotdemo_bot

Features
--------

* Wellcome and help commands
* Unknown command handler
* Categories list command
* Products list command
* Product detail command
* Order detail command

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py


