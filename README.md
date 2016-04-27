# Ex2 - review

NMEA 0183 is a combined electrical and data specification for communication between marine electronics such as echo sounder, sonars, anemometer, gyrocompass, autopilot, GPS receivers and many other types of instruments. It has been defined by, and is controlled by, the National Marine Electronics Association. It replaces the earlier NMEA 0180 and NMEA 0182 standards.[1] In marine applications, it is slowly being phased out in favor of the newer NMEA 2000 standard.

The electrical standard that is used is EIA-422, although most hardware with NMEA-0183 outputs are also able to drive a single EIA-232 port. Although the standard calls for isolated inputs and outputs, there are various series of hardware that do not adhere to this requirement.

The NMEA 0183 standard uses a simple ASCII, serial communications protocol that defines how data are transmitted in a "sentence" from one "talker" to multiple "listeners" at a time. Through the use of intermediate expanders, a talker can have a unidirectional conversation with a nearly unlimited number of listeners, and using multiplexers, multiple sensors can talk to a single computer port.

At the application layer, the standard also defines the contents of each sentence (message) type, so that all listeners can parse messages accurately.

# Software 
##VisualGPS

VisualGPS (Freeware) incorporates many advanced features found in professional programs.  Its sole purpose is to display graphically specific NMEA 0183 sentences and show the effects of selective availability (SA).

###Features:

* Azimuth and Elevation Graph - View all satellites that are in view. Each satellite identifies its pseudo random number (PRN) and its azimuth and elevation. Also plot and print  the physical mask angle.

* Survey - The survey window displays both position and xDOP (HDOP and VDOP) parameters. The ability for user selectable HDOP/VDOP color thresholds for position averaging make a great utility. Also monitor Standard Deviation and effects of Selective Availability. That's not all - print the results graphically. (Click here for example print output) (in PDF format - 157K)
* Signal Quality/SNR Window - Monitor satellite signal to noise ratios and see them graphically on the screen. The signal quality window will grow or shrink to accommodate number of satellites in view
* Navigation - Monitor latitude, longitude and altitude
* NMEA Command Monitor - View NMEA sentences as they are received
