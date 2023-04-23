from wsgiref.simple_server import make_server
from pyramid.config import Configurator 
from pyramid.view import view_config
from pyramid.renderers import render
from pyramid.response import Response
from benford_check import *
import json

@view_config(route_name="main")
def home(request):
    html = render('view\home.html', {}, request=request)
    return Response(html)

@view_config(route_name="benford", request_method="POST")
def benford(request):
    csvfile = request.POST['csvfile'].file

    data_list = []
    reader = csv.reader(csvfile.read().decode('utf-8').splitlines())
    for row in reader:
        data_list.extend(row)
    # print(data_list[:5])
    # print(len(data_list))

    results, conform = check_benford(data_list)

    if conform==True:
        with open("satisfied_benfords.json", "w") as f:
            json.dump(results, f)
        return Response(json.dumps(results))
    else:
        return Response("Data does not conform to Benford's Law.")


if __name__=="__main__":
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_route('main', '/')
        config.add_route('benford', '/benford')
        config.scan()
        config.add_jinja2_renderer('.html')
        app = config.make_wsgi_app()
        
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
