from models.task import TaskModel
from flask_restful import Resource,reqparse
from flasgger import swag_from

from utils import paginated_results


class Task(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id',type=int)
    parser.add_argument('descrip', type = str)
    parser.add_argument('status', type=str)

    @swag_from('../swagger/task/get_task.yaml')
    def get(self, id):
        tarea = TaskModel.find_by_id(id)
        if tarea:
            return tarea.json()
        return {'message':'No se encuentra la Tarea'},404

    # def put(self, id):
    
    # def delete(self, id):

class TaskList(Resource):
    @swag_from('../swagger/task/list_task.yaml')
    def get(self):
        query = TaskModel.query
        return paginated_results(query)

    # def post(self):

# class TaskSearch(Resource):
    # def post(self):