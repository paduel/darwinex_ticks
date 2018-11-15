# Darwinex-ticks
Darwinex tick data python API.

The broker Darwinex offers to their real accounts a historical data dowload 
service using a ftp server. 

This basic API connects with your server account 
and download the data of one or several assets available. 

The data is returned as a Pandas dataframe. 


## Installation

`pip install Darwinex-ticks`
    
Pandas library is required. Ipywidgets optional, only for progress bar in 
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
                                end='2018-08-02 12')                 
```
You could check the example notebook too.