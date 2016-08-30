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
events = wd+di+'EventosManabi.txt'

dfE = pd.read_csv(events, sep='\t')

print dfE.head(100)

print len(dfE.index)

dfE = dfE.drop('ID',axis=1)

listCols = []

for i in dfE.columns:
	#print i
	listCols.append(i)

print listCols
print len(listCols)

newCols = ['date','time_hour','clientbase','clienthomeprovince','clienthomevillage','clienthomecity','clienthomeparish','clientlatitude','clientlongitude','baseevent','namesiteevent','eventprovince','eventvillage','eventcity','eventparish','eventlatitude','eventlongitude','countpeopleradiobase']

print len(newCols)

for i,j in zip(listCols,newCols):
	dfE = dfE.rename(columns=lambda x: x.replace(i, j))

print dfE.head(100)

dfE['date'] =  pd.to_datetime(dfE['date'], format='%Y-%m-%d')
dfE['month'] = dfE['date'].dt.month
dfE['datetime'] = dfE['date'] + dfE['time_hour'].apply(pd.offsets.Hour)

dfE['client_admin_str'] = dfE['clienthomeprovince']+' - '+dfE['clienthomevillage']+' - '+dfE['clienthomecity']+' - '+dfE['clienthomeparish']
dfE['event_admin_str']  = dfE['eventprovince']     +' - '+dfE['eventvillage']     +' - '+dfE['eventcity']     +' - '+dfE['eventparish']


df = dfE[['datetime','month','clientlatitude','clientlongitude','client_admin_str']]
df = df[(df.month == 4)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'eventsmanabi_client_uniq_m04.csv',index=False)

df = dfE[['datetime','month','clientlatitude','clientlongitude','client_admin_str']]
df = df[(df.month == 7)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count',]]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'eventsmanabi_client_uniq_m07.csv',index=False)

df = dfE[['datetime','month','eventlatitude','eventlongitude','event_admin_str']]
df = df[(df.month == 4)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'eventsmanabi_event_uniq_m04.csv',index=False)

df = dfE[['datetime','month','eventlatitude','eventlongitude','event_admin_str']]
df = df[(df.month == 7)]
df['count'] = 1
df.columns = ['datetime','month','latitude','longitude','admin','count']
df = df[['datetime','latitude','longitude','admin','count']]
dfg = df.groupby(['datetime','latitude','longitude','admin'],as_index=False).sum()
dfg['minnoise'] =  np.random.choice(range(1, 60), dfg.shape[0])
dfg['datetime'] = dfg['datetime'] + dfg['minnoise'].apply(pd.offsets.Minute)
dfg.to_csv(wd+'processing/'+'eventsmanabi_event_uniq_m07.csv',index=False)


