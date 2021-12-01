def solution(time, gold, upgrade):
    remain_time = time
    money = 0
    ans = max(0, gold * (time // upgrade[0][1]))

    while money < upgrade[1][0] and remain_time >= upgrade[0][1]:
        money += gold
        remain_time -= upgrade[0][1]
    
    if money >= upgrade[1][0]:
        money -= upgrade[1][0]
        ans = max(ans, money + gold * (remain_time // upgrade[1][1]))

    while money < upgrade[2][0] and remain_time >= upgrade[1][1]:
        money += gold
        remain_time -= upgrade[1][1]
    
    if money >= upgrade[2][0]:
        money -= upgrade[2][0]
        ans = max(ans, money + gold * (remain_time // upgrade[2][1]))

    return ans