# Measures total interval of time between to parameters.


def timePassed(startH, startM, endH, endM):
  # startH/endH = hours | startM/endM = minutes
  if endH < startH:
    endH += 24
  if startM != 0:
    # minutesLeftover = minutes left from startM to full hour.
    minutesLeftover = 60 - startM
    startH += 1
  else:
    minutesLeftover = startM

  hours = endH - startH
  # Add minutesLeftover for a total sum of minutes
  minutes = endM + minutesLeftover
  # Subtract minutes that are overflown and add to hours
  while minutes >= 60:
    hours += 1
    minutes -= 60
  if hours >= 1:
    print(f"   Total time = {hours}h {minutes}m\n   ==================")
  else:
    print(f"   Total time = {minutes}m\n   ==================")


# Intro user EXP
print("\n   Enter time below\n   ==================")

# Main run
run = True
while run:

  try:
    startH, startM = int(input("   Starting  hour: ")), int(
      input("   Starting minut: "))
    endH, endM = int(input("\n   Ending    hour: ")), int(
      input("   Ending   minut: "))
    timePassed(startH, startM, endH, endM)
  except ValueError:
    print("   Enter only numbers, without spaces or other characters...\n")
