from tqdm import tqdm
import threading
import time
import sys

#置换
def permute(box: list, origin: list) -> list:
    """
        置换操作
    Args:
        box: 置换盒
        origin: 初始数据

    Returns:
        返回置换后的数据
    """
    after_permute = []
    for i in range(0, len(box)):
        after_permute.append(origin[box[i] - 1])
    return after_permute
    
#左移操作
def left_shift(left_list):
    """
    进行左移操作
    """
    after_list=left_list[1:]
    after_list.append(left_list[0])
    return after_list


#二进制转化为十进制
def binary_to_decimal(binary: list) -> int:
    """
    进制转换操作
    """
    num = 0
    for i in range(len(binary)):
        num *= 2
        num += binary[i]
    return num

#十进制转化为二进制
def decimal_to_binary(decimal: int) -> list:

    binary = []
    while decimal > 0:
            binary.append(decimal % 2)
            decimal = int(decimal / 2)
    if len(binary) == 0:
        binary = [0]
    return binary[::-1]


def replace(box: list, origin: list) -> list:
    """
        替换操作
    Args:
        box: 替换盒
        origin: 初始数据

    Returns:
        返回替换结果
    """
    middle = origin[1:3]
    side = [origin[0], origin[3]]
    row = binary_to_decimal(side)
    col = binary_to_decimal(middle)
    binary = decimal_to_binary(box[row][col])
    if len(binary) == 1:
        binary = [0] + binary
    return binary

    
class Decryptor:
    #初始化类的属性
    def __init__(self):
        self.__key = []
        self.__sub_keys = []
        self.__P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.__P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.__initial_Pbox = [2, 6, 3, 1, 4, 8, 5, 7]
        self.__final_Pbox = [4, 1, 3, 5, 7, 2, 8, 6]
        self.__EPbox = [4, 1, 2, 3, 2, 3, 4, 1]
        self.__Sbox = [
            [[1, 0, 3, 2],
             [3, 2, 1, 0],
             [0, 2, 1, 3],
             [3, 1, 0, 2]],
            [[0, 1, 2, 3],
             [2, 3, 1, 0],
             [3, 0, 1, 2],
             [2, 1, 0, 3]]
        ]
        self.__SPbox = [2, 4, 3, 1]

    def init(self):
        self.generate_subkey()

    def set_key(self, key:str):
        li=[]
        for i in key:
            li.append(int(i))
        self.__key=li

    def set_subkey(self,k_1:str,k_2:str):
        li1=[]
        for i in k_1:
            li1.append(int(i))
        self.__sub_keys.append(li1)

        li2=[]
        for i in k_2:
            li2.append(int(i))
        self.__sub_keys.append(li2)


    #生成子密钥--两个P=Box
    def generate_subkey(self):
        """
            生成子密钥，保存到成员变量 sub_keys
        Returns:
            无返回值
        """
        # P10置换盒
        num_after_p10 = permute(self.__P10, self.__key)
        front = num_after_p10[:5]
        tail = num_after_p10[5:]
        for i in range(0, 2):
            # 左移操作
            
            front = left_shift(front)
            tail = left_shift(tail)

            num_after_p10 = front + tail
            # P8置换盒
            num_after_p8 = permute(self.__P8, num_after_p10)
            self.__sub_keys.append(num_after_p8)
        for i in range(2):
            num=i+1



    #轮函数-四个转换步骤
    def F_function(self, right_part, k_i) -> list:

        #第一步k扩展置换
        right_part2=permute(self.__EPbox, right_part)
        
        #第二步与k_i异或运算，加轮密钥
        for i in range(len(k_i)):
                right_part2[i] = right_part2[i] ^ k_i[i]
        
        #第三步通过S-Boxes压缩替换
        sub_left_part = right_part2[:4]
        sub_right_part = right_part2[4:]

        right_part4 = replace(self.__Sbox[0], sub_left_part) + replace(self.__Sbox[1], sub_right_part)
        #第四步直接置换
        output=permute(self.__SPbox,right_part4)
        return output

    
    def decrypt(self,cipher_text : str):
        # 字符传切割分组,得到解密密文
        cipher_text_list = []
        for i in cipher_text:
            cipher_text_list.append(int(i))

        #置换
        after_ip = permute(self.__initial_Pbox, cipher_text_list)
        #分成左右两个部分
        left_part = after_ip[:4]
        right_part = after_ip[4:]

        #多轮变换-解密的K1,K2是相反的
        for i in [1,0]:
                k_i = self.__sub_keys[i]
                # F 函数
                middle_value = self.F_function(right_part, k_i)
                # 生成的与左半部分进行异或--Mixer
                for j in range(len(left_part)):
                    left_part[j] = left_part[j] ^ middle_value[j]
                # 交换-Swapper
                if i != 0:
                    temp = left_part
                    left_part = right_part
                    right_part = temp
        #置换
        plain_text= permute(self.__final_Pbox, left_part + right_part)

        return plain_text  

