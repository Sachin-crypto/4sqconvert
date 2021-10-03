# -*- encoding: utf-8 -*-

from icalendar import Calendar
import os
import codecs

directory = os.path.dirname(__file__)
cal = Calendar.from_ical(open(os.path.join(directory, 'import.ics'),'r').read())

for comp in cal.walk():
	if comp.name == "VEVENT":
		name = comp["location"]
		time = comp["dtstart"].dt.strftime("%x %X")
		latitude = comp["geo"].latitude
		longitude = comp["geo"].longitude
		url = comp["url"]
		print (",".join([name,  time,  unicode(latitude), unicode(longitude) , url]))
