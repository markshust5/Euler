#this is the list formation portion
lis_3 = [n for n in range(1, 1000) if n % 3 == 0]
lis_5 = [n for n in range(1, 1000) if n % 5 == 0]

#comine the list
lis_combined = lis_3 + lis_5
#print(lis_combined)


#remove repeats
cleaned = []
for i in lis_combined:
    if i not in cleaned:
        cleaned.append(i)

#this is the sumation portion of the list
sumation_lis_combined = sum(cleaned)
print(sumation_lis_combined)
#print(cleaned)

