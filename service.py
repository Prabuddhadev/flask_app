import os
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import numpy as np


class ConstructionData:
    def __init__(self):
        self.base_file_path = os.path.join('export29913.xlsx')

    def get_supplier_data(self):
        construction_data = pd.read_excel('export29913.xlsx')
        suppliers = construction_data['Supplier'].dropna().replace({np.nan: None}).to_list()
        return {
            'Supplier': list(set(suppliers))
        }

    def purchase_orders(self, supplier):
        construction_data = pd.read_excel('export29913.xlsx')
        construction_data['Supplier'].ffill(inplace=True)
        po_numbers = construction_data[
            construction_data['Supplier'] == supplier]['PO Number'].replace({np.nan: None}).to_list()
        return {
            'purchase_order_details': list(set(po_numbers))
        }

    def get_po_details(self, purchase_ordr_num):
        construction_data = pd.read_excel('export29913.xlsx')
        construction_data['Supplier'].ffill(inplace=True)
        po_details = construction_data[
            construction_data['PO Number'] == purchase_ordr_num]['Description'].replace({np.nan: None}).to_list()
        return {
            'po_number': purchase_ordr_num,
            'description': po_details
        }

    def save_data(self, data):

        uri = "mongodb+srv://prabuddhakumardwivedi:Samplepoc@cluster0.a0lgvvr.mongodb.net/?retryWrites=true&w=majority"
        data['description'] = data['description'][0].split(', ')
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['parshva']
        user_collection = db['user_data']
        result = user_collection.insert_one(data)
        if result.acknowledged:
            success = True
        else:
            success = False
        client.close()
        return {
            'success': success
        }
