#import sys
#sys.setrecursionlimit(999)

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
    print(merge_sort(test_cases[i]))

test_sort()
