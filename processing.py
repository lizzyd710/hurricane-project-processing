import os
import datetime

MONTHS = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10,
          'NOV': 11, 'DEC': 12}

class Storm():
    def __init__(self, date_line, name):
        self.name = name.strip()
        self.category = name[:name.rindex(' ')]
        self.advs = []
        dl = date_line[6:]
        dl = dl.strip()
        dl = dl.split(' ')  # if the length is now 4, that means its over two months, if its 3, then its just one
        if len(dl) == 3:
            start_month = MONTHS[dl[1]]
            end_month = MONTHS[dl[1]]
            start_day = dl[0][:2]
            end_day = dl[0][3:]
        else:
            start_month = MONTHS[dl[1][:3]]
            end_month = MONTHS[dl[2]]
            start_day = dl[0]
            end_day = dl[1][4:]
        self.year = int(dl[len(dl) - 1])
        self.start_date = datetime.date(self.year, int(start_month), int(start_day))
        self.end_date = datetime.date(self.year, int(end_month), int(end_day))
        self.duration = (self.end_date - self.start_date).days
        self.av_wind = 0

    def __str__(self):
        return self.name[self.name.rindex(' ') + 1:]

    def add_adv(self, adv):
        self.advs.append(adv)

    def average_wind(self):
        sum = 0
        blanks = 0
        for a in self.advs:
            if a.wind == '-':
                blanks += 1
            else:
                sum += int(a.wind)
        return sum // (len(self.advs) - blanks)

class Adv():
    def __init__(self, line, year):
        l = line.strip()
        d = l.split(" ")
        while '' in d:
            d.remove('')
        self.num = d[0]
        self.lat = float(d[1])
        self.long = float(d[2])
        self.wind = d[4]
        self.pressure = d[5]
        if len(d) > 7:
            self.cat = d[6] + " " + d[7]
        else:
            self.cat = d[6]
        t = d[3].split('/')
        self.time = datetime.datetime(year, int(t[0]), int(t[1]), int(t[2][:2]))

    def __str__(self):
        return "Num: " + self.num + " Lat: " + self.lat + " Long: " + self.long + " Time: " + str(
            self.time) + " Wind: " + self.wind + \
               " Pressure: " + self.pressure + " Category: " + self.cat

dict = {'2000': [],
        '2001': [],
        '2002': [],
        '2003': [],
        '2004': [],
        '2005': [],
        '2006': [],
        '2007': [],
        '2008': [],
        '2009': [],
        '2010': [],
        '2011': [],
        '2012': [],
        '2013': [],
        '2014': [],
        '2015': [],
        '2016': [],
        '2017': []
        }

def process():
    for year in list(dict.keys()):
        files = os.listdir(year)  # get all storms in a year
        for storm in files:
            data = open('C:/Users/lizzy/Documents/School/Geosystems/Hurricane Project/' + year + '/' + storm, 'r')
            s = Storm(data.readline(), data.readline())
            data.readline()
            l = data.readline()
            while l != '':
                s.add_adv(Adv(l, int(year)))
                l = data.readline()
            s.av_wind = s.average_wind()
            dict[year].append(s)

yearly_wind_average = {'2000': 0,
        '2001': 0,
        '2002': 0,
        '2003': 0,
        '2004': 0,
        '2005': 0,
        '2006': 0,
        '2007': 0,
        '2008': 0,
        '2009': 0,
        '2010': 0,
        '2011': 0,
        '2012': 0,
        '2013': 0,
        '2014': 0,
        '2015': 0,
        '2016': 0,
        '2017': 0}

def yearly_wind(year):
    num_advs = 0
    total_wind = 0
    for s in dict[year]:
        for a in s.advs:
            if a.wind != '-':
                num_advs += 1
                total_wind += int(a.wind)
    return (total_wind // num_advs, num_advs)

def yearly_duration(year):
    total_duration = 0
    for s in dict[year]:
        total_duration += s.duration
    return total_duration // len(dict[year])

av_duration = {'2000': 0,
        '2001': 0,
        '2002': 0,
        '2003': 0,
        '2004': 0,
        '2005': 0,
        '2006': 0,
        '2007': 0,
        '2008': 0,
        '2009': 0,
        '2010': 0,
        '2011': 0,
        '2012': 0,
        '2013': 0,
        '2014': 0,
        '2015': 0,
        '2016': 0,
        '2017': 0}
process()
for y in dict.keys():
    yearly_wind_average[y] = yearly_wind(y)
    av_duration[y] = yearly_duration(y)