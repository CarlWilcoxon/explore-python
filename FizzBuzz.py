class Fizzy:
  def __init__(self, num):
    self.num = num
    self.fizzCount = 0
    self.buzzCount = 0
    self.fizzbuzzCount = 0

  def getcounts(self):
    return self.fizzCount, self.buzzCount, self.fizzbuzzCount

  def fizzbuzz (self):
    for x in range(1, self.num):
      if (x % 15 == 0):
        self.fizzbuzzCount+=1
        print('FizzBuzz')
      elif (x % 3 == 0):
        self.fizzCount+=1
        print('Fizz')
      elif (x % 5 == 0):
        self.buzzCount+=1
        print('Buzz')
      else:
        print(x)




bop = Fizzy(31)
bop.fizzbuzz()
print(bop.getcounts())
