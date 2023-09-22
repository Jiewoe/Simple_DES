import random


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


def binary_to_decimal(binary: list) -> int:
    num = 0
    for i in range(len(binary)):
        num *= 2
        num += binary[i]
    return num


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


class Encryptor:
    def __init__(self):
        self.__key = []
        self.__sub_keys = []
        self.__P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # 置换盒P10
        self.__P8 = [6, 3, 7, 4, 8, 5, 10, 9]  # 置换盒P8
        self.__left_shift_num = [1, 2]  # 左移位数
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
        """
            初始化密钥、子密钥
        Returns:
            无返回值
        """
        self.generate_key()
        self.generate_subkey()

    def generate_key(self) -> None:
        """
            生成10bit密钥的函数,以字符串的方式保存在成员变量中
        Returns:
            无返回值
        """
        for i in range(0, 10):
            temp = random.random()
            self.__key.append(round(temp))

    def set_key(self, key):
        self.__key = key

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
            left_temp = front[:self.__left_shift_num[i]]
            right_temp = front[self.__left_shift_num[i]:]
            front = right_temp + left_temp

            left_temp = tail[:self.__left_shift_num[i]]
            right_temp = tail[self.__left_shift_num[i]:]
            tail = right_temp + left_temp

            num_after_p10 = front + tail

            # P8置换盒
            num_after_p8 = permute(self.__P8, num_after_p10)
            self.__sub_keys.append(num_after_p8)

    def single_group_encrypt(self, group: list, is_decrypt=False) -> list:
        """
            单组明文加密
        Args:
            is_decrypt: 是否解密过程，若是解密过程，则置为 True
            group: 8bit明文组，此处为一个8位的列表，列表的每一个元素代表一个bit位

        Returns:
            返回密文
        """
        if is_decrypt:
            sub_keys = self.__sub_keys[::-1]
        else:
            sub_keys = self.__sub_keys

        after_ip = permute(self.__initial_Pbox, group)

        left_part = after_ip[:4]
        right_part = after_ip[4:]

        for i in range(0, 2):
            k_i = sub_keys[i]

            # F 函数
            middle_value = self.F_function(right_part, k_i)

            # 左半部分进行异或
            for j in range(len(left_part)):
                left_part[j] = left_part[j] ^ middle_value[j]

            # 交换
            if i != 1:
                temp = left_part
                left_part = right_part
                right_part = temp

        after_fp = permute(self.__final_Pbox, left_part + right_part)
        return after_fp

    def F_function(self, right_part, k_i) -> list:
        """
            轮函数
        Args:
            k_i: 子密钥
            right_part: 明文经过初始置换后的右半部分

        Returns:
            返回一个list，用于与左半部分进行异或运算
        """
        middle_value = permute(self.__EPbox, right_part)
        for j in range(len(k_i)):
            middle_value[j] = middle_value[j] ^ k_i[j]

        sub_left_part = middle_value[:4]
        sub_right_part = middle_value[4:]
        middle_value = replace(self.__Sbox[0], sub_left_part) + replace(self.__Sbox[1], sub_right_part)
        middle_value = permute(self.__SPbox, middle_value)

        return middle_value


if __name__ == "__main__":
    en = Encryptor()

    plain_text = [1, 0, 0, 1, 1, 0, 1, 0]
    # en.set_key([1, 0, 1, 0, 0, 0, 0, 0, 1, 0])
    en.generate_key()
    en.generate_subkey()

    s = en.single_group_encrypt(plain_text)
    print("加密: " + str(s))
    p = en.single_group_encrypt(s, True)
    print("解密: " + str(p))
    print("明文: " + str(plain_text))
