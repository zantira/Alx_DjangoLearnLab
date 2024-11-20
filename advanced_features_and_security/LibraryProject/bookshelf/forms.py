from django import forms

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100)

# In the view
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['example_field']
            # Process data
