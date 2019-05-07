import os

if __name__ == '__main__':
    # w_file_path = "D:/data/weibo_dataset/re_follow.txt"
    # w_file = open(w_file_path, 'w')
    follow_dir_path = r"D:\data\weibo_dataset\original_data\follows"
    fan_dir_path = r"D:\data\weibo_dataset\original_data\fans"
    files_list = os.listdir(fan_dir_path)
    follow_set = set()
    fan_set = set()
    for file in files_list:
        follow_set.clear()
        fan_set.clear()
        follow_full_path = os.path.join(follow_dir_path, file)
        fan_full_path = os.path.join(fan_dir_path, file)
        try:
            with open(follow_full_path, 'r') as f1:
                lines1 = f1.readlines()
            with open(fan_full_path, 'r') as f2:
                lines2 = f2.readlines()
        except FileNotFoundError:
            print('File is not found.')
            continue
        # print(lines1[0].strip())
        # print(lines2)
        for line1 in lines1:
            follow_set.add(line1.strip())
        for line2 in lines2:
            fan_set.add(line2.strip())
        # print(follow_set)
        try:
            re_follow = len(follow_set.intersection(fan_set)) / len(follow_set)
        except ZeroDivisionError:
            re_follow = 0
        print(file[:-4], re_follow)
    #     w_file.write(file[:-4] + " " + str(re_follow) + "\n")
    # w_file.close()