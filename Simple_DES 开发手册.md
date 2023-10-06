# Simple_DES 开发手册

#### 文件主要函数及其接口如下

#### encrypt.py : 实现加密解密算法，同时实现了ASCII码扩展部分加解密
    permute : 置换函数
    binary_to_decimal : 二进制转化为十进制
    decimal_to_binary : 十进制转化为二进制
    replace : 替换操作
    class Encryptor : 封装了加密解密的内容的class类，其中的函数包含以下部分：
        generate_key : 随机生成10bit密钥的函数
        set_key : 保存输入的密钥
        generate_subkey : 生成子密钥
        single_group_encrypt : 明文加密函数，参数设置is_decrypt判断是否解密过程，若是解密过程，则置为 True进行解密
        F_function : 轮函数
        encrypt_string : 加密（解密）函数，支持字符串输入，生成ASCII密文
        encrypt_binary : 二进制列表输入的加密解密函数
#### decrypt.py : 实现暴力破解
    class Decryptor : 解密算法类，函数包含与加密一致
    class mythread : 使用线程暴力破解密钥的class类，包含以下函数：
        find_key : 通过穷举法暴力破解得到可能密钥的函数
        progress_bar : 建立进度条查看解密进度
        sift : 多个明密文对的密钥筛选得到共同密钥的函数
        onethread : 寻找一对密钥的函数
        Multithreading : 创建多个线程，寻找明密文对共同的密钥的函数
        solve : 启动线程寻找明密文对

        
        
        
        
        
        
    
    
    
