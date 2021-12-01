def solution(character, monsters):
    player_hp, player_at, player_def = map(int, character.split())
    res = []
    
    for monster in monsters:
        monster_name = monster.split()[0]
        monster_exp, monster_hp, monster_at, monster_def = map(int, monster.split()[1:])
        
        exp = 0
        time = 0
        hp = player_hp
        
        while True:
            if player_at > monster_def:
                monster_hp -= player_at - monster_def
            else:
                break
            
            time += 1

            if monster_hp <= 0:
                exp = monster_exp
                break
            
            if monster_at > player_def:
                hp -= monster_at - player_def
            
            if hp <= 0:
                break
            
            hp = player_hp

        if exp:
            res.append((exp / time, monster_exp, monster_name))
        
    res.sort(key=lambda item: (-item[0], -item[1]))
    return res[0][2]