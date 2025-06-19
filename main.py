from apis import comtrade_calls, wits_calls
from apis.comtrade_calls import get_export_data as get_comtrade_export, get_import_data as get_comtrade_import
from apis.wits_calls import get_export_data as get_wits_export, get_import_data as get_wits_import
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_all_data():
    try:
        logger.info("Starting data fetch from Comtrade API...")
        # Fetch Comtrade data
        algeria_export_comtrade = get_comtrade_export(comtrade_calls.cc_algeria, 'Algeria')
        burkina_export_comtrade = get_comtrade_export(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')
        algeria_import_comtrade = get_comtrade_import(comtrade_calls.cc_algeria, 'Algeria')
        burkina_import_comtrade = get_comtrade_import(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')
        logger.info("Comtrade data fetch completed successfully")

        print("Starting data fetch from WITS API...")
        # Fetch WITS data
        algeria_export_wits = get_wits_export(wits_calls.ALGERIA_CODE, 'algeria')
        burkina_export_wits = get_wits_export(wits_calls.BURKINA_FASO_CODE, 'burkina_faso')
        algeria_import_wits = get_wits_import(wits_calls.ALGERIA_CODE, 'algeria')
        burkina_import_wits = get_wits_import(wits_calls.BURKINA_FASO_CODE, 'burkina_faso')
        logger.info("WITS data fetch completed successfully")

        return {
            'comtrade': {
                'algeria_export': algeria_export_comtrade,
                'algeria_import': algeria_import_comtrade,
                'burkina_export': burkina_export_comtrade,
                'burkina_import': burkina_import_comtrade
            },
            'wits': {
                'algeria_export': algeria_export_wits,
                'algeria_import': algeria_import_wits,
                'burkina_export': burkina_export_wits,
                'burkina_import': burkina_import_wits
            }
        }
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Fetch all data
        data = fetch_all_data()
        
        # Print summary of fetched data
        logger.info("\nData Summary:")
        logger.info("Comtrade Data:")
        for key, df in data['comtrade'].items():
            if df is not None:
                logger.info(f"{key}: {len(df)} rows")
            else:
                logger.info(f"{key}: No data available")
        
        logger.info("\nWITS Data:")
        for key, df in data['wits'].items():
            if df is not None:
                logger.info(f"{key}: {len(df)} rows")
            else:
                logger.info(f"{key}: No data available")
                
    except Exception as e:
        logger.error(f"Program failed: {str(e)}")
