#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegrambot.test import testcases
from telegrambot.models import AuthToken, Chat
from django.core.urlresolvers import reverse
from oscar.core.compat import get_user_model
try:
    from unittest import mock
except ImportError:
    import mock  # noqa
    
User = get_user_model()
    
class TestSimpleCommands(testcases.BaseTestBot):
    start = {'in': '/start',
             'out': {'parse_mode': 'Markdown',
                     'reply_markup': '',
                     'text': "Wellcome to Oscar"}
             }
    
    help = {'in': '/help',
            'out': {'parse_mode': 'Markdown',
                    'reply_markup': '',
                    'text': 'You can control'}
            }
    
    unknown = {'in': '/unknown_command',
               'out': {'parse_mode': 'Markdown',
                       'reply_markup': '',
                       'text': 'Unknown command. Use /help'}
               }
            
    def test_start(self):
        self._test_message_ok(self.start)
        
    def test_help(self):
        self._test_message_ok(self.help)
        
    def test_unknonw(self):
        self._test_message_ok(self.unknown)
        
class TestOscarCommands(testcases.BaseTestBot):
    fixtures = ['tests/fixtures/catalogue.json', 'tests/fixtures/partner.json', 'tests/fixtures/users.json',
                'tests/fixtures/orders.json', 'tests/fixtures/baskets.json', 'tests/fixtures/addresses.json']
    
    categories_list = {'in': '/categories',
                       'out': {'parse_mode': 'Markdown',
                               'reply_markup': '/categories books',
                               'text': 'Books'}
                       }
    
    categories_detail = {'in': '/categories computers-in-literature',
                         'out': {'parse_mode': 'Markdown',
                                 'reply_markup': '/products tron',
                                 'text': 'Tron'}
                         }
    
    products_list = {'in': '/products',
                     'out': {'parse_mode': 'Markdown',
                             'reply_markup': '/categories books',
                             'text': 'select a category'}
                     }
    products_detail = {'in': '/products tron',
                       'out': {'parse_mode': 'Markdown',
                               'reply_markup': '',
                               'text': 'Tron'}                    
                       }
    
    orders_list_not_authed = {'in': '/orders',
                              'out': {'parse_mode': 'Markdown',
                                      'reply_markup': '',
                                      'text': "You need an *authenticated chat*" +
                                              " to perform this action please login" +
                                              " [here](https://example.com/telegrambot/auth/"
                                    }                   
                              }
    
    orders_list_authed = {'in': '/orders',
                          'out': {'parse_mode': 'Markdown',
                                  'reply_markup': '/orders 100001',
                                  'text': "This is the list of the orders:\nOrder 100001- "}
                          }
    
    orders_detail_not_authed = {'in': '/orders 100001',
                                'out': {'parse_mode': 'Markdown',
                                        'reply_markup': '',
                                        'text': "You need an *authenticated chat*" +
                                              " to perform this action please login" +
                                              " [here](https://example.com/telegrambot/auth/"
                                        }
                            }
    
    orders_detail_authed = {'in': '/orders 100001',
                                'out': {'parse_mode': 'Markdown',
                                        'reply_markup': '',
                                        'text': 'Order *100001*'}                        
                                }

    def test_categories_list(self):
        self._test_message_ok(self.categories_list)
        
    def test_categories_detail(self):
        self._test_message_ok(self.categories_detail)
        
    def test_products_list(self):
        self._test_message_ok(self.products_list)
        
    def test_products_detail(self):
        self._test_message_ok(self.products_detail)
        
    def test_orders_list_not_authed(self):
        self._test_message_ok(self.orders_list_not_authed)        
        
    def test_orders_list_authed(self):
        login = self.client.login(email="user1@example.com", password=u'password1')
        user = User.objects.get(email="user1@example.com")
        token = AuthToken.objects.create(user=user)
        chat = Chat.objects.create(**self.update.message.chat.to_dict())
        token.chat_api = chat
        token.save()
        self._test_message_ok(self.orders_list_authed)
        
    def test_orders_list_detail_not_authed(self):
        self._test_message_ok(self.orders_detail_not_authed)    
        
    def test_orders_detail_authed(self):
        login = self.client.login(email="user1@example.com", password=u'password1')
        user = User.objects.get(email="user1@example.com")
        token = AuthToken.objects.create(user=user)
        chat = Chat.objects.create(**self.update.message.chat.to_dict())
        token.chat_api = chat
        token.save()
        self._test_message_ok(self.orders_detail_authed)