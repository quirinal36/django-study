from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import Feed

class Index(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'
    
    def get(self, request):        
        feeds = Feed.objects.all().order_by("id")

        return render(
            request, 
            self.template_name,
            {'feed_list' : feeds}
            )

class NewContent(View):
    template_name = 'upload_form.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        param = request.POST.get('content', '')
        param2 = request.FILES.get('up_photo', False)

        print(param)
        feed = Feed(content=param, photo = param2)
        feed.save()

        return redirect('edu:tag_study')