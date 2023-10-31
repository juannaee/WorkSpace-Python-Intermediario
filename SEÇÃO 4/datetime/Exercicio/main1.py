from datetime import datetime
from dateutil.relativedelta import relativedelta


loan_price = 500_000
loan_date = datetime(2020, 1, 1)
quantity_parcels = relativedelta(days=365 * 5)
loan_final_date = loan_date + quantity_parcels


list_parcels = []
parcerls = loan_date

while parcerls < loan_final_date:
    list_parcels.append(parcerls)
    parcerls += relativedelta(months=1)
