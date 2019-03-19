import os

if __name__ == '__main__':
    w_file_path = "D:/data/weibo_dataset/interaction.txt"
    w_file = open(w_file_path, 'w')
    dir_path = "D:/data/weibo_dataset/original_data/weibo1"
    files_list = os.listdir(dir_path)
    for file in files_list:
        count = 0
        full_path = os.path.join(dir_path, file)
        with open(full_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "转发微博" in line:
                    count += 1
            inter_rate = count / 134
            print(inter_rate)
        w_file.write(file[:-4] + " " + str(inter_rate) + "\n")
    w_file.close()