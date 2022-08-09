def comp(a, b):
    min_len = min(len(a), len(b))
    if a[:min_len] == b[:min_len]:
        return False
    else:
        return True

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if comp(phone_book[i], phone_book[i+1]):
            continue
        else:
            return False
    
    return answer