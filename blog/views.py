from django.views import generic
from .forms import InquiryForm

class BlogView(generic.TemplateView):
    template_name = "blog_index.html"

class BlogInquiryView(generic.FormView):
    template_name = "blog_inquiry.html"
    form_class = InquiryForm