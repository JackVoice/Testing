class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()
    return self

print(SortedList([4, 1, 5]).append(7))
