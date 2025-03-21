def anagram_check(s1:str, s2:str):
    s2_list = list(s2)
    
    result = True
    if len(s1) != len(s2_list):
        result = False
    
    pos_1 = 0
    while pos_1 < len(s1) and result:
        pos_2 = 0
        
        found = False
        while pos_2 < len(s2_list) and not found:
            
            if s1[pos_1] == s2_list[pos_2]:
                found = True
            else:
                pos_2 += 1
        if found:
            s2_list[pos_2] = None
        else:
            result = False
        pos_1 += 1
    return result



print(anagram_check("python", "typhon"))