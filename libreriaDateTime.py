import datetime
#print(datetime.datetime(2019, 1, 1, 09, 10, 12))
#print(datetime.datetime(2019, 1, 1, 24, 10, 35))
#print(datetime.datetime(2019, 1, 1))
#print(datetime.date(2019, 01, 01))
#print(datetime.datetime(2019, 1, 1, 12, 10, 35))
#print(datetime.date(2019, 2, 29))
#print(datetime.date(2019, 12, 31).isoformat())
#date_time = datetime.datetime(2019, 2, 27, 11, 15, 30)
#print(date_time.strftime("%d/%m/%y %H:%M"))
#date_time = "2019-01-30 15:30:45"
#data_str = datetime.strptime(data_str, "%Y-%m-%d-%H:%M:%S.%f")
#print(data_str)
#data_time = date_time.strptime("%Y-%m-%d-%H:%M:%S")
#print(data_time)
#data2_str = datetime.strptime(data2_str, "%Y-%m-%d-%H:%M:%S")
#print(data2_str)
#data3_str = datetime.strftime("%Y-%m-%d-%H:%M:%S.%f")
#print(data3_str)

#time.strptime(time_string[, format])

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)
print(date_time.strftime("%Y/%m/%d %H:%M:%S"))
print(type(date_time))
#print(date_time.strptime("%Y/%m/%d %H:%M:%S"))
#print(date_time.strftime("%y/%m/%d %H:%M:%S"))
#print(date_time.strftime("%Y/%m/%d %H:%M:%s"))