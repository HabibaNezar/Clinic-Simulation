class Doctor:
  # A class that simulates the doctor behaviour

  def __init__(self, rate):
    # timeRemaining: for the current patient to finish
    # workRate => "total patient time = age / workRate"
    self.timeRemaining = 0
    self.currentPatient = None
    self.workRate = rate

  def tick(self):
    # A function to pass one minute and decrease the remaining time by one
    # It also makes the doctor free if the remaining time is zero
    if self.currentPatient != None:
      self.timeRemaining -= 1
      if self.timeRemaining == 0:
        self.currentPatient = None

  def busy(self):
    # A function to check if the doctor is busy or not
    if self.currentPatient != None:
      return True
    else:
      return False

  def startNext(self,newPatient):
    # Enter new patient to the doctor room and give the doctor the data needed
    self.currentPatient = newPatient
    self.timeRemaining = round(newPatient.getAge() / self.workRate) # rounding for achieving zero at the end