from django.contrib import admin

from .models import Language, Snippet


class LanguageAdmin(admin.ModelAdmin):
    pass

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    

admin.site.register(Language,LanguageAdmin)
admin.site.register(Snippet,SnippetAdmin)

#Configuración del Panel
title = "Proyecto Snippets"
subtitle = "Panel de Gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle