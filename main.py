
def calculate_time(startH, startM, endH, endM):
  global totalHours, totalMinutes
  if endH < startH:
    endH += 24
  if startM != 0:
    startMoverflow = 60 - startM
    startH += 1
  else:
    startMoverflow = startM
  hours = endH - startH
  minutes = endM + startMoverflow
  while minutes >= 60:
    hours += 1
    minutes -= 60
  totalHours += hours
  totalMinutes += minutes

def interval(n):
  global totalHours, totalMinutes
  totalHours = 0
  totalMinutes = 0
  count = 0
  stay = 1
  while count < n:
    print(f" ---------------\n Interval no. {stay}.")
    try:
      startH, startM = int(input(" Starting   hour: ")), int(input(" Starting minute: "))
      endH, endM = int(input("\n Ending     hour: ")), int(input(" Ending   minute: "))
      calculate_time(startH, startM, endH, endM)
    except ValueError:
      print(" Please, enter numbers only, without spaces. Restarting...\n")
      break
    count += 1
    stay += 1

  while totalMinutes >= 60:
    totalHours += 1
    totalMinutes -= 60
  
  if totalHours >= 1:
    print(f"\n Total time = {totalHours}h {totalMinutes}m\n ---------------------")
  else:
    print(f"\n Total time = {totalMinutes}m\n ---------------------")
  
# Main Loop
run = True
while run:

  try:
    n = int(input("""\n Enter '1' (for one time interval calucaltion) 
 or a number of time intervals if you would like to sum: """))
  except ValueError:
    print(" Please, enter numbers only, without spaces. Restarting...")
    continue

  interval(n)
