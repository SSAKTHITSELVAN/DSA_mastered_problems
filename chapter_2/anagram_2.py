def anagram_check(s1: str, s2: str):
    """Check the strings are anagram"""
    a = sorted(s1)
    b = sorted(s2)
    
    pos = 0
    result = True
    while pos < len(a) and result:
        if a[pos] == b[pos]:
            pos += 1
        else:
            result = False
    
    
    return result




print(anagram_check("python", "typhon"))