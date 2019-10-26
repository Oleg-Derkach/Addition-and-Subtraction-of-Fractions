# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:22:53 2019

@author: Pups
"""

def find_frict(dr1, sign, dr2):

    dr_copy1, dr_copy2 = dr1.copy(), dr2.copy()
    mult, mult_2 = 1, 2
    
    while dr_copy1[1] != dr_copy2[1]:
        dr_copy1 = dr1.copy()
        dr_copy1[0], dr_copy1[1] = dr_copy1[0] * mult, dr_copy1[1] * mult
        mult += 1
        if dr_copy2[1] < dr_copy1[1]:
            mult -= 1
            dr_copy2 = dr2.copy()
            dr_copy2[0], dr_copy2[1] = dr_copy2[0] * mult_2, dr_copy2[1] * mult_2
            mult_2 += 1
    
    dr3 = [dr_copy1[0] + dr_copy2[0] * sign, dr_copy1[1]] 
    a, b, c = abs(dr3[0]), dr3[1], abs(dr3[0])
    
    while a != 1:
        if b % a == 0 and c % a == 0:
            de, da = b/a, c/a
            break
        else:
            a -= 1
            da, de = c, b
    return [int(sign * da), int(de)]

        
if __name__ == '__main__':
    
    while True:
        dr1 = [int(i) for i in input('введите дробь 1 в фомате 1/4: ').split('/')]
        sign =  input('знак (- или +): ')
        sign = -1 if sign == '-' else 1
        dr2 = [int(i) for i in input('введите дробь 1 в фомате 1/4: ').split('/')]  
        result = find_frict(dr1, sign, dr2) 
        print('Result: {}/{}'.format(result[0],result[1]))
        print('--------------------------------------------','\n')
        chose = input('Введите "c" для продолжения или "q" чтобы выйти : ').lower()
        if chose == 'q':
            break     
       
    