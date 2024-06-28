from django.contrib import admin
from .models import Order, Problem, Article, Clients


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['client', 'phone']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'date', 'is_active']
    actions = [set_active]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'phone', 'text', 'date', 'is_active']
    actions = [set_active]


class ProblemAdmin(admin.ModelAdmin):
    list_display = ['problem', 'is_active']
    actions = [set_active]


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Problem, ProblemAdmin)
