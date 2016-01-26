from django import template
from oscar.core.loading import get_class
register = template.Library()
Selector = get_class('partner.strategy', 'Selector')


@register.assignment_tag
def purchase_info_for_product(product):
    #  TODO: while request is not used in context
    strategy = Selector().strategy()
    if product.is_parent:
        return strategy.fetch_for_parent(product)

    return strategy.fetch_for_product(product)