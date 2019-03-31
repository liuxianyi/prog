import os


def get_all_html_file(file_path):
    """
    # https://www.cnblogs.com/renfanzi/p/8243777.html
    :param file_path:
    :return:
    """
# 遍历file_path下所有文件，包括子目录
    files = os.listdir(file_path)
    file_name = []
    for fi in files:
        fi_d = os.path.join(file_path, fi)
        # if os.path.isdir(fi_d):
            # get_all_html_file(fi_d)
        # else:
        file_ = os.path.join(file_path, fi_d)
        file_name.append(file_)
        # print('file_name', file_)
    return file_name


# def get_html_data(file):
