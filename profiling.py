import pandas as pd
#df = import your data in any format
#pip install ydata-profiling
from ydata_profiling import ProfileReport
report = ProfileReport(df)
report.to_file(output_file='output_name_given_to_your_dataset_report.html')
