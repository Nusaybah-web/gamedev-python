'''with open("test.txt","w") as file:
    file.write("hello world. ")


with open("test.txt","a") as file:
    file.write("I am nusaybah")


with open("test.txt","r") as file:
    print(file.read())

'''

from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open("diary","w") as file:
    file.write("dear diary...")

with open("diary","a") as file:
    file.write( "today is wednesday and my day was not that exiteing, i woke up and was mostly on my phone.\n I had my quran class around 6 and finished 7 so i went out for a walk right after. "
               " I came back at 8 and we an dmy family went out to BBQ,"
               "then we came home and slept.")