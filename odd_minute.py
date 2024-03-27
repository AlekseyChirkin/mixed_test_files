import datetime
import time
from random import randint

for i in range(10):
    current_min = datetime.datetime.today().minute
    print(f"It's {current_min} minute now")
    if current_min // 2 == 0:
        print("Not an odd minute!")
    else:
        print("This minutes seems a little odd.")
    time.sleep(randint(1, 10))
