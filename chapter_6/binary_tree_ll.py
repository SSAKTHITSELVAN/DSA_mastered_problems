"""Creating the binary tree by thr list of list approach"""

def make_binary_tree(root_val):
    return [root_val, [], []]

def insert_left_child(root, new_child):
    old_left_child = root.pop(1)
    
    if len(old_left_child) > 1:
        root.insert(1, [new_child, old_left_child, []])
    else:
        root.insert(1, [new_child, [], []])

def insert_right_child(root, new_child):
    old_right_child = root.pop(2)
    
    if len(old_right_child) > 1:
        root.insert(2, [new_child, [], old_right_child])
    else:
        root.insert(2, [new_child, [], []])

def get_root_value(root):
    return root[0]

def set_root_value(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


at = make_binary_tree(3)
insert_left_child(at, 4)
insert_left_child(at, 5)
insert_right_child(at, 6)
insert_right_child(at, 7)
lc = get_left_child(at)
set_root_value(lc, 9)
insert_left_child(lc, 11)
print(get_right_child(get_right_child(at)))
