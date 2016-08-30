import pandas as pd
import datetime as dt
import numpy as np

# pd.options.display.max_columns = 5200
# pd.options.display.max_rows    = 5200
# pd.set_option('display.width', 1000) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display
# pd.set_option('display.max_rows', 500) #http://stackoverflow.com/questions/11707586/python-pandas-widen-output-display

wd = '/Users/danielmsheehan/Google Drive/projects/bid/data/'
wd = '/Users/danielmsheehan/Dropbox/Projects/bid/data/'

dp = wd+'processing/'

df1 = pd.read_csv(dp+'eventsmanabi_client_uniq_m04.csv')
df2 = pd.read_csv(dp+'eventsmanabi_client_uniq_m07.csv')
df3 = pd.read_csv(dp+'eventsmanabi_event_uniq_m04.csv')
df4 = pd.read_csv(dp+'eventsmanabi_event_uniq_m07.csv')
df5 = pd.read_csv(dp+'residentsmanabi_client_uniq_m04.csv')
df6 = pd.read_csv(dp+'residentsmanabi_client_uniq_m07.csv')
df7 = pd.read_csv(dp+'residentsmanabi_event_uniq_m04.csv')
df8 = pd.read_csv(dp+'residentsmanabi_event_uniq_m07.csv')

df1['type'] = 'events-client-04'
df2['type'] = 'events-client-07'
df3['type'] = 'events-event-04'
df4['type'] = 'events-event-07'
df5['type'] = 'residents-client-04'
df6['type'] = 'residents-client-07'
df7['type'] = 'residents-event-04'
df8['type'] = 'residents-event-07'

df04 = pd.concat([df1,df3,df5,df7])
df07 = pd.concat([df2,df4,df6,df8])

df04.to_csv(dp+'manabi_all_04.csv',index=False)
df07.to_csv(dp+'manabi_all_07.csv',index=False)