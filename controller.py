from flask_restful import Resource, request, abort
from service import ConstructionData


class ConstructionDataController(Resource):
    def get(self, vars):
        if vars == 'suppliers':
            return ConstructionData().get_supplier_data()
        else:
            abort(404, message='URL does not exist')

    def post(self, vars):
        params = request.get_json()
        if vars == 'po_details':
            return ConstructionData().purchase_orders(params['supplier'])
        elif vars == 'po_disc':
            return ConstructionData().get_po_details(params['purchase_ordr_num'])
        elif vars == 'submit':
            return ConstructionData().save_data(params['data'])
        else:
            abort(404, message='URL does not exist')
