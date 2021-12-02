import re

def solution(word, pages):
    score = {}
    url_idx = {}
    word = word.lower()

    for idx, page in enumerate(pages):
        score[idx] = {}
        score[idx]['link'] = []
        basic = 0

        for s in re.findall(r'[a-zA-Z]+', page.lower()):
            if s == word:
                basic += 1
        
        url = re.findall(r'<meta property="og:url" content="https://(\S+)"', page)[0]
        score[idx]['url'] = url

        link = re.findall(r'<a href="https://(\S+)"', page)
        for lk in link:
            score[idx]['link'].append(lk)
        
        score[idx]['basic'] = basic
        score[idx]['lnum'] = len(score[idx]['link'])
        score[idx]['external'] = 0
        url_idx[url] = idx

    for idx in score:
        cur = score[idx]
        for link in score[idx]['link']:
            if link in url_idx:
                target = score[url_idx[link]]
                target['external'] += cur['basic'] / cur['lnum']
    
    res = []
    for idx in score:
        cur = score[idx]
        res.append((cur['basic'] + cur['external'], idx))
    
    return sorted(res, key=lambda x: (-x[0], x[1]))[0][1]