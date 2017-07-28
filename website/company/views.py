from django.shortcuts import render
from company.forms import Contact_form


# Create your views here.
def about_us(request):
    return render(request, 'company/about_us.html')

def customers(request):
    return render(request, 'company/customers.html')

def contact(request):
    form = Contact_form()

    if request.method == "POST":
        form = Contact_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return index(request)
        else:
            print("Error from invalid")

    return render(request, 'company/contact.html', {'contact_form': form})
