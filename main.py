from Tkinter import *
#from tkFileDialog   import askopenfilename  
import os.path
import sqlite3
import csv
from datetime import datetime
import math

def nmea(INPUT,TableName):
	conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
	c = conn.cursor()
	l = str(TableName)
	listName = l.split('.')
	# Create table
	c.execute('''CREATE TABLE '''+ str(listName[0]) + '''
						 (date text,time,speed float,latitude text,latitude_direction text,
						 longitude text,longitude_direction text,fix text,horizontal_dilution text,
						  altitude text,direct_of_altitude text,altitude_location text)''')

	with open(INPUT, 'r') as input_file:
		reader = csv.reader(input_file)
		#flag will tell us if the GPGGA is good if yes continue to the GPRMC
		flag = 0
		# create a csv reader object from the input file (nmea files are basically csv)
		i = 0
		for row in reader:
			# skip all lines that do not start with $GPGGA
			if not row:
				continue
			elif row[0].startswith('$GPGGA'):
				time = row[1]
				latitude = row[2]
				lat_direction = row[3]
				longitude = row[4]
				lon_direction = row[5]
				fix = row[6]
				numOfSat = row[7]
				horizontal = row[8]
				altitude = row[9]
				direct_altitude = row[10]
				altitude_location = row[11]
				flag = 1
				
			elif row[0].startswith('$GPRMC') and flag==1:
				speed = row[7]
				date = row[9]
				warning = row[2]
				if warning == 'V':
					continue
				i = i + 1
				print "Row " + str(i)
				c.execute("INSERT INTO "+str(listName[0])+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(date,time,speed,
																			   latitude, lat_direction,
																			   longitude, lon_direction,fix,
																			   horizontal,altitude,
																			   direct_altitude,
																			   altitude_location))
			# Save (commit) the changes
				conn.commit()
				flag=0
			else:
				continue
	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.commit()
	conn.close()

def toCSV():
	conn = sqlite3.connect("C:\\Python27\\nmea_to_db.db") #open db
	cursor = conn.cursor() #cursor to the db
	cursor.execute("select * from info;") # execute a sql script

	with open("out.csv", "wb") as csv_file: #writing to csv
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor.description]) # write headers
		csv_writer.writerows(cursor)

def addNmea():
	conn = sqlite3.connect('nmea_to_db.db')
	c = conn.cursor()

def toKML():
	conn = sqlite3.connect("C:\\Python27\\nmea_to_db.db") #open db
	cursor = conn.cursor() #cursor to the db
	pois = cursor.execute("select * from info;") # execute a sql script
	file = "out.kml"
	FILE = open(file, 'w')
	FILE.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	FILE.write('<kml xmlns="http://earth.google.com/kml/2.2">\n')
	FILE.write('<Document>\n')
	FILE.write('    <name>%s</name>\n' % file)
	FILE.write('    <description></description>\n')

	# Header
	FILE.write('<Placemark>\n')
	FILE.write('<name>Path</name>\n')
	FILE.write('<description><![CDATA[]]></description>\n')
	FILE.write('<styleUrl>#style_line</styleUrl>\n')
	FILE.write('<LineString>\n')
	
	# Cooridinates
	FILE.write('        <coordinates>\n')
	for poi in pois:
		lat = float(poi[3][:2]) + (float(poi[3][2:]) / 60)
		lon = float(poi[5][:3]) + (float(poi[5][3:]) / 60)
		FILE.write('        %s,%s,%s\n' % (str(lon), str(lat), str(0.0)))
	FILE.write('        </coordinates>\n')
	
	FILE.write('    </LineString>\n')
	FILE.write('</Placemark>\n')

	FILE.write('    </Document>\n')
	FILE.write('</kml>\n')
	FILE.close()
	conn.close()


def StartTime():
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT time FROM info')
        result=str(cur.fetchone())
        hour=result[3:5]
        minutes=result[5:7]
        seconds=result[7:9]
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        time="Start time:  " +str(hour)+ ': '+str(minutes)+': '+ str(seconds)
        pr=Label(root,text=time)
        pr.pack()
	conn.close()


def EndTime():
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT time FROM info')
        result=cur.fetchall()
        result1=str(result[len(result)-1])
        hour=result1[3:5]
        minutes=result1[5:7]
        seconds=result1[7:9]
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        time="Start time:  " +str(hour)+ ': '+str(minutes)+': '+ str(seconds)
        pr=Label(root,text=time)
        pr.pack()
	conn.close()

