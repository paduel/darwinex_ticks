# Darwinex-ticks
Darwinex tick data python API.

The broker Darwinex offer to their real accounts a historical data dowload 
service using a ftp server. 

This basic API connect with your server account 
and download the data of one or several assets available. 

The data is returned as a Pandas dataframe. 


## Installation

`pip install darwinex_ticks`

Pandas library is required. Ipywidgets opcional, only for progress bar in 
Jupyter notebooks.


## Example 



Quick usage.
```
import darwinex_ticks
dwt = darwinex_ticks.DarwinexTicksConnection(dwx_ftp_user='<your Darwinex username>',
                       dwx_ftp_pass='<your Darwinex ftp password>',
                       dwx_ftp_hostname='<Darwinex ftp host eg. tickdata.darwinex.com>',
                       dwx_ftp_port='<assigned port>')
                       
data = dwt.ticks_from_darwinex('EURUSD', start='2018-08-02 08', 
                                end='2018-08-02 08')                 
```
You could check the example notebook too.