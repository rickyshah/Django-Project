from django.shortcuts import render

from django.views.generic import TemplateView, ListView


from .models import Product


class Products_Index(ListView):
    template_name = 'products_index.html'
    model = Product

    # Django generic views(e.g View, TemplateView, ListView etc) gives access
    # to all the property(fields) of a model(s)
    # this can be access using any two variables 'object_list' and 'modelName_list'

    # 'object_list' is generic way of accessing the fields of any Model, it refers
    # to the model that is used in a class, so if we are using model Product
    # it stores all the fields of Product,  for model Customer, its fields etc

    # 'modelName_list' which in our case is 'product_list' is another way where
    # django built in generic views stores the fields of a model. The naming conventions
    # is model name followed by underscore followed by list, all in small letter
    # this way we can reference any specific model we like

    # we can iterate through the product_list in html page
    # using {% if %} template tag

    # we can also use our own variable to store the list, we use context_object_name
    # this way we know our list name in the html page
    context_object_name = 'products'


class Products_New(TemplateView):
    template_name = 'products_new.html'
