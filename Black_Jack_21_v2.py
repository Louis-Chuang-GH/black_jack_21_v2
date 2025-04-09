### BLACK JACK 21點遊戲 ###

import random

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
dealer = []  #莊家
player = []  #玩家
dealer_point = 0  #莊家點數
player_point = 0  #玩家點數


# 洗牌 (牌庫少於18張時會重新洗牌)
def shuffle():
    global cards
    if len(cards) < 18:
        cards = []
        for k in keys:
            cards.append(k)
        random.shuffle(cards)
        return cards
    else:
        return cards

# 遊戲初始
def start():
    print("♠♥♦♣ GAME START ♠♥♦♣")
    print()
    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())

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
        print("Player Hands:",player,"\t","Ponint=", player_point)
    elif lst == dealer:
        print("Dealer Hands:",dealer,"\t","Ponint=", dealer_point)
        
        

# 發牌
def deal(lst):
    lst.append(cards.pop())

# 選擇
def option():
    ans = input("Hit or Stand or Surrender?")
    while True:
        ans = ans.strip()
        if ans == "Hit" or "HIT" or "hit":
            deal(player)
            player_point = point(player)
            show(player)
        elif ans == "Stand" or "STAND" or "stand":
            deal(dealer)
            dealer_point = point(dealer)
            show(dealer)

            
        elif ans == "Surrender" or "SURRENDER" or "surrender":
            print("YOU LOSE")
            break
        else:
            print("請輸入", "Hit(要牌) or Stand(不要牌) or Surrender(投降)")
            ans = input("Hit or Stand or Surrender?")
    

cards = shuffle()
start()
player_point = point(player)
dealer_point = point(dealer)
show()

# deal()

"""

#發牌
print()
Player.append((Cards.pop()))
Player_Point += D[Player[-1]]
Dealer.append((Cards.pop()))
Dealer_Point += D[Dealer[-1]]
Player.append((Cards.pop()))
Player_Point += D[Player[-1]]

print("Dealer Hands:",Dealer,"\t","Ponint=", Dealer_Point)
print("Player Hands:",Player,"\t","Ponint=", Player_Point)

#Hit要牌 / Stand不要牌 / Surrender投降
print()
print("Hit or Stand or Surrender?")
Option = input()
while True:
    if Option == "Hit":
        Player.append((Cards.pop()))
        Player_Point += D[Player[-1]]
        if Player_Point <= 21:
            if len(Player) == 5:  #過五關
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                Option = "Stand"
                continue
            print("Player Hands:",Player,"\t","Ponint=", Player_Point)
            print("Hit or Stand or Surrender?")
            Option = input()
        elif Player_Point > 21:
            if Player.count("♠A") > 0:
                Player[Player.index("♠A")]="♠A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♥A") > 0:
                Player[Player.index("♥A")]="♥A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♦A") > 0:
                Player[Player.index("♦A")]="♦A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            elif Player.count("♣A") > 0:
                Player[Player.index("♣A")]="♣A."
                Player_Point-= 10
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                if len(Player) == 5:
                    Option = "Stand"
                    continue
                print("Hit or Stand or Surrender?")
                Option = input()
            else:
                print("Player Hands:",Player,"\t","Ponint=", Player_Point)
                break
    elif Option == "Stand":
        while Dealer_Point < 17:  #未滿17點強迫莊家要牌
            Dealer.append((Cards.pop()))
            Dealer_Point += D[Dealer[-1]]
            if Dealer_Point > 21:  #爆牌時判斷莊家是否有A
                if Dealer.count("♠A") > 0:
                    Dealer[Dealer.index("♠A")]="♠A."
                    Dealer_Point-= 10
                elif Dealer.count("♥A") > 0:
                    Dealer[Dealer.index("♥A")]="♥A."
                    Dealer_Point-= 10
                elif Dealer.count("♦A") > 0:
                    Dealer[Dealer.index("♦A")]="♦A."
                    Dealer_Point-= 10
                elif Dealer.count("♣A") > 0:
                    Dealer[Dealer.index("♣A")]="♣A."
                    Dealer_Point-= 10
                elif len(Dealer) ==5:  #過五關
                    break
        print("Dealer Hands:",Dealer,"\t","Ponint=", Dealer_Point)
        break
    elif Option == "Surrender":
        print("YOU LOSE")
        break
    else:
        print("請輸入", "Hit(要牌) or Stand(不要牌) or Surrender(投降)")
        Option = input()

#判斷勝負  #PUSH平手
if Option != "Surrender":
    if len(Player) == 5:
        if Player_Point <= 21 :
            if len(Dealer) == 5:
                print("PUSH")
            elif Dealer_Point == 21:
                print("PUSH")
            else:
                print("YOU WIN")
        else:
            print("YOU LOSE")
    else:
        if Dealer_Point <= 21:
            if Player_Point <= 21:
                if Player_Point == 21 and len(Dealer) ==5:
                    print("PUSH")
                elif Player_Point > Dealer_Point and len(Dealer) !=5:
                    print("YOU WIN")
                elif Player_Point == Dealer_Point and len(Dealer) !=5:
                    print("PUSH")
                else:
                    print("YOU LOSE")
            else:
                print("YOU LOSE")
        else:
            print("YOU WIN")

input("按下 Enter 鍵結束...")

#Play Again?



"""
