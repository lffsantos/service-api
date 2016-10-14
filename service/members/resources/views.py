from flask import request, jsonify
from flask.ext.restful import Resource
from service.members import queries
from service.members.models import Education, Visa, Course, OccupationArea, Technology
from service.members.queries import add_aux_model, get_members, add_member


class GenericAuxModelList(Resource):
    cls = None

    def get(self):
        result = queries.get_all(self.cls)
        return jsonify({self.cls.__name__: result})


class GenericAuxModelViewItem(Resource):
    cls = None

    def get(self, obj_id):
        result = queries.get_aux_model_by_id(self.cls, obj_id)
        return jsonify(result.serialize) if result else None

    def put(self, obj_id):
        pass

    def delete(self, obj_id):
        pass

    def post(self):
        payload = request.get_json()
        args = payload.get('args')
        add_aux_model(self.cls, args)
        return jsonify({'ok': 'ok'})


class MemberList(Resource):
    def get(self):
        # payload = request.get_json()
        return jsonify({'members': get_members()})

    def post(self):
        payload = request.get_json()
        args = payload.get('args')
        member = add_member(**args)
        return jsonify(member)


class MemberItem(Resource):
    def get(self, obj_id):
        pass

    def put(self, obj_id):
        pass

    def delete(self, obj_id):
        pass


class EducationList(GenericAuxModelList):
    cls = Education


class EducationItem(GenericAuxModelViewItem):
    cls = Education


class VisaList(GenericAuxModelList):
    cls = Visa


class VisaItem(GenericAuxModelViewItem):
    cls = Visa


class CourseList(GenericAuxModelList):
    cls = Course


class CourseItem(GenericAuxModelViewItem):
    cls = Course


class OccupationAreaList(GenericAuxModelList):
    cls = OccupationArea


class OccupationAreaItem(GenericAuxModelViewItem):
    cls = OccupationArea


class TechnologyList(GenericAuxModelList):
    cls = Technology


class TechnologyItem(GenericAuxModelViewItem):
    cls = Technology
