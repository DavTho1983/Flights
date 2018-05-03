import pandas as pd
from calendarapp.models import Flight

data = pd.read_csv('data/Flights.csv', sep=',', header=0)

# year,month,day,dep_time,dep_delay,arr_time,arr_delay,cancelled,
# carrier,tailnum,flight,origin,dest,air_time,distance,hour,min

# print(data.head())
flights = [
    Flight(
        year = data.iloc[row].loc['year'],
        month = data.iloc[row].loc['month'],
        day = data.iloc[row].loc['day'],
        dep_time = data.iloc[row].loc['dep_time'],
        dep_delay = data.iloc[row].loc['dep_delay'],
        arr_time = data.iloc[row].loc['arr_time'],
        arr_delay = data.iloc[row].loc['arr_delay'],
        cancelled = data.iloc[row].loc['cancelled'],
        carrier = data.iloc[row].loc['carrier'],
        tailnum = data.iloc[row].loc['tailnum'],
        flight = data.iloc[row].loc['flight'],
        origin = data.iloc[row].loc['origin'],
        dest = data.iloc[row].loc['dest'],
        air_time = data.iloc[row].loc['air_time'],
        distance = data.iloc[row].loc['distance'],
        hour = data.iloc[row].loc['hour'],
        min = data.iloc[row].loc['min'],
    )
    for row, _ in enumerate(data)
]
for f in flights: f.save()
