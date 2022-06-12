from django.urls import path
from graphene_django.views import GraphQLView
from product.schema import schema
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
     path(
        route='graphql',
        view=csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('listProduct',views.getProduct,name='getproduct'),
    
]