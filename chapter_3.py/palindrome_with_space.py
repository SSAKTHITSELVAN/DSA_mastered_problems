from pythonds3 import Deque

def palindrome_checker(text):
    """verify the palindrome even with space"""
    dequeue = Deque()
    if not text:
        raise ValueError("Text is empty, not able to process...")
    for i in text:
        if i != " ":
            dequeue.add_rear(i)
    
    while dequeue.size() > 1:
        l = dequeue.remove_front()
        r = dequeue.remove_rear()
        if l != r:
            print(f"Not a palindrome, doesn't match {l} x {r}")
            return False
    return True

# pali_str = input()
print(palindrome_checker("i prefer pi"))
