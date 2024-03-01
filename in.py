# 1748. Sum of Unique Elements-
# You are given an integer array nums. The unique elements of an array 
# are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

# look at each number

# track each number and its occurences
# check if the number is being tracked
# if tracke, increment count
# if not track it

# look thru log, count only the number with count = 1
# identify unique numbers
# start running sum

# def unique_sum(list):
#     unique = []
#     for i in range(len(list)):
#         count = 0
#         for j in range(len(list)):
#             if list[i] == list[j]:
#                 count += 1
#         if count == 1:
#             unique.append(list[i])
#     print(unique)
#     return sum(unique)
# print(unique_sum([1,2,3,4,5]))

# def sum_unique_numbers(nums):
#     output = 0
#     hash_map = {}
#     for num in nums:
#         if num not in hash_map:
#             hash_map[num] = 0
#         hash_map[num] +=1

#     for num, count in hash_map.items():
#         if count == 1:
#             output += num

#     return output

# print(sum_unique_numbers([1,2,3,3,2]), 1)

shopping_list = {}
while True:
    user_choice = input("Do you want to : Show/Add/Delete or Quit?: ")
    if user_choice == 'add':
        item = input('What item do you want to add?: ')
        quan = int(input('How many items do you want to add?: '))
        shopping_list[item] = quan
    elif user_choice == 'delete':
        remove_item = input('What item do you want to delete?: ')
        quan = int(input('How many?: '))
        if remove_item in shopping_list:
            shopping_list[remove_item] -= quan
            if shopping_list[remove_item] < 1:
                del(shopping_list[remove_item])
                print(f'{remove_item} removed from cart')
            else:
                print(f'You now have {shopping_list[remove_item]} of {remove_item} in your cart')

    elif user_choice == 'show':
        print('Your shopping list includes:')
        for k,v in shopping_list.items():
            print(f'there are {v} {k} in your cart')
    elif user_choice == 'quit':
        break
    else: print("enter valid input")
        


