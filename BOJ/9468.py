score = int(input())
if score >= 90:
    rank = 'A'
elif score >=80:
    rank = 'B'
elif score >= 70:
    rank = 'C'
elif score >= 60:
    rank = 'D'
else:
    rank = 'F'
print(rank)