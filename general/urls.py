from general.views import homepage, about, property_grid, blog_grid, blog_single, pages, contact, agents_grid, agent_single, property_single
from django.urls import path

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about', about, name='about'),
    path('property',property_grid, name='property'),
    path('property/single',property_single, name='property_single'),
    path('blog/grid',blog_grid, name='blog'),
    path('blog/single',blog_single, name='blog_single'),
    path('pages',pages, name='pages'),
    path('contact',contact, name='contact'),
    path('agents/grid',agents_grid, name='agents_grid'),
    path('agent/single',agent_single, name='agent_single'),

]
