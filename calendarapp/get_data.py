import pandas as pd
from calendarapp.models import Flight

data = pd.read_csv('data/Flights.csv', sep=',', header=0)

# year,month,day,dep_time,dep_delay,arr_time,arr_delay,cancelled,
# carrier,tailnum,flight,origin,dest,air_time,distance,hour,min



data = data.applymap(str)
data['month'] = data['month'].str.pad(2,side='left',fillchar='0')
data['day'] = data['day'].str.pad(2,side='left',fillchar='0')
data['date'] = data[['year', 'month', 'day']].apply(lambda x: ''.join(x), axis=1)
data['date'] = pd.to_datetime(data['date'])
data['dep_time'] = data['dep_time'].str.pad(4,side='left',fillchar='0')
data['dep_time'] = pd.to_datetime(data['dep_time'], format='%H%M',errors='coerce').dt.time
data['dep_delay'] = data['dep_delay'].astype(int)
data['dep_delay'] = pd.to_timedelta(data['dep_delay'], unit='m', errors='coerce')
data['arr_time'] = data['arr_time'].str.pad(4,side='left',fillchar='0')
data['arr_time'] = pd.to_datetime(data['arr_time'], format='%H%M',errors='coerce').dt.time
data['arr_delay'] = data['arr_delay'].astype(int)
data['arr_delay'] = pd.to_timedelta(data['arr_delay'], unit='m', errors='coerce')
data['flight'] = data['flight'].astype(int)
data['air_time'] = data['air_time'].astype(int)
data['air_time'] = pd.to_timedelta(data['air_time'], unit='m', errors='coerce')
data['distance'] = data['distance'].astype(int)
data['duration'] = data[['hour', 'min']].apply(lambda x: ''.join(x), axis=1).str.pad(4,side='left',fillchar='0')
data['duration'] = data['duration'].astype(int)
data['duration'] = pd.to_timedelta(
    (data['duration']//100)*60 + (data['duration'] % 100), unit='m',
    errors='coerce')
# data['duration'] = pd.to_timedelta(data['duration'])
data = data.drop(['year', 'month', 'day', 'hour', 'min'], axis=1)
cols = ['date', 'dep_time', 'dep_delay', 'arr_time',
        'arr_delay', 'cancelled', 'carrier',
        'tailnum', 'flight', 'origin',
        'dest', 'air_time', 'distance', 'duration']
data = data.reindex(columns=cols)
print(data.tail())
#
def timeStrFormat(time):

    time = str(time)

    newTime = time[:-2] + ':' + time[-2:]

    return newTime

flights = [
    Flight(
        date = data.iloc[row].loc['date'],
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
        duration = data.iloc[row].loc['duration'],
    )
    for row, _ in enumerate(data)
]
for f in flights: f.save()
