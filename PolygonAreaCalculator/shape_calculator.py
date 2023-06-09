class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, amount):
    self.width = amount
  def set_height(self, amount):
    self.height = amount
  def get_area(self):
    return self.width*self.height
  def get_perimeter(self):
    return 2*(self.width + self.height)
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    x=""
    if self.width <= 50 and self.height <= 50:
      
      for i in range(self.height):
        x+="*"*self.width + "\n"
    else:
      x = "Too big for picture."
    return x
  def get_amount_inside(self, other):
    return (self.get_area()/other.get_area())//1
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, amount):
    self.width = amount
    self.height = amount
  def set_width(self, amount):
    self.width = amount
    self.height = amount
  def set_height(self, amount):
    self.height = amount
    self.width = amount
  def __str__(self):
    return f"Square(side={self.width})"