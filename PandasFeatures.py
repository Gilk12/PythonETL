import pandas as pd


flights_data = pd.read_csv("csv/flights.csv")

flights_data['date'] = pd.to_datetime(flights_data['date'])
flights_mask = flights_data['date'].between('2020-04-01', 'now')
filtered_flights_data = flights_data[flights_mask]

users_data = pd.read_csv("csv/users.csv")
users_gender_mask = (users_data['gender'] == 'female') & (users_data['age'] > 35)

users_mask = users_gender_mask
filtered_users_data = users_data[users_mask]

hotels_data = pd.read_csv("csv/hotels.csv")

print(flights_data[flights_mask])

print(users_data[users_mask])

merge_data = pd.merge(filtered_flights_data, filtered_users_data, left_on='userCode', right_on='code', how='inner')

merge_data = pd.merge(merge_data, hotels_data, on='travelCode', how='inner')

merge_data.to_csv("out")
print(merge_data)
# print(filtered_flights_data['userCode'].merge(filtered_users_data['code'], how='cross'))