import os

if __name__ == '__main__':
    w_file_path = 'D:/data/weibo_dataset/active_days.txt'
    w_file = open(w_file_path, 'w')
    dir_path = 'D:/data/weibo_dataset/original_data/weibo1'
    file_list = os.listdir(dir_path)
    for file in file_list:
        full_path = os.path.join(dir_path, file)
        with open(full_path, 'r') as f:
            count = set()
            count.clear()
            lines = f.readlines()
            for line in lines:
                line = line.split()
                count.add(line[1])
        res = len(count) / 134
        # print(file[:-4])
        # print(res)
        w_file.write(file[:-4] + " " + str(res) + "\n")
    w_file.close()