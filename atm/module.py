
# Core modules
import datetime
from datetime import date
import time
from time import time


#pip module
from camelcase import camelCase

#today = datetime.date.today()
today = date.today()
timestamp = time()

c = camelCase()
print(c.hump('hello there world'))

print(timestamp)