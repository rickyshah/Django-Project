from django.contrib import admin

from . import models

# we can change how django admin interface looks, or has
# to change the admin interface
# we use the following class(the naming convention is model name followed by Admin)
class PostAdmin(admin.ModelAdmin):
    # change the order of fields
    fields = ['user', 'group', 'message']

    # add search bar, search_fields is built in keyword
    # we can pass the fields we can search
    search_fields = ['message']

    # NOTES: if a searching field is a foreign key of another model
    # then the search has to also include the proper field in the search seperated by two underscore
    # e.g: if 'user' was a foreign field from User class/model and it was named
    # as userName in that model, then the search would have been like below
    # search_fields = ['user__userName']

    # add filter bar on the right hand side of admin interface
    # it helps to quickly filter large data without needing to do search
    # we use builtin keyword 'list_filter'
    list_filter = ['user']

    # display as many fields as we want on admin interface by using 'list_display'
    list_display = ['message', 'user', 'group']

    # edit fields using 'list_editable', 
    # we also need to add 'list_display' before we can use it
    # some fields may not be editable 
    # as it needs to go to seperat detail url page like the one 'message'
    # *********************************************
    # NOTE: USING LIST_EDITABLE TIS NOT RECOMMENDED,
    # IT CAN CAUSE TOO MANY USERS EDITING SAME TIME
    # *********************************************
    list_editable = ['user', 'group']
    




admin.site.register(models.Post, PostAdmin)


