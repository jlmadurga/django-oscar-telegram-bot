#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tests import factories
from django.test.testcases import TestCase
from telegram.replykeyboardhide import ReplyKeyboardHide
from django.core.urlresolvers import reverse
try:
    from unittest import mock
except ImportError:
    import mock  # noqa
    
    
class BaseTestCommands(TestCase):
    csrf_checks = False
    setup_auth = False
    webhook_url = reverse('telegram-webhook')
    
    def setUp(self):
        super(BaseTestCommands, self).setUp()
        self.update = factories.UpdateFactory()  
        
    def assertInKeyboard(self, button, keyboard):
        found = False
        for line in keyboard:
            if button in line:
                found = True
                break
        self.assertTrue(found)
            
    def _test_command(self, command):
        self.update.message.text = "/" + command['command']
        with mock.patch("telegram.bot.Bot.sendMessage", callable=mock.MagicMock()) as mock_send:
            kwargs = {'content_type': 'application/json', }
            self.client.post(self.webhook_url, self.update.to_json(), **kwargs)
            args, kwargs = mock_send.call_args
            self.assertEqual(1, mock_send.call_count)
            self.assertEqual(kwargs['chat_id'], self.update.message.chat.id)
            self.assertEqual(kwargs['parse_mode'], command['values']['parse_mode'])
            #  print kwargs['text']
            if not command['values']['reply_markup']:
                self.assertTrue(isinstance(kwargs['reply_markup'], ReplyKeyboardHide))
            else:
                self.assertInKeyboard(command['values']['reply_markup'], kwargs['reply_markup'].keyboard)
                
            self.assertIn(command['values']['text'], kwargs['text'].decode('utf-8'))
    
class TestSimpleCommands(BaseTestCommands):
    start = {'command': 'start',
             'values': {'parse_mode': 'Markdown',
                        'reply_markup': '',
                        'text': "Wellcome to Oscar"}
             }
    
    help = {'command': 'help',
            'values': {'parse_mode': 'Markdown',
                       'reply_markup': '',
                       'text': 'You can control'}
            }
    
    unknown = {'command': 'unknown_command',
               'values': {'parse_mode': 'Markdown',
                          'reply_markup': '',
                          'text': 'Unknown command. Use /help'}
               }
            
    def test_start(self):
        self._test_command(self.start)
        
    def test_help(self):
        self._test_command(self.help)
        
    def test_unknonw(self):
        self._test_command(self.unknown)
        
class TestOscarCommands(BaseTestCommands):
    fixtures = ['tests/fixtures/catalogue.json', 'tests/fixtures/partner.json']
    
    categories_list = {'command': 'categories',
                       'values': {'parse_mode': 'Markdown',
                                  'reply_markup': '/categories books',
                                  'text': 'Books'}
                       }
    
    categories_detail = {'command': 'categories computers-in-literature',
                         'values': {'parse_mode': 'Markdown',
                                    'reply_markup': '/products tron',
                                    'text': 'Tron'}
                         }
    
    products_list = {'command': 'products',
                     'values': {'parse_mode': 'Markdown',
                                'reply_markup': '/categories books',
                                'text': 'select a category'}
                     }
    products_detail = {'command': 'products tron',
                       'values': {'parse_mode': 'Markdown',
                                  'reply_markup': '',
                                  'text': 'Tron'}                    
                       }
    
    orders_list = {'command': 'orders',
                   'values': {'parse_mode': 'Markdown',
                              'reply_markup': '',
                              'text': 'order number'}                   
                   }
    
    orders_detail = {'command': 'orders',
                     'values': {'parse_mode': 'Markdown',
                                'reply_markup': '',
                                'text': ''}                        
                     }
    
    def test_categories_list(self):
        self._test_command(self.categories_list)
        
    def test_categories_detail(self):
        self._test_command(self.categories_detail)
        
    def test_products_list(self):
        self._test_command(self.products_list)
        
    def test_products_detail(self):
        self._test_command(self.products_detail)
        
    def test_orders_list(self):
        self._test_command(self.orders_list)
        
    def test_orders_detail(self):
        self._test_command(self.orders_detail)