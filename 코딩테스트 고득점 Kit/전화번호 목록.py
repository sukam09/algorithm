def solution(phone_book):
    dic = {x: True for x in phone_book}
    phone_book.sort(key=lambda x: -len(x))
    maxlen = len(phone_book[0])
    for i in range(maxlen + 1):
        for x in phone_book:
            try:
                if dic[x[:i]] and x[:i] != x:
                    return False
            except:
                pass
    return True