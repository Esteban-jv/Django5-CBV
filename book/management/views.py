from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic import DetailView, ListView
from .forms import BookForm
from .models import Book

# Create your views here.
#Vista básica para creación con un formulario específico
class BookSaveFormView(FormView):
    template_name = 'book/save.html'
    form_class = BookForm
    success_url = '/management/save/success'

    # This is what we have to handle before actually saving the record
    def form_valid(self, form):
        form.save()
        return super().form_valid(form) # Actually save the record

#Vista básica para creación
class BookCreateFormView(CreateView):
    model=Book
    template_name = 'book/save.html'
    form_class = BookForm
    # fields = ['name',] # Es posible seleccionar solo los campos que se desean editar, peor hay que quitar form_class
    success_url = '/management/save/success'

#Vista básica para edición
class BookUpdateFormView(UpdateView):
    model=Book
    template_name = 'book/save.html'
    form_class = BookForm
    # fields = ['name',] # Es posible seleccionar solo los campos que se desean editar, peor hay que quitar form_class
    success_url = '/management/save/success'

#Vista básica para el detalle
class BookDetailFormView(DetailView):
    model=Book
    template_name = 'book/detail.html'
    #Opcional
    context_object_name = 'libro' # Para cambiar el nombre "object" o "book" que recibe el template

#Vista básica para eliminacion
class BookDeleteFormView(DeleteView):
    model=Book
    template_name = 'book/delete.html'
    success_url = '/management/save/success'

#Vista básica para lista de libros
class BookListFormView(ListView):
    model=Book
    template_name = 'book/index.html'

# Vista básica para consulta
class BookSaveFormSuccessView(View):
    def get(self, request):
        return HttpResponse('El libro se creó')
