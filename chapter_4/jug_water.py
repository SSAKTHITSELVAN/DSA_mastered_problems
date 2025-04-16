
jug_max4 = 4
jug_max3 = 3

def water_fill(jug4, jug3, to_rem):
    """Solve the jug problem"""
    
    if jug4 == to_rem:
        print("success...")
        return
    
    print(f"j-3 -- {jug3} , j - 4 -- {jug4}")
    # filling event
    jug3 = jug_max3
    
    jug4 = min(jug3 , jug_max4-jug3)
    
    
    water_fill(jug4, jug3, to_rem)

water_fill(0, 0, 2)