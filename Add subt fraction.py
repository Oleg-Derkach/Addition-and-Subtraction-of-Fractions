dr1, dr2 = [4, 15], [12, 15]       
sign = -1                        #(+ or -)

dr_copy1, dr_copy2 = dr1.copy(), dr2.copy()
mult, mult_2 = 2, 2

while dr_copy1[1] != dr_copy2[1]:
    dr_copy1 = dr1.copy()
    dr_copy1[0], dr_copy1[1] = dr_copy1[0] * mult, dr_copy1[1] * mult
    mult += 1
    if dr_copy2[1] < dr_copy1[1]:
        dr_copy2 = dr2.copy()
        dr_copy2[0], dr_copy2[1] = dr_copy2[0] * mult_2, dr_copy2[1] * mult_2
        mult_2 += 1

dr3 = [dr_copy1[0] + dr_copy2[0] * sign, dr_copy1[1]]
delim = 1   
a, b, c = abs(dr3[0]), dr3[1], abs(dr3[0])

while a != 1:
    if b % a == 0 and c % a == 0:
        de, da = b/a, c/a
        break
    else:
        a -= 1
        da, de = c, b
        
print(sign * da,'/',de)
