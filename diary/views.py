from django.views import generic

# Create your views here.
#トップページ用のビュー
class IndexView(generic.TemplateView):
    template_name = "index.html"