#從一段文字中提取出國內手機號碼
import re


def main():
    # 創建正則表達式對象 使用了前瞻和回顧來保證手機號前後不應該出現數字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情說8130123456789遍，我的手機號是13512346789這個號碼，
    不是15600998765，也是110或119，B的手機號才是15600998765。
    '''
    # 查找所有匹配並保存到一個列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------分隔線--------')
    # 通過迭代器取出匹配對象並獲得匹配的內容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------分隔線--------')
    # 通過search函數指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()