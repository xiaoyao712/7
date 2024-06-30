# 随机函数输出012
# 遍历字典
# 获取指定时间
# 函数的定义
# 字符串的
'''
%f 字符串以浮点型输出
求实数平方根的函数sqrt
函数的名称不可以随便命名
turtle
字符串的索引 0开始
'''
'''
if else 

'''
# strip
'''
input() ,print()函数的额使用
if else:分支的使用
datetime模块获取当前的日期时间
怎么通过日历模块获取6月7日这个时间
今年高考是星期几
文件的读取与写入
建党100零3周年写入到文件里面
将这个操作去用函数实现def
'''
# 要写入的字符串
content = '建党100零3周年'

# 打开文件
file = open('anniversary.txt', 'w', encoding='utf-8')

# 写入内容
file.write(content)

# 关闭文件
file.close()





import calendar

# 指定年份
year = 2024

# 获取6月7日是星期几，0代表星期一，6代表星期日
weekday = calendar.weekday(year, 6, 7)

# 创建一个星期几的列表
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 输出结果
print(f"{year}年的6月7日是{weekdays[weekday]}")

