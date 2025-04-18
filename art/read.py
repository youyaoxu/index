import os

all=''
folder_path = "./art"
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # print(root)
        full_path = os.path.join(root, file) # 输出所有文件的完整路径（包含子目录）
        tagA = ("<a href='"+full_path+"'>" + full_path + "</a>")
        link = tagA.replace("\\","/")
        link = link.replace("art/","")
        # all+=link
        print(link)  
# print(all) 