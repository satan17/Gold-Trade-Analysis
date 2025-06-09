from apis import comtrade_calls
from apis.comtrade_calls import get_export_data, get_import_data

algeria_export_data = get_export_data(comtrade_calls.cc_algeria, 'Algeria')
burkina_export_data = get_export_data(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')
algeria_import_data = get_import_data(comtrade_calls.cc_algeria, 'Algeria')
burkina_import_data = get_import_data(comtrade_calls.cc_burkina_faso, 'Burkina_Faso')

print(algeria_export_data)
# print(burkina_export_data)
# print(algeria_import_data)
# print(burkina_import_data)