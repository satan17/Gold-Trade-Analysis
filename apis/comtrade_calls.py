import comtradeapicall
import pandas as pd
import os
from pathlib import Path
import logging

import Constants

logging.basicConfig(filename= Constants.BASE_DIR / Path('logs.log'), level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

subscription_key = '0fbbfac85565439baf8f361e349e8d03'
cc_algeria = 12 # M49 country code for Algeria
cc_burkina_faso = 854 # M49 country code for Burkina Faso
time_period = '2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025'
commodity_codes = '284330,710820,710811,710812,710813' # all form of gold and it's compounds
import_types = 'm,fm,mip,mop,rm' # all kind of imports
export_types = 'x,dx,rx,xip,xop' # all kind of exports


'''
    This function get all form of gold and it's compounds export data from a country
    
    
    @:param country_code = specify M49 code for the desired country
    @:param country_name = specify country name (_ delimited)
    
    @:returns = A dataframe consists of all the parameters
'''

def get_export_data(country_code, country_name):
    try:
        if os.path.exists(Path(Constants.DATASET_DIR) / Path(str(country_name) + '_export_comtrade' + '.csv')):
            df = pd.read_csv(Path(Constants.DATASET_DIR) / Path(str(country_name) + '_export_comtrade' + '.csv'))
            print('found local data for ', country_name)
        else:
            df = comtradeapicall.getFinalData(subscription_key=subscription_key, typeCode='C', freqCode='A', clCode='HS',
                                           period=time_period, reporterCode='', cmdCode=commodity_codes,
                                           flowCode=export_types, partnerCode=country_code, partner2Code=0,
                                           customsCode=None, motCode=None, maxRecords=50000, format_output='JSON',
                                           aggregateBy=None, breakdownMode='plus', countOnly=None, includeDesc=True)
            # saving file on disk to avoid repeated calls
            df.to_csv(Path(Constants.DATASET_DIR) / Path(str(country_name) + '_export_comtrade' + '.csv'), index=False)
            print('fetched data from API for ', country_name)
        return df
    except Exception as e:
        logging.exception("Error in function : get_export_data")
        # print('some internal error occurred')


'''
    This function get all form of gold and it's compounds import data to a country


    @:param country_code = specify M49 code for the desired country
    @:param country_name = specify country name (_ delimited)

    @:returns = A dataframe consists of all the parameters
'''

def get_import_data(country_code, country_name):
    try:
        if os.path.exists(Path(Constants.DATASET_DIR) /Path(str(country_name) + '_import_comtrade' + '.csv')):
            df = pd.read_csv(Path(Constants.DATASET_DIR) / Path(str(country_name) + '_import_comtrade' + '.csv'))
            print('found local data for ', country_name)
        else:
            
            df = comtradeapicall.getFinalData(subscription_key=subscription_key, typeCode='C', freqCode='A', clCode='HS',
                                              period=time_period, reporterCode='', cmdCode=commodity_codes,
                                              flowCode=import_types, partnerCode=country_code, partner2Code=0,
                                              customsCode=None, motCode=None, maxRecords=50000, format_output='JSON',
                                              aggregateBy=None, breakdownMode='plus', countOnly=None, includeDesc=True)
            # saving file on disk to avoid repeated calls
            df.to_csv(Path(Constants.DATASET_DIR) / Path(str(country_name) + '_import_comtrade' + '.csv'), index=False)
            print('fetched data from API for ', country_name)
        return df
    except Exception as e:
        logging.exception("Error in function : get_import_data")
        # print('some internal error occurred')

