from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict

from main.models.person import Person
from ron.web import Controller
from ron import request, response


class API(Controller):

    # sets a base route for this controller
    base_route = '/api'

    @Controller.route('/', method='GET')
    def index(self):
        """
        Just returns the "index" text on the base api url
        """
        return dict(data='index')

    @Controller.route('/person', method='GET')
    def get_persons(self):
        """
        Get all Persons
        """
        result = Person.select().dicts()
        return dict(name='Person', data=list(result))

    @Controller.route('/person', method='POST')
    def add_person(self):
        """
        Insert a new Person
        """
        data = dict(request.forms)
        pp = Person(**data)
        if pp.validate():
            pp.save()
            data = model_to_dict(pp)
        else:
            data = pp.validator().errors
        return dict(name='Person', data=data)

    @Controller.route('/person/<id:int>', method='GET')
    def get_person(self, id):
        """
        Return a person by id
        """
        try:
            person = Person.get(Person.id == id)
            data = model_to_dict(person)
        except DoesNotExist:
            response.status = 404
            data = "Not found"
        return dict(name='Person', data=data)

    @Controller.route('/person/<id:int>', method='PUT')
    def update_person(self, id):
        """
        Update a Person
        """
        person = Person.get(Person.id == id)
        form_data = dict(request.forms)
        if person.validate(form_data):
            person.update_model(form_data)
            person.save()
            data = model_to_dict(person)
        else:
            data = person.validator().errors
        return dict(name='Person', data=data)

    @Controller.route('/person/<id:int>', method='DELETE')
    def delete_person(self, id):
        """
        Delete a person
        """
        data = Person.delete().where(Person.id == id).execute()
        return dict(name='Person', data=data)
