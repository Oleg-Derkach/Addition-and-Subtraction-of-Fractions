# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:38:22 2019

@author: Pups
"""

def long_range(array):
    '''Функция находит самый длинный непрерывный список чисел в массиве 
    '''
    numbers = {x:0 for x in array}
    left = right = 0
    for nums in array:
        if numbers[nums] == 0:
            left_count = nums -1
            right_count = nums +1
            
            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1
            
            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1
            
            if (right-left) <= (right_count-left_count):
                right = right_count
                left = left_count
    return (left, right)

array = [11,7,3,4,2,1,0,22,23,24,25]  
print(long_range(array))            
      