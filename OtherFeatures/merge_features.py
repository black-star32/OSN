import os

if __name__ == '__main__':
    '''
    normalize_features3.txt
    re_follow
    active_days_figure
    similarly
    interaction
    D:\data\weibo_dataset\coefficients
    
    '''
    dir_path = r'D:\data\weibo_dataset'
    active_days_file =  os.path.join(dir_path, 'active_days.txt')
    interaction_file = os.path.join(dir_path, 'interaction.txt')
    re_follow_file = os.path.join(dir_path, 're_follow.txt')
    similary_file = os.path.join(dir_path, 'similarly.txt')
    topic_file = os.path.join(dir_path, 'topic.txt')