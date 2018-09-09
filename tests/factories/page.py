import factory
from django.utils.text import slugify
from wagtail_factories.factories import PageFactory

from tests.site.pages.models import ContentPage


class ContentPageFactory(PageFactory):
    parent = None
    title = "Test page"
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))

    class Meta:
        model = ContentPage
