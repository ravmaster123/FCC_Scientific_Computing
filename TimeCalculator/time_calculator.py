def add_time(start, duration, day = None):
  time12 = start.split()[0]
  startTime = int(time12.split(":")[0])*60 + int(time12.split(":")[1])
  if start.split()[1] == "PM":
    startTime = startTime + 720
  durationTime = int(duration.split(":")[0])*60 + int(duration.split(":")[1])
  finishTime = startTime+durationTime
  hours = finishTime // 60
  if len(str(finishTime %60)) == 1:
    minutes = "0" + str(finishTime % 60)
  else:
    minutes = str(finishTime%60)
  by24Hours = str(hours%24)
  by12Hours = str(((hours-1)%12)+1)
  if int(by24Hours) < 12:
    ampm = " AM"
  else:
    ampm = " PM"
  if hours//24 == 1:
    daysLater = " (next day)"
  elif hours//24 == 0:
    daysLater = ""
  else:
    daysLater = f" ({hours//24} days later)"
  if day == None:
    newDay = ""
  else:
    daysHigher = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    daysLower = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    dayDex = daysLower.index(day.lower())
    newDay = ", " + daysHigher[((hours//24) + dayDex)%7]
  new_time = by12Hours + ":" + minutes + ampm + newDay + daysLater
  
  return new_time