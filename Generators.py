# Example building a list and Returning it
def first_n(n):
  # BUild and Return a list
  num, nums = 0, []
  while num < n:
    nums.append(num)
    num += 1
  return nums

sum_of_first_n = sum(first_n(100000))

## The above is Uncceptable since we can't store 10GB of memory just for a list of numbers.


#'''Using python generators instead'''
# Create a class
class first_n(object):
  def __init__ (self,n):
    self.n = n
    self.num = 0

  def __iter__(self):
    return self

# Python 3 compatibility
  def __next__(self):
    return.self.next()


  def next(self):
    if self.num < self.n:
      cur, self.num = self.num, self.num+1
      return cur,
    raise StopIteration()

sum_of_first_n = sum(first_n(100000))




# Or option 2
def first_n(n):
  num = 0
  while num < n:
    yield num
    num += 1

sum_of_first_n = sum(first_n(10000000))
                     

