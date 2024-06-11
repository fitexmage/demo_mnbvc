# demo_mnbvc

## 文件说明
48.txt：20230101/aliyun.20230101.6.网络小说/48.txt
474.txt：20230101/aliyun.20230101.6.网络小说/474.txt

## 问题说明
尝试读取上述的两个文件，采用charset_mnbvc中的get_cn_charset进行检查后，发现编码格式是UNKNOWN，代码如下：
```
coding_name = api.get_cn_charset(file_path, mode=2)
print(f"文件名: {file_path}, 编码: {coding_name}")
```
结果是：
```
文件名: 20230101/aliyun.20230101.6.网络小说/474.txt, 编码: UNKNOWN
```
直接采用UTF-8的方式进行读取后，出现的是乱码，如果再转为gbk等格式，会出现锟斤拷
