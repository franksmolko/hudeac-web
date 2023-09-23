def template_list(request):
    templates = ['home', 'air', 'gallery', 'mission', "email"]
    return {'templates': templates}