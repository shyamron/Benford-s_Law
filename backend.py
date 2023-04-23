from wsgiref.simple_server import make_server
from pyramid.config import Configurator 
from pyramid.view import view_config
from pyramid.renderers import render
from pyramid.response import Response
from benford_check import *
import json
import uuid

@view_config(route_name="main")
def home(request):
    html = render('view\home.html', {}, request=request)
    return Response(html)

@view_config(route_name="upload", request_method="POST")
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
        file_location = f"json/{uuid.uuid1()}file.json"
        with open(file_location, "w+") as f:
            json.dump(results, f)
        return Response("Data conforms to Benford's Law. Check the JSON file for more details.")
    else:
        return Response("Data does not conform to Benford's Law.")


if __name__=="__main__":
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_route('main', '/benford')
        config.add_route('upload', '/upload')
        config.scan()
        config.add_jinja2_renderer('.html')
        app = config.make_wsgi_app()
        
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
