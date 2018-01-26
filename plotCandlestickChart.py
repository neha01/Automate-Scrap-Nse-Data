import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
from matplotlib.finance import candlestick2_ochl
import matplotlib.dates as mdates


##style.use('ggplot')


##Reading csv file and storing as dataframe in df
df=pd.read_csv('TCS.csv')


df_ohlc=df

##Mapping dates of csv file to matplotlib dates  format
df_ohlc['Date']=df_ohlc['Date'].map(mdates.datestr2num)
##df_volume['Date']=df_volume['Date'].map(mdates.datestr2num)

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)

##ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.set_title('TCS')
candlestick2_ochl(ax1,df_ohlc['Open'],df_ohlc['Close'],df_ohlc['High'],df_ohlc['Low'],width=2,colorup='g')

##ax2.fill_between(df_volume['Date'],df_volume['Total Traded Quantity'].mean(),0)
##ax1.scatter(df_ohlc['Date'],df_ohlc['Total Traded Quantity'])
plt.show()
                     



                     






