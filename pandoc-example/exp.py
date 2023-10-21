from fileinput import filename
import os

# os.system('pandoc --standalone --template template.html doc.md -o doc.html')


file_dir = "./answer_new"
file_answer = []
# for root, dirs, files in os.walk(file_dir, topdown=False):
#     print(root)     # 当前目录路径
#     # print(dirs)     # 当前目录下所有子目录
#     print(files)        # 当前路径下所有非目录子文件
#     for item in files:
#         file_answer.append(item[0:10])
#         os.system('cp '+file_dir+'/'+item+' '+'./answer_new'+'/'+item[0:10])

for root, dirs, files in os.walk(file_dir, topdown=False):
    print(root)     # 当前目录路径
    # print(dirs)     # 当前目录下所有子目录
    print(files)        # 当前路径下所有非目录子文件
    # for item in files:
    #     file_answer.append(item)
    file_answer=files

sl = open("./Student_List.txt","r")
data = sl.readlines()
sl.close()

sa = open("./Student_Grade.txt","w")
for item in data:
    number = item[0:10]
    if number in file_answer:
        fans = open("./data/"+item[11:51]+".ans", "r")
        ans = fans.read()
        fans.close()

        sans = open("./answer_new/"+number, "r")
        output = sans.read()
        sans.close()

        if ans.strip() == output.strip():
            sa.write(number+"\t"+"1\t"+"10\n")
        else:
            sa.write(number+"\t"+"1\t"+"0\n")
    else:
        sa.write(number+"\t"+"0\t"+"0\n")
sa.close()


