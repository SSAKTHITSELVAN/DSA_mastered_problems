def generate_perm(st_list, l, r, res):
    if l == r:
        res.append("".join(st_list))  # Convert list back to string
        return

    for i in range(l, r + 1):
        dubli = True
        for j in range(l, i):
            if st_list[i] == st_list[j]:
                dubli = False
                break
        if dubli:
            st_list[l], st_list[i] = st_list[i], st_list[l]
            generate_perm(st_list, l + 1, r, res)
            st_list[l], st_list[i] = st_list[i], st_list[l]

a = "AAB"
res = []
l = 0
r = len(a) - 1
a_list = list(a)  # Convert string to list
generate_perm(a_list, l, r, res)
print(res)