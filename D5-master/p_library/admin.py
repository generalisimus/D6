from django.contrib import admin
from p_library.models import Book, Author, Edition, Friends


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'copy_count', 'price', 'edition', 'image')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    pass

@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    pass