import csv
import datetime
import math


class Activity:

    def __init__(self, r):

        # Activity type
        self.type = r[0]

        # Activity title
        self.title = r[4]

        # Average HF
        try:
            self.averageHF = int(row[7])
        except:
            # No valid average HF -> simply set to zero
            self.averageHF = 0

        # Average pace
        try:
            if self.type == 'cycling':  # For cycling pace is given in km per hour -> convert to min per km
                self.average_pace = self.km_per_hour_to_minutes_per_km(row[12])
            elif self.type == 'lap_swimming': # For swimming pace is given in min per 100m -> convert to min per km
                self.average_pace = self.string_to_timedelta(row[12]) * 10
            else:  # For all other activity types pace is already given in min per km
                self.average_pace = self.string_to_timedelta(row[12])
        except:
            self.average_pace = datetime.timedelta(hours=0)

        # Date and time of activity, date format in string '2018-01-13 10:14:47'
        try:
            self.date = datetime.datetime.strptime(r[1], '%Y-%m-%d %H:%M:%S')
        except:
            # No valid distance -> simply set to zero
            self.date = datetime.datetime.strptime('9999-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

        # Distance
        try:
            self.distance = float(row[4].replace(',', '.'))
        except:
            # No valid distance -> simply set to zero
            self.distance = 0.0

        # Calories
        try:
            self.calories = float(r[5])
        except:
            self.calories = 0

        # Duration comes in form '1:48:45' or '56:48'
        self.duration = self.string_to_timedelta(row[6])

    def string_to_timedelta(self, str):
        try:
            parts = str.split(":")
            mult = 1
            sec = 0
            for part in reversed(parts):
                sec += mult * int(part)
                mult *= 60
            # Return timedelta
            return datetime.timedelta(seconds=sec)
        except:
            return datetime.timedelta(hours=0)

    def km_per_hour_to_minutes_per_km (self, km_per_hour):
        try:
            # Conversion formula for km per hour (60 min): 60 divided by km -> min per km
            (full_min, part_min) = math.modf(60 / float(km_per_hour.replace(',', '.')))
            min_per_km = datetime.timedelta(seconds=(full_min * 60 + part_min * 60))
            # Round microseconds to next second
            if min_per_km.microseconds <= 500000:
                min_per_km += datetime.timedelta(seconds=1)
            min_per_km -= datetime.timedelta(microseconds=min_per_km.microseconds)
        except:
            min_per_km = datetime.timedelta(hours=0)
        return min_per_km

# someiterable = [['Wolle','Name'],['Horst','Name']]
# with open('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/someother.csv', 'a', newline='') as f:
#	writer = csv.writer(f)
#	writer.writerows(someiterable)
#	print("Hello world")

# Mobile-Path: /private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Activities.csv
# iCloud-Path: /Users/andibub/Library/Mobile Documents/com~apple~CloudDocs/Developer/Python/Garmin/Activities.csv
with open('/Users/andibub/Library/Mobile Documents/com~apple~CloudDocs/Developer/Python/Garmin/Activities.csv',
          newline='', encoding='utf-8') as csvfile:
    activities = csv.reader(csvfile)
    cycling = []
    walking = []
    act = []
    distance_cycling = 0.0
    calories_cycling = 0.0
    counter_cycling = 0
    distance_walking = 0.0
    calories_walking = 0.0

    firstline = True
    for row in activities:

        print(row)

        if firstline:
            firstline = False
            continue

        a = Activity(row)
        act.append(a)

        if act == 'cycling':
            cycling.append(row)
            distance_cycling += float(row[4].replace(',', '.'))
            calories_cycling += float(row[5])
            counter_cycling += 1
        elif act == 'walking':
            walking.append(row)
            distance_walking += float(row[4].replace(',', '.'))
            calories_walking += float(row[5])

    for row in cycling:
        print(row)

    print('Distance cycling: ' + str(distance_cycling))
    print('Calories cycling: ' + str(calories_cycling))
    print('Counter cycling: ' + str(counter_cycling))
    # print(f'Average distance cycling {distance_cycling/counter_cycling:{8}.{5}}')
    # print('Average distance cycling: ' + str(distance_cycling/counter_cycling))
    # width = 10
    # >>> precision = 4
    # >>> value = decimal.Decimal("12.34567")
    # >>> f"result: {value:{width}.{precision}}"

    print('Distance walking: ' + str(distance_walking))
    print('Calories walking: ' + str(calories_walking))

    for a in act:
        print(a.type, a.duration, a.date, a.distance, a.average_pace)

