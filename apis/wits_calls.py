import requests
import pandas as pd
import os
from pathlib import Path
import logging
import Constants
import json
from datetime import datetime

logging.basicConfig(filename=Constants.BASE_DIR / Path('logs.log'), level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# WITS API Configuration
WITS_BASE_URL = "https://wits.worldbank.org/API/V1/SDMX/V21/rest/data"
WITS_AUTH_URL = "https://wits.worldbank.org/API/V1/SDMX/V21/rest/auth"

# You need to replace these with your actual WITS API credentials
WITS_USERNAME = "hakima.merzayee3@gmail.com"
WITS_PASSWORD = "UmY@HujXXqr7Dyr"

# Gold-related HS codes (6-digit)
GOLD_CODES = ['710811', '710812', '710813', '710820', '284330']

# Country codes
ALGERIA_CODE = 'DZA'
BURKINA_FASO_CODE = 'BFA'

def get_wits_token():
    """
    Get authentication token from WITS API
    """
    try:
        # Create a session
        session = requests.Session()
        
        # First, get the login page to get any necessary cookies
        login_url = "https://wits.worldbank.org/login"
        session.get(login_url)
        
        # Now perform the login
        auth_data = {
            'username': WITS_USERNAME,
            'password': WITS_PASSWORD,
            'submit': 'Login'
        }
        
        # Make the login request
        response = session.post(login_url, data=auth_data)
        response.raise_for_status()
        
        # Get the API token
        token_url = "https://wits.worldbank.org/API/V1/SDMX/V21/rest/token"
        token_response = session.get(token_url)
        token_response.raise_for_status()
        
        return token_response.json()['token']
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        logging.exception("Error getting WITS authentication token")
        raise

def process_wits_response(data):
    """
    Process WITS API response and convert to DataFrame
    """
    try:
        # Extract observations from the response
        observations = []
        for obs in data['data']['dataSets'][0]['series']:
            for period, value in obs['observations'].items():
                observation = {
                    'year': period,
                    'value': value[0] if value[0] is not None else 0,
                    'product_code': obs['dimensions']['product'][0],
                    'flow_type': obs['dimensions']['flow'][0]
                }
                observations.append(observation)
        
        # Convert to DataFrame
        df = pd.DataFrame(observations)
        
        # Add product descriptions
        product_map = {
            '710811': 'Gold (including gold plated with platinum) unwrought or in semi-manufactured forms, or in powder form',
            '710812': 'Gold (including gold plated with platinum) in unwrought forms',
            '710813': 'Gold (including gold plated with platinum) in semi-manufactured forms',
            '710820': 'Gold (including gold plated with platinum) in powder form',
            '284330': 'Gold compounds'
        }
        df['product_description'] = df['product_code'].map(product_map)
        
        return df
    except Exception as e:
        logging.exception("Error processing WITS API response")
        raise

def get_wits_data(country_code, country_name, flow_type='import'):
    """
    Fetch trade data from WITS API for a specific country
    
    @param country_code: ISO3 country code
    @param country_name: Name of the country (for file naming)
    @param flow_type: 'import' or 'export'
    @returns: DataFrame containing the trade data
    """
    try:
        # Check if local data exists
        file_name = f"{country_name}_{flow_type}_wits.csv"
        file_path = Path(Constants.DATASET_DIR) / file_name
        
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(f'Found local data for {country_name}')
            return df

        # Get authentication token
        token = get_wits_token()
        
        # Prepare headers with authentication
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        # Prepare parameters for WITS API
        params = {
            'dataflow': 'TRADE_STATS',
            'key': 'TRD_VAL_MRD_HS6',  # Trade value in USD
            'startPeriod': '2015',
            'endPeriod': str(datetime.now().year),
            'dimensionAtObservation': 'AllDimensions',
            'format': 'json'
        }

        # Add country-specific parameters
        params['reporter'] = country_code
        params['partner'] = 'WLD'  # World as partner
        params['product'] = ','.join(GOLD_CODES)
        params['flow'] = 'M' if flow_type == 'import' else 'X'

        # Make API request
        response = requests.get(WITS_BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        
        # Process the response and convert to DataFrame
        data = response.json()
        df = process_wits_response(data)
        
        # Save to CSV
        df.to_csv(file_path, index=False)
        print(f'Fetched data from WITS API for {country_name}')
        
        return df

    except Exception as e:
        logging.exception(f"Error in function: get_wits_data for {country_name}")
        return None

def get_import_data(country_code, country_name):
    """
    Get import data for a specific country
    """
    return get_wits_data(country_code, country_name, 'import')

def get_export_data(country_code, country_name):
    """
    Get export data for a specific country
    """
    return get_wits_data(country_code, country_name, 'export')

# Example usage
if __name__ == "__main__":
    # For Algeria
    algeria_imports = get_import_data(ALGERIA_CODE, 'algeria')
    algeria_exports = get_export_data(ALGERIA_CODE, 'algeria')

    # For Burkina Faso
    burkina_imports = get_import_data(BURKINA_FASO_CODE, 'burkina_faso')
    burkina_exports = get_export_data(BURKINA_FASO_CODE, 'burkina_faso') 