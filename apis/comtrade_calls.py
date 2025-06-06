import pandas
import requests
import comtradeapicall
from datetime import date
from datetime import timedelta

subscription_key = '0fbbfac85565439baf8f361e349e8d03'
output_dir = 'downloaded'

today = date.today()
yesterday = today - timedelta(days=1)
lastweek = today - timedelta(days=7)

mydf = comtradeapicall.previewFinalData(typeCode='C', freqCode='M', clCode='HS', period='202205',
                                        reporterCode='36', cmdCode='91', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=5, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)

print(mydf.columns)
print(mydf.head(5))