class mythread():
    """
    使用线程来完成暴力破解
    """
    def __init__(self):
        self.__total=[]
        self.__find_total=[]
        
    def init(self):
         self.violent_debunking()

    def progress_bar(self, finish_tasks_number, tasks_number):
        """
        进度条
        :param finish_tasks_number: int, 已完成的任务数
        :param tasks_number: int, 总的任务数
        :return:
        """
        percentage = round(finish_tasks_number / tasks_number * 100)
        print("\r进度: {}%: ".format(percentage), "▓" * (percentage // 2), end="")
        sys.stdout.flush()
    
    #寻找密钥
    def find_key(self,text:list, flag:bool):
        find_keys=[]
        plainText=text[0]
        cipherText=text[1]
        for i in range(1024): 
                try_key = format(i, '010b')
                de = Decryptor()
                de.set_key(try_key)
                de.generate_subkey()
                lis = de.decrypt(cipherText)
                li=[str(m) for m in lis]
                string="".join(li)
                if string==plainText:
                    find_keys.append(try_key)
                    if flag==1:
                        self.__total.append(try_key)   
        return find_keys

    def onethread(self,text : list):
        find_keys=self.find_key(text, 0)
        num=len(find_keys)
        if num==0:
            print("没有找到密钥")
        else:
            print("一共找到",num,"个密钥:")
            for key in find_keys:print(key)

    #多个明密文对，筛选里面共同的密钥
    def sift(self, text,num):
        find=self.find_key(text,1)
        for i in self.__total:
            if self.__total.count(i)==num:
                if i not in self.__find_total:
                    self.__find_total.append(i)
                else:
                    pass


    #多线程
    def Multithreading(self):
        find_text=[]
        print("请输入明密文对个数")
        num=int(input())
        n=num
        while num>0:
            print("输入明文：")
            pt=input()
            print("请输入密文")
            ct=input()
            l1=[pt,ct]
            num-=1
            find_text.append(l1)
        start=time.time()
        #多线程
        for i in range(n):#利用循环创建n个线程
            t=threading.Thread(target=self.sift,args=(find_text[i], n,))
            #启动线程
            t.start()
            t.join()
            self.progress_bar(i+1,n)
        s=len(self.__find_total)
        if s!=0:
            print("找到共同的密钥：",self.__find_total)
        else:
            print('未找到共同密钥')
        print("花了:",time.time() - start,"s")

    def solve(self):
        print("输入明文：")
        pt=input()
        print("请输入密文")
        ct=input()
        find_text=[pt,ct]

        start=time.time()
        th=threading.Thread(target=self.onethread,args=(find_text,))
        #启动线程
        th.start()
        th.join()
        self.progress_bar(1,1)
        print("花了:",time.time() - start,"s")

    
if __name__=='__main__':
    de=Decryptor()
    print("请输入密钥：")
    k=input('')
    de.set_key(k)
    de.generate_subkey()
    print("请输入密文")
    ct=input('')
    s=de.decrypt(ct)
    print("明文为：",s,)
    
    #以下为调用暴力解密
    du=mythread()
    #一个明密文对解密
    du.solve()
    #多个线程，多个明密文对解密
    du.Multithreading()