def Date():
        
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT date FROM info')
        result=str(cur.fetchone())
        day=result[3:5]
        month=result[5:7]
        year=result[7:9]
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        date="Start time:  " +str(day)+ '/ '+str(month)+'/ '+ str(year)
        pr=Label(root,text=date)
        pr.pack()
	conn.close()


def Speed():

        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT speed FROM info')
        result=cur.fetchall()
        sum=0.0
        for row in range(len(result)):
                result1=str(result[row])
                result1=result1[1:4]
                sum=sum+float(result1)
                print sum

        sum=sum/len(result)
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=sum)
        pr.pack()
	conn.close()
        

def Latitude():
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT latitude FROM info')
        result=cur.fetchall()
        sum=0.0
        for row in range(len(result)):
                result1=str(result[row])
                result1=result1[3:14]
                print result1
                sum=sum+float(result1)

                
        sum=sum/len(result)
        sum=str(sum)
        cur.execute('SELECT latitude_direction FROM info')
        result=str(cur.fetchone())
        answer=sum[:2]+'d '+sum[2:]+' '+result[2:4]
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=answer)
        pr.pack()
	conn.close()


def Longitude():
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT longitude FROM info')
        result=cur.fetchall()
        sum=0.0
        for row in range(len(result)):
                result1=str(result[row])
                result1=result1[3:14]
                sum=sum+float(result1)

                
        sum=sum/len(result)
        sum=str(sum)
        cur.execute('SELECT longitude_direction FROM info')
        result=str(cur.fetchone())
        answer=sum[:2]+'d '+sum[2:]+' '+result[2:4]
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=answer)
        pr.pack()
	conn.close()


def Fix():

        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT fix FROM info')
        result=str(cur.fetchone())
        result=result[3]
        result=int(result)
        if result==0:
                Start="Data invalid"
        elif result==1:
                Start="Data is from a GPS fix"
        else:
                Start="Data is from a DGPS fix"

        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=Start)
        pr.pack()
	conn.close()


def Horizontal():
        
        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT horizontal_dilution FROM info')
        result=str(cur.fetchone())
        result=result[3]
        result='Relative accuracy of horizontal position: ' + result
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=result)
        pr.pack()
	conn.close()


def Altitude():

        conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
        cur = conn.cursor()
        cur.execute('SELECT altitude FROM info')
        result=cur.fetchall()
        sum=0.0
        for row in range(len(result)):
                result1=str(result[row])
                result1=result1[3:7]
                sum=sum+float(result1)

                
        sum=sum/len(result)
        sum=str(sum)
        result= sum+' Meters above mean sea level'
        root = Tk()
        root.title("ANSWER")
        root.geometry("250x150")
        pr=Label(root,text=result)
        pr.pack()
	conn.close()


        
def load():
	conn = sqlite3.connect('C:\\Python27\\nmea_to_db.db')
	c = conn.cursor()
	tables = list(c.execute("select name from sqlite_master where type is 'table'"))
	
	c.executescript(';'.join(["drop table if exists %s" % i for i in tables]))
	
	INPUT = 'D:\\New folder'
	if os.path.isdir(INPUT):
		l = os.listdir(INPUT)
		for k in range(len(l)):
			nmea(INPUT + "\\"+l[k],l[k])


root = Tk()
root.title("NMEA TO DB")
root.geometry("157x312")
app = Frame(root,bg='black')
app.grid()

NmeaRunButton = Button(app , text = "Click to convert to db!" , command= load)
NmeaRunButton.pack()


ConvertToCSVbutton = Button(app , text = "Convert This NMEA to CSV!" , command = toCSV)
ConvertToCSVbutton.pack()

ConvertToKMLbutton = Button(app ,text = "Convert This NMEA to KML!", command = toKML)
ConvertToKMLbutton.pack()

StartButton = Button(app ,text = "Start time", command = StartTime)
StartButton.pack()

EndButton = Button(app ,text = "End time", command = EndTime)
EndButton.pack()

DateButton = Button(app ,text = "Date", command = Date)
DateButton.pack()

SpeedButton = Button(app ,text = "Average speed", command = Speed)
SpeedButton.pack()

LatitudeButton = Button(app ,text = "Average latitude", command = Latitude)
LatitudeButton.pack()

LongitudeButton = Button(app ,text = "Average longitude", command = Longitude)
LongitudeButton.pack()

FixButton= Button(app ,text = "Fix Quality", command = Fix)
FixButton.pack()

HorizontalButton= Button(app ,text = "Horizontal", command = Horizontal)
HorizontalButton.pack()

AltitudeButton= Button(app ,text = "Average Altitude", command = Altitude)
AltitudeButton.pack()


mainloop()
