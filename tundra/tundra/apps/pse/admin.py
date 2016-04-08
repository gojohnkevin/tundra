from django.contrib import admin

from pse.models import Sector, Index


class IndexAdmin(admin.ModelAdmin):
    list_filter = ('status',)

admin.site.register(Sector)
admin.site.register(Index, IndexAdmin)
