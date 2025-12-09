import pandas as pd

# data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")
# data = pd.DataFrame({
#     'Date': ['11/8/2011', '04/23/2008', '10/2/2019'],
#     'Event': ['Music', 'Poetry', 'Theatre'],
#     'Cost': [10000, 5000, 15000]
# })
# print("Before Conversion:")
# print(data.info())
# data['Date'] = pd.to_datetime(data['Date'])

# print("\nAfter Conversion:")
# print(data.info())


#Converting from 'yymmdd' Format
patientData = pd.DataFrame({
    'Date': ['200712', '200714', '200716', '200719'],
    'Patients': [50000, 51000, 51500, 53000]
})

print(patientData.dtypes)
patientData['Date'] = pd.to_datetime(patientData['Date'], format='%y%m%d')
print("After Conversion:\n")
print(patientData.dtypes)