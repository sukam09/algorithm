def solution(numbers):
    ans = []
    
    for number in numbers:
        if number % 2 == 0:
            ans.append(number + 1)
        
        else:
            number = list(bin(number)[2:])
            
            for i in range(len(number) - 1, -1, -1):
                if number[i] == '0':
                    number[i] = '1'
                    number[i + 1] = '0'
                    ans.append(int(''.join(number), 2))
                    break
            else:
                number[0] = '0'
                ans.append(int('1' + ''.join(number), 2))
    
    return ans