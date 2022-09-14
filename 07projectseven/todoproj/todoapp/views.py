from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Create your views here.

from .models import TodoModel
from .forms import TodoForm


def index(request):
    mytodo = TodoModel.objects.order_by("pk")
    form = TodoForm()
    context = {'mytodo': mytodo, 'form': form}
    return render(request, "todoapp/index.html", context)


@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = TodoModel(task=request.POST['text'])
        my_new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    mytodo = TodoModel.objects.get(pk=todo_id)
    mytodo.completed = True
    mytodo.save()

    return redirect('index')


def deleteTodo(request):
    TodoModel.objects.filter(completed__exact=True).delete()
    return redirect('index')
