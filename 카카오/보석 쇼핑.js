function solution(gems) {
    let answer = [0, gems.length - 1];
    
    let gemType = new Set(gems);
    let gemSize = gemType.size;
    let gemMap = new Map();    
    
    let gl = gems.length;
    let start = 0, end = 0;
    gemMap.set(gems[0], 1);
    
    while(end < gl && start <= end) {
        if (gemSize === gemMap.size) {
            if (answer[1] - answer[0] > end - start)
                answer = [start, end];
            if ((answer[1] - answer[0] == end - start) && (start < answer[0]))
                answer = [start, end];
            
            if (gemMap.get(gems[start]) > 1)
                gemMap.set(gems[start], gemMap.get(gems[start]) - 1);
            else
                gemMap.delete(gems[start]);
            start++;
        } else {
            end++;
            gemMap.set(gems[end], 1 + (gemMap.get(gems[end]) || 0));
        }
    }
    
    
    return [answer[0] + 1, answer[1] + 1];
}