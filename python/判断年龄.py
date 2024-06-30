user_nl = int(input('请输入您的年龄：'))
age = int(18)
l = int(65)

if user_nl >= l:
    print('您已步入老年')
elif user_nl >= age:
    print('您已成年')
else:
    print('您还未成年')
