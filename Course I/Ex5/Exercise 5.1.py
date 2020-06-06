# Exercise 5.1

import pandas as pd
import numpy as np

tanjoubi = pd.read_csv('tanjoubi.csv')

jp_year = '年'
jp_month = '月'
jp_day ='日'
jp_age = '年齢'

tanjoubi['誕生日'] = tanjoubi['誕生日'].str.replace('年','-')
tanjoubi['誕生日'] = tanjoubi['誕生日'].str.replace('月','-')
tanjoubi['誕生日'] = tanjoubi['誕生日'].str.replace('日','')

birthday = pd.to_datetime(tanjoubi['誕生日'])

today = pd.to_datetime('2020-6-12')

Timedelta = (today - birthday)

Timedelta = pd.to_timedelta(Timedelta)

年齢 = np.floor(Timedelta.dt.days/365)

tanjoubi['年齢'] = 年齢

tanjoubi.to_csv('tanjoubi_nenrei.csv')