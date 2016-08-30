import pandas as pd
import datetime as dt
import numpy as np

pd.options.display.max_columns = 5200
pd.options.display.max_rows    = 5200
pd.set_option('display.width', 1000) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display
pd.set_option('display.max_rows', 500) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display

wd = '/Users/danielmsheehan/Google Drive/projects/bid/data/'
wd = '/Users/danielmsheehan/Dropbox/Projects/bid/data/'

di = 'input/bid/'
residents = wd+di+'ResidentesManabi.txt'

dfR = pd.read_csv(residents, sep='\t')

#['ID','FechaEvento','Hora','BaseCliente','ProvinciaCliente','CantonCliente','CiudadCliente','ParroquiaCliente','LatitudCliente','LongitudCliente','BaseEvento','NombreSitioEvento','ProvinciaEvento','CantonEvento','CiudadEvento','ParroquiaEvento','LatitudEvento','LongitudEvento','CantidadClientes']
dfR = dfR[['FechaEvento','Hora',   'ProvinciaCliente',    'CantonCliente',   'CiudadCliente', 'ParroquiaCliente','LatitudCliente','LongitudCliente','ProvinciaEvento','CantonEvento','CiudadEvento','ParroquiaEvento','LatitudEvento','LongitudEvento']]
dfR.columns = ['date', 'time_hour','clienthomeprovince','clienthomevillage','clienthomecity','clienthomeparish','clientlatitude', 'clientlongitude','eventprovince',  'eventvillage','eventcity',   'eventparish',    'eventlatitude','eventlongitude']

dfR['date'] =  pd.to_datetime(dfR['date'], format='%Y-%m-%d')
dfR['month'] = dfR['date'].dt.month
dfR['datetime'] = dfR['date'] + dfR['time_hour'].apply(pd.offsets.Hour)

dfR['client_admin_str'] = dfR['clienthomeprovince']+' - '+dfR['clienthomevillage']+' - '+dfR['clienthomecity']+' - '+dfR['clienthomeparish']
dfR['event_admin_str']  = dfR['eventprovince']     +' - '+dfR['eventvillage']     +' - '+dfR['eventcity']     +' - '+dfR['eventparish']


df = dfR[['datetime','month','clientlatitude','clientlongitude','client_admin_str']]
df = df[(df.month == 4)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'residentsmanabi_client_uniq_m04.csv',index=False)

df = dfR[['datetime','month','clientlatitude','clientlongitude','client_admin_str']]
df = df[(df.month == 7)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'residentsmanabi_client_uniq_m07.csv',index=False)

df = dfR[['datetime','month','eventlatitude','eventlongitude','event_admin_str']]
df = df[(df.month == 4)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'residentsmanabi_event_uniq_m04.csv',index=False)

df = dfR[['datetime','month','eventlatitude','eventlongitude','event_admin_str']]
df = df[(df.month == 7)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'residentsmanabi_event_uniq_m07.csv',index=False)

