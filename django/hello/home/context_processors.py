from home.models import Category


def add_variable_to_context(request):
    categorys = Category.objects.values()
    return {'categorys': categorys}
