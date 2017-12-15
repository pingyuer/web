from django.contrib import admin
from article.models import Article
from users.models import User

# Register your models here.

admin.site.register(Article)
admin.site.register(User)
