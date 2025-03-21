def anagram_check(s1: str, s2: str):
    """check for anagram"""
    
    count_a = [0] * 26
    count_b = [0] * 26
    
    for i in s1:
        pos = ord(i) - ord("a")
        count_a[pos] += 1
    
    for j in s2:
        pos = ord(j) - ord("a")
        count_b[pos] += 1
    
    pos_ = 0
    result = True
    while pos_ < 26 and result:
        if count_a[pos_] == count_b[pos_]:
            pos_ += 1
        else:
            result = False
    
    return result



print(anagram_check("python", "typhon"))