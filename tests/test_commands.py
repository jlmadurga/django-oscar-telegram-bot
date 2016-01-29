#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegrambot.test import testcases
try:
    from unittest import mock
except ImportError:
    import mock  # noqa
    
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
    fixtures = ['tests/fixtures/catalogue.json', 'tests/fixtures/partner.json']
    
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
    
    orders_list = {'in': '/orders',
                   'out': {'parse_mode': 'Markdown',
                           'reply_markup': '',
                           'text': 'order number'}                   
                   }
    
    orders_detail = {'in': '/orders',
                     'out': {'parse_mode': 'Markdown',
                             'reply_markup': '',
                             'text': ''}                        
                     }
    
    def test_categories_list(self):
        self._test_message_ok(self.categories_list)
        
    def test_categories_detail(self):
        self._test_message_ok(self.categories_detail)
        
    def test_products_list(self):
        self._test_message_ok(self.products_list)
        
    def test_products_detail(self):
        self._test_message_ok(self.products_detail)
        
    def test_orders_list(self):
        self._test_message_ok(self.orders_list)
        
    def test_orders_detail(self):
        self._test_message_ok(self.orders_detail)