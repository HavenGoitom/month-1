from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm, TodoSearchForm

def todo_list(request):
    # Handle adding a new task via POST
    if request.method == 'POST':
        add_form = TodoItemForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('todo_list')
    else:
        add_form = TodoItemForm()

    # Handle searching via GET (using 'query' as the GET parameter)
    search_query = request.GET.get('query', '')
    if search_query:
        todos = TodoItem.objects.filter(title__icontains=search_query)
    else:
        todos = TodoItem.objects.all()

    # Create search form instance (pre-populated with the query)
    search_form = TodoSearchForm(initial={'query': search_query})

    context = {
        'todos': todos,
        'add_form': add_form,
        'search_form': search_form,
    }
    return render(request, 'myapp/todo_list.html', context)

def toggle_complete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_task(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
