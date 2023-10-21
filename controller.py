from flask_restful import Resource, request, abort
from service import ConstructionData


class ConstructionDataController(Resource):
    def get(self, vars):
        res = None

        try:
            if vars == 'suppliers':
                res = ConstructionData().get_supplier_data()
            else:
                abort(404, message='URL does not exist')
        except Exception as e:
            print(str(e))
            abort(500, message='Internal server error')
        else:
            return res

    def post(self, vars):
        res = None
        params = request.get_json()
        try:
            if vars == 'po_details':
                res = ConstructionData().purchase_orders(params['supplier'])
            elif vars == 'po_disc':
                res = ConstructionData().get_po_details(params['purchase_ordr_num'])
            elif vars == 'submit':
                res = ConstructionData().save_data(params['data'])
            else:
                abort(404, message='URL does not exist')
        except Exception as e:
            print(str(e))
            abort(500, message='Internal server error')
        else:
            return res
