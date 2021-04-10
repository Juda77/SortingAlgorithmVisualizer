class max_heap:

#automatically build max heap upon instantiation
  def __init__(self, nums):
    self.heap = [] #declare an attribute
    self.build_heap(nums)

  def heapify_up(self, num):

    self.heap.append(num)
    curr_index = len(self.heap) - 1
    parent_index = int((curr_index - 1) / 2)
    print(type(parent_index))
    parent = self.heap[parent_index]

    while (curr_index > 0 and parent < num):
      self.heap[parent_index] = num
      self.heap[curr_index] = parent
      curr_index = parent_index
      parent = self.heap[int((curr_index - 1) / 2)]

  #takes an array of nums as input and builds a heap out of its elements
  def build_heap(self, nums):
    for i in range(len(nums)):
      self.heapify_up(nums[i])



  def print_heap(self):

    for i in range(len(self.heap)):
      print(self.heap[i], "hi")
