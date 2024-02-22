import time as time

date = time.time()

print("Seconds since January 1, 1970:", format(date, ",.4f"), "or",
      format(date, '.2e'), "in scientific notation")
print(time.strftime("%b %d %Y"))
