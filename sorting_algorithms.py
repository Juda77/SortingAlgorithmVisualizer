import sys
from max_heap import max_heap

def merge_sort(nums):

  if (len(nums) == 1 or len(nums) == 0):
    return nums

  first_half = nums[0 : int(len(nums) / 2)]
  second_half = nums[int(len(nums) / 2) : len(nums)]

  sorted_first_half = merge_sort(first_half)
  sorted_second_half = merge_sort(second_half)

  sorted_first_and_second_halfs = []
  first_half_index = 0
  second_half_index = 0

  while (first_half_index < len(sorted_first_half) or second_half_index < len(sorted_second_half)):

    if (first_half_index == len(sorted_first_half)):
      while (second_half_index < len(sorted_second_half)):
        sorted_first_and_second_halfs.append(sorted_second_half[second_half_index])
        second_half_index += 1
    elif (second_half_index == len(sorted_second_half)):
      while (first_half_index < len(sorted_first_half)):
        sorted_first_and_second_halfs.append(sorted_first_half[first_half_index])
        first_half_index += 1
    else:

      if (sorted_first_half[first_half_index] <= sorted_second_half[second_half_index]):
        sorted_first_and_second_halfs.append(sorted_first_half[first_half_index])
        first_half_index += 1
      else:
        sorted_first_and_second_halfs.append(sorted_second_half[second_half_index])
        second_half_index += 1

  return sorted_first_and_second_halfs


def quick_sort(nums):
  quick_sort_helper(nums, 0, len(nums) - 1)
  return nums

def quick_sort_helper(nums, left_index, right_index):

  if (left_index >= right_index):
    return

  pivot = nums[right_index]
  pivot_index = sort_by_pivot(nums, left_index, right_index, pivot)
  quick_sort_helper(nums, left_index, pivot_index - 1)
  quick_sort_helper(nums, pivot_index + 1, right_index)


#return final index of the pivot
def sort_by_pivot(nums, left_index, right_index, pivot):

  swap_index = left_index
  for i in range(left_index, right_index):
    curr = nums[i]
    if (curr < pivot):
      nums[i] = nums[swap_index]
      nums[swap_index] = curr
      swap_index += 1

  nums[right_index] = nums[swap_index]
  nums[swap_index] = pivot
  return swap_index

def heap_sort(nums):

  mh = max_heap(nums)
  mh.print_heap()

heap_sort([5,4,2,8,9,10,0,3])



def bubble_sort(nums):

  for i in range(len(nums)):
    stop_index = len(nums) - i
    for j in range(0, stop_index):
      if (j < stop_index - 1 and nums[j] > nums[j + 1]):
          #swap
          next_num = nums[j + 1]
          nums[j + 1] = nums[j]
          nums[j] = next_num

  return nums

def insertion_sort(nums):

  for i in range(len(nums)):
    curr = nums[i]
    backwards_index = i - 1
    while (0 <= backwards_index and curr < nums[backwards_index]):
      #swap
      temp = nums[backwards_index + 1]
      nums[backwards_index + 1] = nums[backwards_index]
      nums[backwards_index] = temp
      backwards_index -= 1

  return nums

def selection_sort(nums):

  for i in range(len(nums) - 1):
    index_of_minimum = i

    minimum = nums[i + 1]
    for j in range(i + 1, len(nums)):
      curr = nums[j]
      if (curr < minimum):
        minimum = curr
        index_of_minimum = j
    if (i < len(nums) - 2):
      #swap
      nums[index_of_minimum] = nums[i]
      nums[i] = minimum

  return nums

def test_sort():

  test_cases = [

    [],
    [0],
    [0,1,2],
    [2,1,0],
    [3,5,2,0,8,7,9],
    [9,8,7,6,5]

  ]

  for i in range(len(test_cases)):
    print("selection sort", selection_sort(test_cases[i]))

