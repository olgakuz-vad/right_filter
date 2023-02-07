from django.contrib import admin
from .models import PostCategory, Post, Author, Comment, Category

#так можно привязать промежуточную модель между моделями
class  PostCategoryInline(admin.TabularInline ):
    model  =  PostCategory
    extra  =  1
    show_change_link  =  True

class PostAdmin(admin.ModelAdmin):
    inlines  = [PostCategoryInline]

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)