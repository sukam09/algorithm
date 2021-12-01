from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0
    going = deque()
    waiting = deque(truck_weights)
    arrived = deque()
    now_weight = 0

    while len(arrived) < len(truck_weights):
        ans += 1

        if going and ans - going[0][1] == bridge_length:
            arrived.append(going.popleft())
            now_weight -= arrived[-1][0]

        if waiting and len(going) < bridge_length and now_weight + waiting[0] <= weight:
            now_weight += waiting[0]
            going.append((waiting.popleft(), ans))

    return ans