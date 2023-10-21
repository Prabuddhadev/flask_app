import os
from datetime import datetime

import pandas as pd
import numpy as np


class ConstructionData:
    def __init__(self):
        self.base_file_path = os.path.join('export29913.xlsx')

    def get_supplier_data(self):
        construction_data = pd.read_excel('export29913.xlsx')
        suppliers = construction_data['Supplier'].dropna().replace({np.nan: None}).to_list()
        return {
            'Supplier': suppliers
        }

    def purchase_orders(self, supplier):
        construction_data = pd.read_excel('export29913.xlsx')
        construction_data['Supplier'].ffill(inplace=True)
        po_numbers = construction_data[
            construction_data['Supplier'] == supplier]['PO Number'].replace({np.nan: None}).to_list()
        return {
            'purchase_order_details': po_numbers
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

        data['description'] = data['description'][0].split(', ')
        max_length = max(len(data[key]) for key in data)
        # Fill shorter columns with NaN (null)
        data = {key: data[key] + [''] * (max_length - len(data[key])) for key in data}
        # Create the DataFrame
        df = pd.DataFrame(data)
        # Replace empty strings with NaN
        df = df.replace('', np.nan)
        print(data)
        folder_path = os.path.join(os.getcwd(), 'User_data')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        path = os.path.join(os.getcwd(), 'User_data', f"{df['name'][0].lower().replace(' ', '')}_{df['po_number'][0].replace('/', '_')}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
        print(path)
        df.to_csv(path, index=False)
        return {
            'success': True
        }