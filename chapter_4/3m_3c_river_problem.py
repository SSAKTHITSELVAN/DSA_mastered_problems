
def river_cross(m, c, b, path, visited):
    if (m, c, b) in visited:
        return False
    
    if m >= c:
        path.append((m,c,b))
        return False
    
    if m == c == 0:
        return True
    
    possible_moves = [
        (m-2, c, 'r'),
        (m-1, c-1, 'r'),
        (m, c-2, 'r'),
    ]
    
    for m, c, r in possible_moves:
        if river_cross(m, c, r):
            return True
    
    path.pop()
    return False

p = []
v = []
river_cross(3, 3, 'r', p, v)
print(p)