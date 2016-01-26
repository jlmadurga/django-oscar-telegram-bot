from oscar.core.loading import get_model, get_class
from telegrambot import generic

Category = get_model('catalogue', 'Category')
Product = get_model('catalogue', 'Product')
Order = get_model('order', 'Order')
Selector = get_class('partner.strategy', 'Selector')

class StartView(generic.TemplateCommandView):
    template_code = "start"
    
class HelpView(generic.TemplateCommandView):
    template_code = "help"
    
class UnknownView(generic.TemplateCommandView):
    template_code = "unknown"
    
class CategoryListView(generic.ListCommandView):
    template_code = "categories_list"
    model = Category
    context_object_name = "category_list"
    
class CategoryDetailView(generic.DetailCommandView):
    template_code = "categories_detail"
    context_object_name = "product_list"
    
    def __init__(self, slug=None):
        super(CategoryDetailView, self).__init__(slug)
        self.category = Category.objects.get(slug=self.get_slug())
        
    def get_queryset(self):
        qs = Product.browsable.base_queryset()
        if self.slug:
            qs = qs.filter(categories__in=self.category.get_descendants_and_self
                           ()).distinct()
        return qs
    
    def get_context(self, update):
        products = self.get_queryset().all()        
        context = {'context_object_name': products}
        if self.context_object_name:
            context[self.context_object_name] = products
        context['category'] = self.category
        selector = Selector()
        context['request'] = selector.strategy()
        return context
        
    
class CategoryListDetailView(generic.ListDetailCommandView):
    list_view_class = CategoryListView
    detail_view_class = CategoryDetailView
    
    
class ProductDetailView(generic.DetailCommandView):
    template_code = "products_detail"
    context_object_name = "product"
    model = Product
    slug_field = 'slug'
    
class ProductSelectOneView(generic.ListCommandView):
    template_code = "products_list"
    model = Category
    context_object_name = "category_list"
    
class ProductListDetailView(generic.ListDetailCommandView):
    list_view_class = ProductSelectOneView
    detail_view_class = ProductDetailView
    
class OrdersDetailView(generic.DetailCommandView):
    template_code = "orders_detail"
    context_object_name = "order"
    model = Order
    slug_field = 'number'
    
class OrdersListView(generic.TemplateCommandView):
    template_code = "orders_list"
    
class OrdersCommandView(generic.ListDetailCommandView):
    list_view_class = OrdersListView
    detail_view_class = OrdersDetailView
