
def tower(height, source, helper, destionation):
    """parameters as height, source, help, destination"""
    if height <= 1:
        destionation.append(source.pop())
        return
    tower(height-1, source, destionation,  helper)
    destionation.append(source.pop())
    tower(height-1, helper, source,  destionation)


s = [10, 9]
h = []
d = []
tower(2, s, h, d)
print(d)