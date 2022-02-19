import time, os
import auto_player as player
from datetime import datetime

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
        re = player.find_touch_any(['challenge_1', 'challenge_2', 'daily_close_1'])
        if re == 'challenge_1' or re == 'challenge_2':
            print('进入关卡')
            time.sleep(3)
            flag_bc = player.find_touch_any(['infinite_tower_go', 'infinite_tower_cancel'])
            if flag_bc == 'infinite_tower_go':
                print('开始战斗')
                time.sleep(3)
            elif flag_bc == 'infinite_tower_cancel':
                print("等待钥匙恢复")
                time.sleep(900)

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

    count = 0
    while count < round:
        re = player.find_touch_any(['challenge_1', 'challenge_2', 'daily_close_1'])
        if re == 'challenge_1' or re == 'challenge_2':
            print('进入关卡')
            time.sleep(3)
            flag_bc = player.find_touch_any(['infinite_tower_go', 'infinite_tower_cancel'])
            if flag_bc == 'infinite_tower_go':
                print('开始战斗')
                time.sleep(3)
            elif flag_bc == 'infinite_tower_cancel':
                print("等待钥匙恢复")
                time.sleep(900)
                continue

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

        elif re == 'daily_close_1':
            print('每日刷新')
            time.sleep(12)
            re3 = player.find_touch_any(['daily_prize'])
            if re3 == 'daily_prize':
                print('获取签到奖励')
                time.sleep(12)
            re4 = player.find_touch_any(['daily_close_2'])
            if re4 == 'daily_close_2':
                print('关闭签到奖励')
                time.sleep(12)

        else:
            print('正在战斗中')
            time.sleep(30)


def da_luan_dou():
    flag1 = 0
    while flag1 == 0:
        re = player.find_touch_any(['explore'])
        if re == 'explore':
            flag1 = 1
            print('进入探索')
            time.sleep(2)
        else:
            print('请返回游戏主界面')
            time.sleep(2)
    flag2 = 0
    while flag2 == 0:
        re = player.find_touch_any(['battle_training'])
        if re == 'battle_training':
            flag2 = 1
            print('进入战斗训练')
            time.sleep(2)
        else:
            print('请返回探索界面')
            time.sleep(12)
    flag3 = 0
    while flag3 == 0:
        re = player.find_touch_any(['daluandou_1', 'daluandou_2'])
        if re == 'daluandou_1' or re == 'daluandou_2':
            flag3 = 1
            print('进入大乱斗')
            time.sleep(2)
        else:
            print('请返回战斗训练界面')
            time.sleep(12)
    day_week = datetime.now().weekday()
    day_week_output = day_week + 1
    if day_week == 0:
        player.find_touch_any(['daluandou_yue'])
    elif day_week == 1:
        player.find_touch_any(['daluandou_huo'])
    elif day_week == 3:
        player.find_touch_any(['daluandou_mu'])
    elif day_week == 4:
        player.find_touch_any(['daluandou_jin'])
    elif day_week == 5:
        player.find_touch_any(['daluandou_tu'])
    elif day_week == 6:
        player.find_touch_any(['daluandou_ri'])
    else:
        print('今天是星期' + str(day_week_output))
        print('今天没有大乱斗')
        menu()
    time.sleep(2)
    print('今天是星期' + str(day_week_output))

    while True:
        re = player.find_touch_any(['luandou_new'])
        if re == 'luandou_new':
            print('进入关卡')
            time.sleep(2)
            player.find_touch_any(['luandou_challenge'])
            time.sleep(12)

        flag4 = 0
        while flag4 == 0:
            re2 = player.find_touch_any(['skip'])
            if re2 == 'skip':
                print('结束战斗')
                time.sleep(12)
            else:
                print('战斗进行中')
                time.sleep(30)
            re3 = player.find_touch_any(['luandou_prize'])
            if re3 == 'luandou_prize':
                print('获取奖励')
                time.sleep(3)
                flag4 = 1

def menu(debug=False):

    menu_list = [
    [get_pictures, '获取当前屏幕截图'],
    [auto_play_akatsuki, '你游自动收菜测试'],   
    [airship_collect, '你游自动收菜'],
    [infinite_tower, '自动挂塔(15/30分钟自动消耗钥匙)(已废弃)'],
    [infinite_tower_key, '自动挂塔(内测版)'],
    [da_luan_dou, '大乱斗'],
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
