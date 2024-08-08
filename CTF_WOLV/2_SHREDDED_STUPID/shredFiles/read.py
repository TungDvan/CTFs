# def read_first_character(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         first_char = file.read(1)
#         return first_char

# for i in range(28):
#     fname = ".\\shredFiles\\shred" + str(i) + ".txt"
#     if read_first_character(fname) == ' ': print(i)

def read_all_file(file_path):
    ans = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            ans.append(line)
    return ans

ans = []

for i in range(28):
    fname = ".\\shredFiles\\shred" + str(i) + ".txt"
    tmp = read_all_file(fname)
    ans.append(tmp)

for i in range(len(ans)):
    print(ans[i])

# for i in range(len(ans[i])):
#     for j in range(len(ans)): print(ans[j][i], end = '')
#     print()