import numpy as np, pandas as pd

sample_data = pd.read_csv('C:/Users/SESA627676/Downloads/sample_timeseries_data.txt', sep=',', index_col=0, parse_dates=True, squeeze=True)

from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np, pandas as pd

class removeOutliers:
    def __init__(self, data_series, model, period):
        self.data_series = np.array(data_series)
        self.model = model
        self.period = period

    def calculate(self):
        pass

sample_data = pd.read_csv("C:/Users/SESA627676/Box/School of DataScience - Internal/SDS L2 - Final/Session 4 - Time Series/Session content/AirPassengers.csv")
data_series = list(sample_data['#Passengers'])
decompose_ts_add = seasonal_decompose(data_series, model = "additive", period = 12, extrapolate_trend='freq')
trend = decompose_ts_add.trend
# print(trend)
seasonal = decompose_ts_add.seasonal
# print()
# print(seasonal)
resid = decompose_ts_add.resid
# print()
print(resid)
q1_resid = np.percentile(resid, 25)
q3_resid = np.percentile(resid, 75)
iqr = q3_resid - q1_resid
element_list = []
for index, r in enumerate(resid):
    if (r < (q1_resid - (3 * iqr))) | (r > (q3_resid + (3 * iqr))):
        element_list.append(index)
print(min(resid), max(resid))
print(q1_resid, q3_resid)
print(iqr)
print(q1_resid - (2 * iqr))
print(q3_resid + (2 * iqr))
print(element_list)