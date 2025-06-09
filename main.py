from apis import comtrade_calls
from apis.comtrade_calls import get_export_data, get_import_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

algeria_export_data = get_export_data(comtrade_calls.cc_algeria, 'Algeria')
burkina_export_data = get_export_data(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')
algeria_import_data = get_import_data(comtrade_calls.cc_algeria, 'Algeria')
burkina_import_data = get_import_data(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')
