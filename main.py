from charset_mnbvc import api


def convert(input_paths):
    for file_path in input_paths:
        coding_name = api.get_cn_charset(file_path, mode=2)
        print(f"文件名: {file_path}, 编码: {coding_name}")
        if coding_name == "UNKNOWN":
            with open(file_path, 'r', encoding='utf-8') as f:
                for i in range(10):
                    text = f.readline()
                    print([text])


if __name__ == "__main__":
    convert(["48.txt", "474.txt"])