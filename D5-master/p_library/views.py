from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from .models import Author, Book, Edition, Friends
from django.http import HttpResponse
from p_library.models import Author  
from p_library.forms import AuthorForm, BookForm, FriendsForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect

def base(request):
    template = loader.get_template('base.html')
    biblios_data = {
        "titles": "моя библиотека",
    }
    return HttpResponse(template.render(biblios_data, request))

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    friends = Friends.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "friends": friends,

    }
    return HttpResponse(template.render(biblio_data, request))

def edition(request):
    template = loader.get_template('edition.html')
    editions = Edition.objects.all()
    books = Book.objects.all()
    data_edition = {
        "editions": editions,
        "books": books,
    }
    return HttpResponse(template.render(data_edition, request))
    
def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
                book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'author_edit.html'  

class AuthorList(ListView):  
    model = Author  
    template_name = 'author_list.html'

class FriendsEdit(CreateView):
    model = Friends
    form_class = FriendsForm
    success_url = reverse_lazy('p_library:index')
    template_name = 'friend_form.html'

class FriendsList(ListView):
    model = Friends
    template_name = 'index.html'    

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:  
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:  
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})

def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=4)  
    BookFormSet = formset_factory(BookForm, extra=1)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
        request,  
        'manage_books_authors.html',  
        {  
            'author_formset': author_formset,  
            'book_formset': book_formset,  
        }  
    )