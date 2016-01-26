from oscar_telegrambot.commands_views import StartView, HelpView, UnknownView, \
    CategoryListDetailView, ProductListDetailView, OrdersCommandView


commandspatterns = [('start', StartView.as_command_view()),
                    ('help', HelpView.as_command_view()),
                    ('categories', CategoryListDetailView.as_command_view()),
                    ('products', ProductListDetailView.as_command_view()),
                    ('orders', OrdersCommandView.as_command_view()),
                    (None, UnknownView.as_command_view())
                    ]