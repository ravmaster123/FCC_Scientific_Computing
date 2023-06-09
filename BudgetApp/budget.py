
class Category:
  def __init__(self, categ):
    self.categ = categ
    self.balance = 0
    self.ledger=[]
    self.spending = 0
  def check_funds(self, amount):
    return self.balance >= amount
  def deposit(self, amount, description=""):
    self.balance = self.balance + amount
    self.ledger.append({"amount": amount, "description": description})
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance = self.balance - amount
      self.ledger.append({"amount": -amount, "description": description})
      self.spending += amount
      return True
    return False
  def get_balance(self):
    return self.balance
  def transfer(self, amount, other):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {other.categ}")
      other.deposit(amount, f"Transfer from {self.categ}")
      return True
    return False
  def __str__(self):
    line1 = "*"*((30-len(self.categ))//2) + self.categ + (30-((30-len(self.categ))//2 + len(self.categ)))*"*"
    soForth = ""
    for i in self.ledger:
      line = ""
      if i["amount"] % 1 == 0:
        amount=str(i["amount"]) + ".00"
      elif len(str(i["amount"]).split(".")[1]) == 2:
        amount=str(i["amount"])
      else:
        amount = str(i["amount"]) + "0"
      if len(amount) > 7:
        amount = amount[-7:]
      if len(i["description"]) > 23:
        line += i["description"][:23]
      else:
        line += i["description"]
      line += (30-len(line)-len(amount))*" "
      line += amount
      soForth += '\n' + line
    soForth += '\n'
    soForth += f"Total: {self.balance}"
    return line1 + soForth
    
  



def create_spend_chart(categories):
  toReturn="Percentage spent by category\n"
  totalSpending = 0
  toMakeChart = []
  for i in categories:
    totalSpending += i.spending
  for i in categories:
    toMakeChart.append(((i.spending*100)/totalSpending)//10)
  toPrint = [[" " for i in range(11)] for i in categories]
  for i in range(len(categories)):
    for j in range(int(toMakeChart[i])+1):
      toPrint[i][j] = "o"
  for i in range(10, -1, -1):
    line = ""
    line += (3-len(str(i*10)))*" " + str(i*10) + "| "
    for j in range(len(categories)):
      line += toPrint[j][i]
      line += "  "
    toReturn += line + "\n"
  toReturn += ("    " + (3*len(categories)+1)*"-")
  counter = 0
  while True:
    toAdd = ""
    for i in categories:
      if counter >= len(i.categ):
        toAdd += " "
      else:
        toAdd += i.categ[counter]
    if toAdd == " "*len(categories):
      break
    toReturn += "\n"
    toAddFinally="     "
    for i in toAdd:
      toAddFinally += i
      toAddFinally += "  "
    toReturn += toAddFinally
    counter += 1
  return toReturn
      
    
    
    
