from datetime import datetime
from dateutil.parser import parse

cases = int(raw_input('enter the number of subs'))
for i in range(cases):
    t1 = parse(raw_input('first_date'))
    t2 = parse(raw_input('second date'))
    print int(abs((t1 - t2).total_seconds()))
