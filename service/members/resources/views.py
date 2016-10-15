from flask import request, jsonify
from flask.ext.restplus import Resource

from service import api_v1
from service.members import queries
from service.members.models import *


class GenericAuxModelList(Resource):
    cls = None

    def get(self):
        result = queries.get_all(self.cls)
        return jsonify({self.cls.__name__: result})

    @api_v1.response(201, 'Item successfully created.')
    def post(self):
        payload = request.get_json()
        result = queries.add_aux_model(self.cls, payload)
        return result.serialize, 201


class GenericAuxModelViewItem(Resource):
    cls = None

    def get(self, obj_id):
        result = queries.get_aux_model_by_id(self.cls, obj_id)
        return jsonify(result.serialize) if result else None


@api_v1.route('/members/', endpoint='members')
class MemberList(Resource):
    def get(self):
        payload = request.args
        return jsonify({'members':  queries.get_members(payload)})


@api_v1.route('/members/<int:obj_id>', endpoint='member')
class MemberItem(Resource):
    def get(self, obj_id):
        pass

    def put(self, obj_id):
        pass


@api_v1.route('/educations/', endpoint='educations')
class EducationList(GenericAuxModelList):
    cls = Education


@api_v1.route('/educations/<int:obj_id>', endpoint='education')
class EducationItem(GenericAuxModelViewItem):
    cls = Education


@api_v1.route('/visas/', endpoint='visas')
class VisaList(GenericAuxModelList):
    cls = Visa


@api_v1.route('/visas/<int:obj_id>', endpoint='visa')
class VisaItem(GenericAuxModelViewItem):
    cls = Visa


@api_v1.route('/courses/', endpoint='courses')
class CourseList(GenericAuxModelList):
    cls = Course


@api_v1.route('/courses/<int:obj_id>', endpoint='course')
class CourseItem(GenericAuxModelViewItem):
    cls = Course


@api_v1.route('/occupations/', endpoint='occupations')
class OccupationAreaList(GenericAuxModelList):
    cls = OccupationArea


@api_v1.route('/occupations/<int:obj_id>', endpoint='occupation')
class OccupationAreaItem(GenericAuxModelViewItem):
    cls = OccupationArea


@api_v1.route('/technologies/', endpoint='technologies')
class TechnologyList(GenericAuxModelList):
    cls = Technology


@api_v1.route('/technologies/<int:obj_id>', endpoint='technology')
class TechnologyItem(GenericAuxModelViewItem):
    cls = Technology


@api_v1.route('/genders/', endpoint='genders')
class GenderList(GenericAuxModelList):
    cls = Gender


@api_v1.route('/genders/<int:obj_id>', endpoint='gender')
class GenderItem(GenericAuxModelViewItem):
    cls = Gender


@api_v1.route('/experiences/', endpoint='experiences')
class ExperienceTimeList(GenericAuxModelList):
    cls = ExperienceTime


@api_v1.route('/experiences/<int:obj_id>', endpoint='experience')
class ExperienceTimeItem(GenericAuxModelViewItem):
    cls = ExperienceTime
