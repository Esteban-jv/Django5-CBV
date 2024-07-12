from django.urls import path
from .views import BookSaveFormView, BookSaveFormSuccessView, BookUpdateFormView, BookCreateFormView, BookDeleteFormView, BookDetailFormView, BookListFormView

app_name = 'management'
urlpatterns = [
    path('/save/', BookSaveFormView.as_view(), name='save'),
    path('/', BookListFormView.as_view(), name='index'),
    path('/create/', BookCreateFormView.as_view(), name='create'),
    path('/detail/<int:pk>', BookDetailFormView.as_view(), name='show'),
    path('/update/<int:pk>', BookUpdateFormView.as_view(), name='update'),
    path('/delete/<int:pk>', BookDeleteFormView.as_view(), name='delete'),
    path('/save/success', BookSaveFormSuccessView.as_view(), name='book_success_message'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='delete'),
]