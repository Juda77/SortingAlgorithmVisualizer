class max_heap:

#automatically build max heap upon instantiation
  def __init__(self, nums):

    self.heap = [] #declare an attribute
    self.build_heap(nums)

  def heapify_up(self, num):

    self.heap.append(num)
    curr_index = len(self.heap) - 1
    parent_index = int((curr_index - 1) / 2)
    parent = self.heap[parent_index]

    while (curr_index > 0 and parent < num):
      self.heap[parent_index] = num
      self.heap[curr_index] = parent
      curr_index = parent_index
      parent_index = int((curr_index - 1) / 2)
      parent = self.heap[parent_index]

  #takes an array of nums as input and builds a heap out of its elements
  #O(n)
  def build_heap(self, nums):

    for i in range(len(nums)):
      self.heapify_up(nums[i])

  def swap(num, curr_index, child_index):
    child = self.heap[child_index]
    self.heap[curr_index] = child
    self.heap[child_index] = num

  #heapify function used as a helper for heap_sort
  def heapify_down(self):
    curr_index = 0
    num = self.heap[curr_index]
    heap_size = len(self.heap)
    left_child_index = curr_index * 2 + 1
    right_child_index = curr_index * 2 + 2
    num_is_smaller_than_a_child = (left_child_index < heap_size and num < self.heap[left_child_index])
                              or (right_child_index < heap_size and num < self.heap[right_child_index])
    while (curr_index < len(self.heap) and num_is_smaller_than_a_child):

      #determine the bigger child
      #currently it's guaranteed that one child is bigger






  def heap_sort():
    for i in range(len(self.heap), 0):
      curr_max = self.heap[0]
      curr_bottom = self.heap[len(self.heap) - 1]
      self.heap[0] = curr_bottom
      self.heap[len(self.heap) - 1] = max
      heapify_down()

