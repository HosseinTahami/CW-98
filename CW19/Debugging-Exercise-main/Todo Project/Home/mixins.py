from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.core.exceptions import PermissionDenied

class TodoMixin:
    form_class = TodoForm
    template_name = 'Home/todo_detail.html'

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        if not todo.user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
        

    def get(self, request, pk):
        todo = Todo.objects.filter(id=pk)
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
