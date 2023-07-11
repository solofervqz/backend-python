from flask.views import MethodView
from flask import Blueprint, request

categories_blueprint = Blueprint("categories_blueprint", __name__,url_prefix='/api/')

class CategoriesList(MethodView):
    def get(self):
        return [{"cat": "Estudiante"},{"cat": "Desarrollador"}]
                
class Categories(MethodView):
    def post(self):
        data = request.get_json()
        cat = data.get('cat')

        if cat is None:
            return{"message:" "No has ingresado tu categoria."},400
        
        return
    
class Categoriesview(MethodView):
    def get(self):
        data = request.get_json()
        cat = data.get('id')
        

        return CategoriesList[cat]
        
categories_blueprint.add_url_rule(
    'categories',
    view_func=CategoriesList.as_view("categories_list")
)

categories_blueprint.add_url_rule(
    'categories',
    view_func=Categories.as_view("categories")
)

categories_blueprint.add_url_rule(
    'categories',
    view_func=Categoriesview.as_view("categories_view")
)