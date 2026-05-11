# 案例1: 定义一个函数: 计算传入的字符串中元音字母的个数 (元音字母为aeiouAEIOU)
def vowel(s):
    """
    根据传入的字符串,计算其中元音字母的个数
    :param s: 传入的字符串
    :return: 字符串中元音字母的个数
    """
    num = 0
    for c in s:
        if c in 'aeiouAEIOU':
            num += 1
    return num

print(vowel('Man, what can I say, manba out'))

# 案例2: 定义一个函数: 计算传入的成绩列表中最高分, 最低分, 平均分 (保留一位小数)
def basic_score_statistics(score_list):
    """
    根据传入的成绩列表, 计算成绩最高分, 最低分, 平均分
    :param score_list: 传入的成绩列表
    :return: 最高分, 最低分, 平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    ave_score = round(sum(score_list) / len(score_list), 1)
    return max_score, min_score, ave_score

score_list = [100, 98, 89, 97, 95]
max_score, min_score, ave_score = basic_score_statistics(score_list)
print(f"最高分: {max_score}, 最低分: {min_score}, 平均分: {ave_score}")