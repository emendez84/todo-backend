from flask import request
from flask_restful.reqparse import Namespace

def paginated_results(query):
    pagination = request.args.get('pagination', 'true', str)
    jsondepth = request.args.get('jsondepth', 1, int)
    if pagination == 'true':
        paginated = query.paginate(page=request.args.get('page', 1, int))
        return {
            'page': paginated.page,
            'pages': paginated.pages,
            'items': [x.json(jsondepth) if jsondepth else x.json() for x in paginated.items]
        }
    else:
        return [x.json(jsondepth) if jsondepth else x.json() for x in query.all()]

# Utility function to only execute and assigment to an object if the value from a reqparse.Namespace dict is not None
def _assign_if_something(obj: object, newdata: Namespace, key: str):
    value = newdata.get(key)
    if value is not None:
        obj.__setattr__(key, value)