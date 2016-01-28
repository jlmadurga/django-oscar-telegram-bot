from oscar_telegrambot.commands_views import StartView, HelpView, UnknownView, \
    CategoryListDetailView, ProductListDetailView, OrdersCommandView
from telegrambot.handlers import command, unknown_command

bothandlers = [command('start', StartView.as_command_view()),
               command('help', HelpView.as_command_view()),
               command('categories', CategoryListDetailView.as_command_view()),
               command('products', ProductListDetailView.as_command_view()),
               command('orders', OrdersCommandView.as_command_view()),
               unknown_command(UnknownView.as_command_view())
               ]