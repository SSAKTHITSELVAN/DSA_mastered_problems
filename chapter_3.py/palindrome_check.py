from pythonds3 import Deque

def palindrome_finder(a_string):
    
    d = Deque()
    for i in a_string:
        d.add_rear(i)
    
    while d.size() > 1:
        front_element = d.remove_front()
        rear_element = d.remove_rear()
        
        if front_element != rear_element:
            return False
        
    return True

print(palindrome_finder('radar'))