from django.contrib import admin

from . import models

# Inline enables us to utilise admin interface in django admin page
# to edit models(tables/class) on the same page as parent model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
