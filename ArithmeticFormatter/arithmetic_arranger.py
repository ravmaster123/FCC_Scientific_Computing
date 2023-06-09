def arithmetic_arranger(problems, should=False):
  #Too long
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  #Constituent parts of each problem
  parts = []
  for i in problems:
    if len(i.split()) == 3:
      
      for j in i.split():
        parts.append(j)
    else:
      arranged_problems = "Error: Too many operands."
      return arranged_problems
  for i in range(len(problems)):
    if parts[3*i + 1] not in ("+", "-"):
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
      if len(parts[3*i] > 4):
        arranged_problems = " Error: Numbers cannot be more than four digits."
        return arranged_problems
    if parts[3*i][0] == "-":
      if len(parts[3*i]) > 5:
        arranged_problems = " Error: Numbers cannot be more than four digits."
        return arranged_problems
      for j in range(1, len(parts[3*i])):
        if (ord(parts[3*i][j])-ord("0")) not in range(10):
          arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems
    else:
      
      for j in parts[3*i]:
        if (ord(j) - ord("0")) not in range(10):
          arranged_problems = "Error: Numbers must only contain digits."
          return arranged_problems
    if parts[3*i+2][0] == "-":
      if len(parts[3*i+2]) > 5:
        arranged_problems = " Error: Numbers cannot be more than four digits."
        return arranged_problems
      for j in range(1, len(parts[3*i+2])):
        if (ord(parts[3*i+2][j])-ord("0")) not in range(10):
          arranged_problems = "Error: Numbers must only contain digits"
        return arranged_problems
        
    else:
      if len(parts[3*i+2]) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems
      for j in parts[3*i + 2]:
        if (ord(j) - ord("0")) not in range(10):
          arranged_problems = "Error: Numbers must only contain digits."
          return arranged_problems
  
  operand1Lengths = [len(parts[3*i]) for i in range(len(problems))]
  operand2Lengths = [len(parts[3*i+2]) for i in range(len(problems))]
  line1 = (max(operand1Lengths[0], operand2Lengths[0])+2-operand1Lengths[0])*" " + parts[0]
  line2 = parts[1] + (max(operand1Lengths[0], operand2Lengths[0])+1-operand2Lengths[0])*" " + parts[2]
  line3 = (max(operand1Lengths[0], operand2Lengths[0])+2)*"-"
  line4 = (max(operand1Lengths[0], operand2Lengths[0])+2-len(str(eval(problems[0]))))*" " + str(eval(problems[0]))

  for i in range(1, len(problems)):
    line1 = line1 + "    "
    line2 = line2 + "    "
    line3 = line3 + "    "
    line4 = line4 + "    "
    line1 = line1 + (max(operand1Lengths[i], operand2Lengths[i])+2-operand1Lengths[i])*" " + parts[3*i]
    line2 = line2 + parts[3*i+1] + (max(operand1Lengths[i], operand2Lengths[i])+1-operand2Lengths[i])*" " + parts[3*i+2]
    line3 = line3 + (max(operand1Lengths[i], operand2Lengths[i])+2)*"-"
    line4 = line4 + (max(operand1Lengths[i], operand2Lengths[i])+2-len(str(eval(problems[i]))))*" " + str(eval(problems[i]))
  if should:
    arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
  else:
    arranged_problems = f"{line1}\n{line2}\n{line3}"
  return arranged_problems