### BLACK JACK 21點遊戲 ###

import random

# 洗牌 (牌庫少於18張時會重新洗牌)
def shuffle():
    global cards
    if len(cards) < 18:
        print("洗牌中...")
        cards = []
        for k in keys:
            cards.append(k)
        random.shuffle(cards)
        return cards
    else:
        return cards

# 發牌
def deal(lst):
    lst.append(cards.pop())

# 遊戲初始
def start():
    print("♠♥♦♣ GAME START ♠♥♦♣")
    print()
    deal(player)
    deal(dealer)
    deal(player)

# 算牌
def point(lst):
    point = 0
    a_count = -1
    count_10 = 0
    for i in lst:
        point = point + dc[i]
    while point > 21:
        if "♠A" or "♥A" or "♦A" or "♣A" in lst:
            a_count = lst.count("♠A") + lst.count("♥A") + lst.count("♦A") + lst.count("♣A")
            if count_10 < a_count:
                point = point - 10
                count_10 = count_10 + 1
            else:
                break
        else:
            break
    
    return point

# 顯示
def show(lst=None):
    if lst == None:
        print("Dealer Hands:",dealer,"\t","Ponint=", dealer_point)
        print("Player Hands:",player,"\t","Ponint=", player_point)
    elif lst == player:
        print()
        print("Player Hands:",player,"\t","Ponint=", player_point)
    elif lst == dealer:
        print()
        print("Dealer Hands:",dealer,"\t","Ponint=", dealer_point)

# 要牌
def hit():
    global player_point
    deal(player)
    player_point = point(player)
    show(player)
    
    if player_point > 21:
        opt = "surrender"
        return opt
    elif len(player) == 5:
        opt = "stand"
        return opt
    else:
        print()
        opt = input("Hit or Stand or Surrender?")
        return opt

# 不要牌
def stand():
    global dealer_point
    dealer_point = point(dealer)
    show(dealer) # 掀開莊家第二張牌

    while dealer_point < 17 and len(dealer) <= 5: # 未滿17點強迫莊家要牌
        print("莊家未滿17點，強迫要牌")
        deal(dealer)
        dealer_point = point(dealer)
        show(dealer)

# 選擇
def option():
    global opt
    print()
    opt = input("Hit or Stand or Surrender?")
    while True:
        opt = opt.strip()
        if opt.lower() == "hit":
            opt = hit()

        elif opt.lower() == "stand":
            stand()
            return opt
        
        elif opt.lower() == "surrender":
            return opt
        
        else:
            print()
            print("請輸入", "Hit(要牌) or Stand(不要牌) or Surrender(投降)")
            opt = input("Hit or Stand or Surrender?")

# 判定勝負
def win(opt):
    if opt == "surrender":
        print("[ YOU LOSE... ]")
    elif opt == "stand":
        if dealer_point > 21:
            print("[ YOU WIN! ]")
        elif len(player) == 5 and player_point <= 21:
            if len(dealer) == 5:
                print("[ =PUSH= ]")
            else:
                print("[ YOU WIN! ]")
        elif len(dealer) == 5 and dealer_point <=21:
            print("[ YOU LOSE... ]")
        elif player_point <= 21 and dealer_point <= 21:
            if player_point > dealer_point:
                print("[ YOU WIN! ]")
            elif player_point == dealer_point:
                print("[ =PUSH= ]")
            elif player_point < dealer_point:
                print("[ YOU LOSE... ]")
            else:
                print("三層判定勝負錯誤")
        else:
            print("二層判定勝負錯誤")
    else:
        print("判定勝負錯誤")

# 再玩一次
def play_again():
    ans = input("是否再玩一次? Y/N")
    print()
    ans = ans.strip()
    if ans.lower() in ("yes", "y"):
        return True
    else:
        return False

keys = ("♠A","♠2","♠3","♠4","♠5","♠6","♠7",
       "♠8","♠9","♠10","♠J","♠Q","♠K",
       "♥A","♥2","♥3","♥4","♥5","♥6","♥7",
       "♥8","♥9","♥10","♥J","♥Q","♥K",
       "♦A","♦2","♦3","♦4","♦5","♦6","♦7",
       "♦8","♦9","♦10","♦J","♦Q","♦K",
       "♣A","♣2","♣3","♣4","♣5","♣6","♣7",
       "♣8","♣9","♣10","♣J","♣Q","♣K")

values = (11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10,
11,2,3,4,5,6,7,8,9,10,10,10,10)

dc = dict(zip(keys,values))

cards = []  #牌庫

while True:
    dealer = [] #莊家
    player = [] #玩家
    dealer_point = 0 #莊家點數
    player_point = 0 #玩家點數
    opt = ""

    cards = shuffle()
    start()
    player_point = point(player)
    dealer_point = point(dealer)
    show()
    deal(dealer) #發給莊家第二張牌(蓋牌狀態)
    opt = option()
    print()
    win(opt)
    if not play_again():
        print("BYE BYE ~")
        break

input("按下 Enter 鍵結束...")
