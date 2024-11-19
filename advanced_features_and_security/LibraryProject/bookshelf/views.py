from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.


# Views
@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_post(request):
    return render(request, 'your_app_name/edit_post.html')

@permission_required('your_app_name.can_create', raise_exception=True)
def create_post(request):
    return render(request, 'your_app_name/create_post.html')

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_post(request):
    return render(request, 'your_app_name/delete_post.html')

@permission_required('your_app_name.can_view', raise_exception=True)
def view_post(request):
    return render(request, 'your_app_name/view_post.html')
