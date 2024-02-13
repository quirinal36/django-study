from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect


class Index(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)

class Result(View):

    def get(self, request):
        
        my_type = request.GET.get('type', None)
        print(f'my_type:{my_type}')
        template_name = f'result/{my_type}.html'
        return render(request, template_name=template_name)