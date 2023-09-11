from random import randrange

class Patient:
  # A class that simultates patient behaviors and give us the main data needed

  def __init__(self,time):
    # timestamp: the time that the patient entered the queue in
    self.timestamp = time
    self.age = randrange(20,61) # Randomizing the age

  # Some getter methods
  def getStamp(self):
    return self.timestamp

  def getAge(self):
    return self.age

  # Calculate the waiting timeا
  def waitTime(self, currentTime):
    return currentTime - self.timestamp