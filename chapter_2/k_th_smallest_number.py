def k_th_small(li, k):
    """find the kth smallest number in O(nlog(n))"""
    if not li:
        raise Exception("no such list")
    if k < 1:
        raise Exception("no such element")
        
    li.sort()
    return li[k-1]

li = [9,8,7,6,5,4,3,2,1,0]
print(k_th_small(li, 10))