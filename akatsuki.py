import time, os
import auto_player as player

def get_pictures():   
    player.screen_shot()

def auto_play_akatsuki(round = 20):
    count = 0
    while count < round:
        ar1 = ['airship']
        re = player.find_touch_any(ar1)
        if re == 'airship':
            print('开始飞行船收菜')
        time.sleep(1)


def airship_collect(round = 20):
    count = 0
    while count < round:
        player.find_touch_any(['airship'])
        print('开始飞行船收菜')
        time.sleep(3)
        player.find_touch_any(['produce'])
        print('进入生产')
        time.sleep(1)
        player.find_touch_any(['collectall'])
        print('收取全部物品')
        time.sleep(1)
        player.touch([960, 760])
        print('返回')
        menu()

def infinite_tower(round = 2022):
    flag1 = 0
    while flag1 == 0:
        re = player.find_touch_any(['event'])
        if re == 'event':
            flag1 = 1
            print('进入活动')
            time.sleep(2)
        else:
            print('请返回游戏主界面')
            time.sleep(2)
    flag2 = 0
    while flag2 == 0:
        re = player.find_touch_any(['infinite_tower'])
        if re == 'infinite_tower':
            flag2 = 1
            print('进入无限之塔')
            time.sleep(12)
        else:
            print('请返回活动界面')
            time.sleep(12)

    count = 0
    while count < round:
        re = player.find_touch_any(['challenge_1', 'challenge_2'])
        if re == 'challenge_1' or re == 'challenge_2':
            print('进入关卡')
            time.sleep(3)
            player.find_touch_any(['infinite_tower_go'])
            print('开始战斗')
            if re == 'challenge_1':
                time.sleep(900)
            elif re == 'challenge_2':
                time.sleep(1800)
            flag3 = 0
            while flag3 == 0:
                re = player.find_touch_any(['infinite_tower_end'])
                if re == 'infinite_tower_end':
                    print('结束战斗')
                    time.sleep(12)
                else:
                    print('战斗进行中')
                    time.sleep(30)
                re2 = player.find_touch_any(['infinite_tower_prize'])
                if re2 == 'infinite_tower_prize':
                    print('获取奖励')
                    time.sleep(12)
                    flag3 = 1
        else:
            print('正在战斗中')
            time.sleep(30)

def infinite_tower_key(round = 2022):
    flag1 = 0
    while flag1 == 0:
        re = player.find_touch_any(['event'])
        if re == 'event':
            flag1 = 1
            print('进入活动')
            time.sleep(2)
        else:
            print('请返回游戏主界面')
            time.sleep(2)
    flag2 = 0
    while flag2 == 0:
        re = player.find_touch_any(['infinite_tower'])
        if re == 'infinite_tower':
            flag2 = 1
            print('进入无限之塔')
            time.sleep(12)
        else:
            print('请返回活动界面')
            time.sleep(12)

    # re0 = player.find_touch_any(['no_key', 'one_key'])
    # if re0 == 'no_key':
    #     print('等待钥匙回复30min')
    #     time.sleep(1800)
    # elif re0 == 'one_key':
    #     print('等待钥匙回复15min')
    #     time.sleep(900)

    count = 0
    while count < round:
        re = player.find_touch_any(['challenge_1', 'challenge_2'])
        if re == 'challenge_1' or re == 'challenge_2':
            print('进入关卡')
            time.sleep(3)
            player.find_touch_any(['infinite_tower_go'])
            print('开始战斗')
            flag3 = 0
            while flag3 == 0:
                re = player.find_touch_any(['infinite_tower_end'])
                if re == 'infinite_tower_end':
                    print('结束战斗')
                    time.sleep(12)
                else:
                    print('战斗进行中')
                    time.sleep(30)
                re2 = player.find_touch_any(['infinite_tower_prize'])
                if re2 == 'infinite_tower_prize':
                    print('获取奖励')
                    time.sleep(12)
                    flag3 = 1
            # re3 = player.find_touch_any(['no_key', 'one_key'])
            # if re3 == 'no_key':
            #     print('等待钥匙回复30min')
            #     time.sleep(1800)
            # elif re3 == 'one_key':
            #     print('等待钥匙回复15min')
            #     time.sleep(900)
        else:
            print('正在战斗中')
            time.sleep(30)

def menu(debug=False):

    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [auto_play_akatsuki, '你游自动收菜测试'],   
    [airship_collect, '你游自动收菜'],
    [infinite_tower, '自动挂塔(15/30分钟自动消耗钥匙)'],
    [infinite_tower_key, '自动挂塔(快速清钥匙)'],
    ]

    start_time = time.time()
    print('程序启动，当前时间', time.ctime(), '\n')
    while True:
        i = 0
        for func, des in menu_list:
            msg = str(i) + ": " + des + '\n'
            print(msg)
            i += 1
        #player.alarm(1)
        raw = input("选择功能模式：") if not debug else 1
        index = int(raw) if raw else 1
        func, des = menu_list[index]
        print('已选择功能： ' + des)
        func()

if __name__ == '__main__':
    menu()
