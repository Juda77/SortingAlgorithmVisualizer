#max heap class used for heap sort
class max_heap:

#automatically build max heap upon instantiation
  def __init__(self, nums):

    self.heap = [] #declare an attribute
    self.build_heap(nums)
    self.heap_sort()

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

  #swap curr element and child with each other
  def swap(self, num, curr_index, child_index):

    child = self.heap[child_index]
    self.heap[curr_index] = child
    self.heap[child_index] = num

  #heapify function used as a helper for heap_sort
  def heapify_down(self, heap_size):

    curr_index = 0
    num = self.heap[curr_index]
    left_child_index = curr_index * 2 + 1
    right_child_index = curr_index * 2 + 2
    num_is_smaller_than_left = (left_child_index < heap_size and num < self.heap[left_child_index])
    num_is_smaller_than_right = (right_child_index < heap_size and num < self.heap[right_child_index])
    num_is_smaller_than_a_child = num_is_smaller_than_left or num_is_smaller_than_right

    while (num_is_smaller_than_a_child):

      #determine the bigger child
      #currently it's guaranteed that one child is bigger
      if (left_child_index >= heap_size): #if left child is not a viable option(it's out of bounds)
        self.swap(num, curr_index, right_child_index)
        curr_index = right_child_index
      elif (right_child_index >= heap_size): #if right child is not a viable option(it's out of bounds)
        self.swap(num, curr_index, left_child_index)
        curr_index = left_child_index
      else: #both children are possible options

        left = self.heap[left_child_index]
        right = self.heap[right_child_index]

        if (left >= right):
          self.swap(num, curr_index, left_child_index)
          curr_index = left_child_index
        elif (right > left):
          self.swap(num, curr_index, right_child_index)
          curr_index = right_child_index

      left_child_index = curr_index * 2 + 1
      right_child_index = curr_index * 2 + 2
      num_is_smaller_than_left = (left_child_index < heap_size and num < self.heap[left_child_index])
      num_is_smaller_than_right = (right_child_index < heap_size and num < self.heap[right_child_index])
      num_is_smaller_than_a_child = num_is_smaller_than_left or num_is_smaller_than_right

  def heap_sort(self):

    for i in range(len(self.heap), 0, -1):
      curr_max = self.heap[0]
      curr_bottom = self.heap[i - 1]
      self.heap[0] = curr_bottom
      self.heap[i - 1] = curr_max
      self.heapify_down(i - 1)
    print(self.heap)
