import pandas as pd
from calendarapp.models import Flight

data = pd.read_csv('data/Flights.csv', sep=',', header=0)

# year,month,day,dep_time,dep_delay,arr_time,arr_delay,cancelled,
# carrier,tailnum,flight,origin,dest,air_time,distance,hour,min



data = data.applymap(str)
data['date'] = data[['month', 'day', 'year']].apply(lambda x: '/'.join(x), axis=1)
data['date'] = pd.to_datetime(data['date'],infer_datetime_format=True)
data['dep_time'] = pd.to_datetime(data['dep_time'].str.pad(4,side='left',fillchar='0'),format='%H%M',errors='coerce').dt.time
data['arr_time'] = pd.to_datetime(data['arr_time'].str.pad(4,side='left',fillchar='0'),format='%H%M',errors='coerce').dt.time
data['duration'] = data[['hour', 'min']].apply(lambda x: ''.join(x), axis=1)
data['duration'] = pd.to_datetime(data['duration'].str.pad(4,side='left',fillchar='0'),format='%H%M',errors='coerce').dt.time
data['date'] = data[['month', 'day', 'year']].apply(lambda x: '/'.join(x), axis=1)
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
        duration = data.iloc[row].loc['hour'],
    )
    for row, _ in enumerate(data)
]
for f in flights: f.save()
