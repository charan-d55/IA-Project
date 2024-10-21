from django.shortcuts import render

# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Type, Item
from datetime import datetime
from django.views import View


# Create your views here.
def index(request):
    type_list = Type.objects.all().order_by('id')
    response = HttpResponse()
    heading1 = '<p>' + 'Different Types: ' + '</p>'
    response.write(heading1)
    for type in type_list:
        para = '<p>' + str(type.id) + ': ' + str(type) + '</p>'
        response.write(para)
    return response

# New function for about page
def about(request, year, month):
    try:
        date = datetime(year, month, 1)  # Create a date object
        month_name = date.strftime("%B")  # Get the full month name
        return HttpResponse(f"This is an Online Grocery Store. You entered: {month_name} {year}.")
    except ValueError:
        return HttpResponse("Invalid date.")

# New function for detail view of items based on type
def detail(request, type_no):
    type_obj = get_object_or_404(Type, id=type_no)
    items = Item.objects.filter(type=type_obj).order_by('-price')[:10]  # Limit to 10 items, sorted by price
    response = HttpResponse()
    heading = f'<p>Items for {type_obj.name}:</p>'
    response.write(heading)
    for item in items:
        para = f'<p>{item.name}: ${item.price}</p>'
        response.write(para)
    return response

def greet(request):
    return HttpResponse("Hello, welcome to the Grocery Store!")

class GreetView(View):
    def get(self, request):
        return HttpResponse("Hello, welcome to the Grocery Store!")


# Differences between Function-Based View (FBV) and Class-Based View (CBV):
# 1. **Structure**: FBVs are defined as simple functions, while CBVs are defined as classes inheriting from Django's View class.
# 2. **HTTP Method Handling**: In FBVs, you handle HTTP methods like GET and POST in a single function. In CBVs, you define separate methods (e.g., `get`, `post`) for each HTTP method, promoting better organization.
# 3. **Reusability**: CBVs allow for code reuse through inheritance and mixins. You can create a base view and extend it, which isn't as straightforward with FBVs.
# 4. **Routing**: With CBVs, you can utilize Django's built-in class-based mixins, which can help you manage common patterns (like form handling) more easily.
# 5. **Complexity**: For simple views, FBVs are often simpler and easier to understand. For more complex views that require different handling for multiple methods or additional features, CBVs offer a more structured approach.
