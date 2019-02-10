import os
#调用本地文件
import sys
# 结束当前程序的模块
def gequ(user):
    song_list = {"往后余生": 'E://马良 _ 孙茜茹 - 往后余生 (V0).mp3', "感谢你曾经来过": 'E://Ayo97 _ 阿涵 - 感谢你曾来过.mp3', "广东爱情故事": 'E://广东雨神 - 广东爱情故事.mp3', "爱上你是一个错": 'E://雨宗林 - 爱上你是一个错 (V0).mp3',
                 '美了美了': 'E://汤潮 _ 小沈阳 - 美了美了.mp3', '沙漠骆驼': 'E://展展与罗罗 - 沙漠骆驼.mp3', '生日礼物': 'E://江涛 - 生日礼物.mp3',
                 '单身情歌': 'E://林志炫 - 单身情歌.mp3', '过客': 'E://阿涵 - 过客.mp3',
                 'I love Poland': 'E://Hazel - I Love Poland.mp3'}
    #     # 用户输入歌单然后显示歌曲名称
    if user == '歌单':
        for k in song_list:
            # 当用户输入0的时候，遍历字典全部的间和值
            print(k, end=' ')
            print()
#第一步输入歌单 显示歌单列表

    else:
        print('请按提示操作，输入 歌单 获取歌曲列表，或者输入结束，关闭程序！')
        user = input('欢迎来到 高大侠 点歌系统,请输入 歌单 ,来获取播放列表 :')
    if user == '歌单':
        # 这是第二步
        for k in song_list:
            print(k ,end = ' ')
            print('')
    elif user == '结束':
        print('欢迎再次使用！')
        sys.exit()
#第三步
    a = input('输入歌曲名称：')
    a = song_list[a]
    # print(a)

    print('您选的歌曲为{0}'.format(a))
    #print('我要开始播放os了')# 提示程序运行到此环节
    os.startfile(a)

    a = input('请您继续输入歌曲名称,播放下一首,或者输入 结束 ,来结束本次运行：')


    for i in a:
        #循环a 当用户输入歌曲名称时 继续提示 a
        print('您选的歌曲为：{0}'.format(a))

        i = song_list[a]
        os.startfile(i)
        # -------------------------------------
        a = input('请您继续输入歌曲名称,播放下一首,或者输入 结束 ,来结束本次运行：')
        #print('您选的歌曲为：{0}'.format(a))
        #print('我又要开始播放os了')  # 提示程序运行到此环节
        i = song_list[a]
        os.startfile(i)
        continue

        i = '结束'
        #用户输入结束 运行sys.exit
        print('欢迎再次使用！')
        quit()
        #sys.exit(0)#结束程序运行
    #while  i == '结束':
        #print('欢迎再次使用！')

        #sys.exit()
user = input('欢迎来到 高大侠 点歌系统,请输入 歌单 ,来获取播放列表 :')
# user = '歌单'
gequ(str(user))
