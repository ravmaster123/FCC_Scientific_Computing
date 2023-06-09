import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
      self.contents = []
      for color, count in args.items():
          for _ in range(count):
              self.contents.append(color)
  def draw(self, num):
    if len(self.contents) < num:
      x=copy.deepcopy(self.contents)
      self.contents = []
      return x
    else:
      drew = []
      for i in range(num):
        x=random.randrange(len(self.contents))
        a=self.contents.pop(x)
        drew.append(a)
      return drew
def countInstances(listy, color, number):
  counter = 0
  for i in listy:
    if i == color:
      counter += 1
  return counter >= number #Present
        
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  result = 0
  
  for _ in range(num_experiments):
    a=copy.deepcopy(hat)
    drawn = a.draw(num_balls_drawn)
    allColorsPresent = True
    for i in expected_balls.keys():
      if not countInstances(drawn, i, expected_balls[i]):
        allColorsPresent = False
        break
    if not allColorsPresent:
      result = 0
    else:
      result = 1
    successes += result
  return successes/num_experiments
      
    
    
  