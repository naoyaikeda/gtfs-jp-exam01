# %%
import pandas as pd
import os

# %%
source_dir = '..\\Data\\Source\\chuo'

# %%
stops = pd.read_csv(os.path.join(source_dir, 'stops.txt'))
stop_times = pd.read_csv(os.path.join(source_dir, 'stop_times.txt'))
trips = pd.read_csv(os.path.join(source_dir, 'trips.txt'))

# %%
stop_times['arrival_time'] = pd.to_datetime(stop_times['arrival_time'], format='%H:%M:%S')
stop_times['departure_time'] = pd.to_datetime(stop_times['departure_time'], format='%H:%M:%S')

# %%
route_group = trips.groupby(['route_id'])

# %%
route_group.groups.keys()

# %%
head_group = trips.groupby(['trip_headsign'])

# %%
head_group.groups.keys()

# %%
trips[trips['trip_headsign'] == 'バスセンター'].groupby(['route_id']).groups.keys()

# %%
route_1 = 'R010200191010000'
route_2 = 'R010200193010000'

# %%
trips_1 = trips[(trips['route_id'] == route_1)]
trips_2 = trips[(trips['route_id'] == route_2)]

# %%
trips_1 = trips_1[trips_1['service_id'] == 'S000004']
trips_2 = trips_2[trips_2['service_id'] == 'S000004']

# %%
first_trip_1 = trips_1.head(1)
first_trip_2 = trips_2.head(1)
# %%
first_trip_1_id = list(first_trip_1['trip_id'])[0]
first_trip_2_id = list(first_trip_2['trip_id'])[0]

# %%
trip1_stop_times = stop_times[stop_times['trip_id'] == first_trip_1_id]
trip2_stop_times = stop_times[stop_times['trip_id'] == first_trip_2_id]

# %%
trip1_01 = trip1_stop_times[['arrival_time', 'departure_time', 'stop_id', 'stop_sequence']].copy()
trip1_01['next_stop_sequence'] = trip1_01['stop_sequence'] + 1

# %%
trip1_02 = pd.merge(trip1_01, trip1_01, left_on='next_stop_sequence', right_on='stop_sequence')
trip1_03 = trip1_02[['departure_time_x', 'stop_id_x', 'stop_id_y', 'stop_sequence_x', 'arrival_time_y']]
trip1_03.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time']
trip1_03['time_diff'] = trip1_03['arrival_time'] - trip1_03['departure_time']
trip1_03['arrival_time'] = trip1_03['arrival_time'].dt.time
trip1_03['departure_time'] = trip1_03['departure_time'].dt.time

# %%
trip1_03

# %%
stop_names = stops[['stop_id', 'stop_name']]

# %%
trip1_04 = pd.merge(trip1_03, stop_names, left_on='from_stop_id', right_on='stop_id')
trip1_05 = trip1_04[['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'stop_name']]
trip1_05.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'from_stop_name']
trip1_06 = pd.merge(trip1_05, stop_names, left_on='to_stop_id', right_on='stop_id')
trip1_07 = trip1_06[['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'from_stop_name', 'stop_name']]
trip1_07.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_difff', 'from_stop_name', 'to_stop_name']

# %%
trip2_01 = trip2_stop_times[['arrival_time', 'departure_time', 'stop_id', 'stop_sequence']].copy()
trip2_01['next_stop_sequence'] = trip2_01['stop_sequence'] + 1

# %%
trip2_02 = pd.merge(trip2_01, trip2_01, left_on='next_stop_sequence', right_on='stop_sequence')
trip2_03 = trip2_02[['departure_time_x', 'stop_id_x', 'stop_id_y', 'stop_sequence_x', 'arrival_time_y']]
trip2_03.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time']
trip2_03['time_diff'] = trip2_03['arrival_time'] - trip2_03['departure_time']
trip2_03['arrival_time'] = trip2_03['arrival_time'].dt.time
trip2_03['departure_time'] = trip2_03['departure_time'].dt.time

# %%
trip2_03

# %%
stop_names = stops[['stop_id', 'stop_name']]

# %%
trip2_04 = pd.merge(trip2_03, stop_names, left_on='from_stop_id', right_on='stop_id')
trip2_05 = trip2_04[['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'stop_name']]
trip2_05.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'from_stop_name']
trip2_06 = pd.merge(trip2_05, stop_names, left_on='to_stop_id', right_on='stop_id')
trip2_07 = trip2_06[['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_diff', 'from_stop_name', 'stop_name']]
trip2_07.columns = ['departure_time', 'from_stop_id', 'to_stop_id', 'stop_sequence', 'arrival_time', 'time_difff', 'from_stop_name', 'to_stop_name']

# %%
trip1_07

# %%
trip2_07
