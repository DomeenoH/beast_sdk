# Syc <github.com/SycAlright>
# Beast_SDK Python
# 注释by CyberBarbarian


beast = ['嗷', '呜', '啊', '~']                         # 密码库，四个字符

# 加密第一步，把字符串中的每个字符变成16进制Unicode（不含0x）堆在一起
def str2hex(text: str):                                 # 输入字符串text
    ret = ""                                            # 空字符串，存加密后的十六位数字
    for x in text:                                      # 对text中的每个字符
        charHexStr = hex(ord(x))[2:]                    # 用ord()函数找到Unicode编码（10进制），然后用hex()函数转为16进制，然后取第2位之后的部分（去掉0x）
        if len(charHexStr) == 3:
            charHexStr = "0" + charHexStr
        elif len(charHexStr) == 2:
            charHexStr = "00" + charHexStr              # 将16进制前面加0补全到4位
        ret += charHexStr                               # 把新的16进制字符串添加进 ret 后面
    return ret                                          # 返回所有字符的16进制Unicode

# 解码第二步，将每一位16进制的unicode编码分别转换回原字符，并拼在一起输出
def hex2str(text: str):                                 # 输入生成好的code：text
    ret = ""
    for i in range(0, len(text), 4):                    # i从0开始，加到text的长度减1停止，每次加4
        unicodeHexStr = text[i:i + 4]                   # 每次的Unicode做一个text[i:i + 4]的切片
        charStr = chr(int(unicodeHexStr, 16))           # 将10进制Unicode码转换回字符
        ret += charStr                                  # 把字符拼在一起
    return ret

# 加密第二步，将Unicode堆在一起的字符串[每一位]进行二次加密，并转换为[2个]兽语，然后堆在一起输出，完成加密
def encode(str):                                        # 输入要转换的字符串
    hexArray = list(str2hex(str))                       # 把字符串做初步加密为16进制Unicode
    code = ""
    n = 0                                               # 引入计数器n
    for x in hexArray:                                  # 对16进制Unicode串的每一个字符
        k = int(x, 16) + n % 16                         # int(x, 16)→把字符串转换为16进制数     k就是每一位的十六进制数加上n（进行二次加密）    %是取余
        if k >= 16:
            k -= 16                                     # 让结果落在0-16
        code += beast[int(k / 4)] + beast[k % 4]        # k/4，商作为第一个兽语，余数作为第二个兽语，因为k小于16，所以商不可能超过3     int(k / 4)代表(k / 4)保留整数   最后加进code
        n += 1                                          # n+1 移动到下一位
    return code

# 解码第一步，把兽语转换成16进制Unicode编码堆（每一位都含0x）
def decode(str):                                        # 传入兽语
    hexArray = list(str)                                # 
    code = ""                                           # 空字符串，存解密后的
    for i in range(0, len(hexArray), 2):                # 计数器i，从0开始，到（hexArray的长度-1）结束，每次+2
        pos1 = beast.index(hexArray[i])
        pos2 = beast.index(hexArray[i + 1])             # 从beast中取出相应字符，分别赋予给第一第二两个变量
        k = ((pos1 * 4) + pos2) - (int(i / 2) % 16)     # (pos1 * 4) + pos2)算出原来加密时的k     - (int(i / 2) % 16)之后得到x的十进制表示
        if k < 0:
            k += 16                                     # 目的是让k落在0-16范围内
        code += hex(k)[2:]                              # hex（）返回的是0xk，把0x去掉之后，k放在code字符串后面
    return hex2str(code)                                # 把生成好的code返回


if __name__ == '__main__':
    print(encode("你好"))
    print(decode("呜嗷嗷嗷啊嗷嗷~啊呜~啊~呜呜嗷"))
