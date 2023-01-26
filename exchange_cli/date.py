import sys

from datetime import datetime, timedelta


def get_date_list(start_date, end_date):
    
    if start_date > end_date:
        print("The start date cannot be greater than the end date, exiting...")
        sys.exit()

    def daterange(date1, date2):
            for n in range(int ((date2 - date1).days)+1):
                yield date1 + timedelta(n)
        
    start_date_object = datetime.strptime(start_date,'%Y%m%d')
    end_date_object = datetime.strptime(end_date,'%Y%m%d')
    date_list = [i for i in daterange(start_date_object,end_date_object)]
    for date in date_list:
        date = datetime.strftime(date,"%Y-%m-%d")
    return date_list
