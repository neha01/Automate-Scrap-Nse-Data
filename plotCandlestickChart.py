import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

import datetime as dt

style.use('ggplot')

df=pd.read_csv('TCS.csv')


from matplotlib.finance import candlestick2_ochl
import matplotlib.dates as mdates


##df_ohlc=df['Last Price']
##
df_ohlc=df

df_volume=df
##df_volume['Total Traded Quantity']=df['Total Traded Quantity'].rolling(10).mean()

##print(df_ohlc.head())

##df_ohlc=df.reset_index()

df_ohlc['Date']=df_ohlc['Date'].map(mdates.datestr2num)
##df_volume['Date']=df_volume['Date'].map(mdates.datestr2num)
##
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
##
##ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
##
##ax1.xaxis_date()
ax1.set_title('TCS')
candlestick2_ochl(ax1,df_ohlc['Open'],df_ohlc['Close'],df_ohlc['High'],df_ohlc['Low'],width=2,colorup='g')

##ax2.fill_between(df_volume['Date'],df_volume['Total Traded Quantity'].mean(),0)
##ax1.scatter(df_ohlc['Date'],df_ohlc['Total Traded Quantity'])

plt.show()
                     



                     






