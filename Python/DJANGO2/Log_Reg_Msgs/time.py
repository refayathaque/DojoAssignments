import datetime
import pytz

fmt = '%b %d, %Y, %I:%M %p'

d = datetime.datetime.now(pytz.timezone("America/New_York"))
d_string = d.strftime(fmt)
d2 = datetime.datetime.strptime(d_string, fmt)
print d_string
print d2.strftime(fmt)
