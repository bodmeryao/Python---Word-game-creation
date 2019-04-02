# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 9:15:26 2018

@author: bodmer.Yao(Lehai Yao)
"""

# Game Assignment

# 1 on 1 basketball bullfight
''' 
A> Intro
This is a basketball game, in which who score 5 first win. 
Both Characters, player and robot, are created by the game randomly, where player's
character will be created follow player's choise.
THere will be no obvious win or lose of this game, since this is a basketball game.
The game you can play multiple times, that every time will be different.

B> Known Bugs/Errors:
None
'''

# Create character
import random as rd
print('''
      Welcome to the basketball fantasy!!!
      In this game you will play as a legendary streetball player in a game against
      the basketball legend, Bodmer.
      ''', end = '')
print('''
      It will be a one-on-one bull fight. One who scored 5 first, win!
      In each round you'll play a role of either deffender or offensive.
      Each round will have 3 steps, which are outside of 3-point line, 2-point area and painting area.
      Once you make the shoot, no matter whether you make it or not, this round is end.
      On the other word, there is no such thing as a rebound.
      Every 3-point shoot made, will be counted as 2.
      Everytime you fail a fake move or a dribble, you have no other options but to shoot.
      You charactor will be randomly created by computer, based on the player type you choose.
      Your rival, Bodmer, will be created totally random by computer.
      TIPS:
          1. Try to understand the charactor's data of both of your charactor and Bodmer,
          which will for sure be helpful.
          2. Use common sense to make decision will be cool.
      '''
      )
print('''
===============================================================================
''')
print('Now the game start!')

print('''
      There is a picture that you were smiling with a basketball hanging on the wall.
      It reminds you one of your best memories which is a one-on-one bullfight with 
      basketball legend Bodmer while you were young''')

print('''
      That was the day 20 years ago...''')
    
print('''
      Tell me which kind of player you were:
          1\. O'neil
          2\. GOAT Jordan
          3\. Curry
          4\. Garnett
          5\. King James
          6\. Dirk Nowizki''') 
pos_1 = int(input('>'))
        
# build a function for creating players
def player(pos,i):   
        
# build O'neil kind player
    if pos == 1:
        height = rd.randint(205,220)
        weight = rd.randint(130,170)
        speed = rd.randint(30,60)
        agility = rd.randint(30,50)
        power = rd.randint(80,100)
        jump = rd.randint(30,70)
        block = rd.randint(80,100)
        steal = rd.randint(30,50)
        shoot_3 = rd.randint(30,50)
        shoot_2 = rd.randint(30,70)
        dunk = rd.randint(80,100)
        skill = rd.randint(30,70)
# build Jordan kinda player 
    elif pos == 2:
        height = rd.randint(190,200)
        weight = rd.randint(80,110)
        speed = rd.randint(75,95)
        agility = rd.randint(80,95)
        power = rd.randint(50,70)
        jump = rd.randint(70,100)
        block = rd.randint(40,60)
        steal = rd.randint(70,95)
        shoot_3 = rd.randint(50,80)
        shoot_2 = rd.randint(75,95)
        dunk = rd.randint(50,70)
        skill = rd.randint(70,95)
# build Curry kinda player
    elif pos == 3:
        height = rd.randint(180,195)
        weight = rd.randint(70,85)
        speed = rd.randint(80,100)
        agility = rd.randint(80,100)
        power = rd.randint(30,60)
        jump = rd.randint(60,80)
        block = rd.randint(30,50)
        steal = rd.randint(75,95)
        shoot_3 = rd.randint(80,100)
        shoot_2 = rd.randint(80,100)
        dunk = rd.randint(30,50)
        skill = rd.randint(80,95)
# build Garnett
    elif pos == 4:
        height = rd.randint(200,215)
        weight = rd.randint(90,110)
        speed = rd.randint(50,80)
        agility = rd.randint(50,80)
        power = rd.randint(70,80)
        jump = rd.randint(60,90)
        block = rd.randint(80,95)
        steal = rd.randint(40,60)
        shoot_3 = rd.randint(70,90)
        shoot_2 = rd.randint(30,60)
        dunk = rd.randint(75,95)
        skill = rd.randint(60,80)
# build James
    elif pos == 5:
        height = rd.randint(198,210)
        weight = rd.randint(100,130)
        speed = rd.randint(60,90)
        agility = rd.randint(40,60)
        power = rd.randint(70,90)
        jump = rd.randint(70,90)
        block = rd.randint(60,80)
        steal = rd.randint(40,60)
        shoot_3 = rd.randint(70,90)
        shoot_2 = rd.randint(60,80)
        dunk = rd.randint(75,95)
        skill = rd.randint(70,90)
# build Dirk
    else: 
        height = rd.randint(200,215)
        weight = rd.randint(85,105)
        speed = rd.randint(40,70)
        agility = rd.randint(50,80)
        power = rd.randint(60,70)
        jump = rd.randint(50,70)
        block = rd.randint(60,75)
        steal = rd.randint(40,60)
        shoot_3 = rd.randint(80,100)
        shoot_2 = rd.randint(70,90)
        dunk = rd.randint(60,80)
        skill = rd.randint(60,80)

# Show data of player
    if i == 1:
        print(f''' 
              You player is created by system. Here is details of your player.
                  Height    :    {height} cm
                  Weight    :    {weight} kg
                  Speed     :    {speed}
                  Agility   :    {agility}
                  Power     :    {power}
                  Jump      :    {jump}
                  Block     :    {block}
                  Steal     :    {steal}
                  3-point   :    {shoot_3}
                  2-point   :    {shoot_2}
                  Dunk      :    {dunk}
                  Skill     :    {skill}''')
    elif i == 0:
        print(f'''
              Bodmer is created by system. Here is details of his.
                  Height    :    {height} cm
                  Weight    :    {weight} kg
                  Speed     :    {speed}
                  Agility   :    {agility}
                  Power     :    {power}
                  Jump      :    {jump}
                  Block     :    {block}
                  Steal     :    {steal}
                  3-point   :    {shoot_3}
                  2-point   :    {shoot_2}
                  Dunk      :    {dunk}
                  Skill     :    {skill}''')

    return (height,weight,speed,agility,power,jump,block,steal,shoot_3,shoot_2,dunk,skill);

# creat player 
player_1 = []
player_1 = player(pos_1,1)

# Help session ---need more details
print('Tell me if you need more information. (Y/N)')
info = input('>')

if info == 'Y' or info == 'y':
    print('''
          All character data will affect your player's performence directly.
          For instance, once your player is trying to steal the ball from 
          rival, the result of comparison of speed and agility, combined with
          the comparison of your steal and his skill will lead to whether you 
          will make it. 
          So, remember it or at least have a rough picture!''')
elif info != 'N' and info != 'n':
    print('Something is wrong, please do that one last time.')
    print('Tell me if you need more information. (Y/N)')
    h = input('>')

    if info == 'Y' or info == 'y':
        print('''
              All character data will affect your player's performence directly.
              For instance, once your player is trying to steal the ball from 
              rival, the result of comparison of speed and agility, combined with
              the comparison of your steal and his skill will lead to a posibility whether you 
              will make it. 
              So, remember it or at least have a rough picture!''')

# Block
input('<Press Enter to create player Bodmer, your rival.>')

# creat player 2
p_2 = rd.randint(1,6)
player_2 = []
player_2 = player(p_2,0)

# Information of comparison 
# Create function position for defination of player type
def position(i):
    if i == 1:
        posi = 'O\'neil'
    elif i == 2:
        posi = 'Jordan'
    elif i == 3:
        posi = 'Curry'
    elif i == 4:
        posi = 'Garnett'
    elif i == 5:
        posi = 'Lebron'
    else: 
        posi = 'Dirk'
    return posi;
print('Players comparison? (Y/N)', end = '')
comparison = input('>')

if comparison == 'Y' or comparison == 'y':
    print('''
          That\'ll be 10 dollars. 
          Press 1 to pay with Paypal.
          Press 2 to pay with Credit Card.
          Press 3 to pay with Check.''')
    input('>')
    input('Ha! Just kidding!!!')
    posi_1 = position(pos_1)
    posi_2 = position(p_2)
    print(f'''
    The type of your player is {posi_1} kinda player, and the type of Bodmer is {posi_2}.
          Height    :    ''',player_1[0]-player_2[0],'''
          Weight    :    ''',player_1[1]-player_2[1],'''
          Speed     :    ''',player_1[2]-player_2[2],'''
          Agility   :    ''',player_1[3]-player_2[3],'''
          Power     :    ''',player_1[4]-player_2[4],'''
          Jump      :    ''',player_1[5]-player_2[5],'''
          Block     :    ''',player_1[6]-player_2[6],'''
          Steal     :    ''',player_1[7]-player_2[7],'''
          3-point  :    ''',player_1[8]-player_2[8],'''
          2-point  :    ''',player_1[9]-player_2[9],'''
          Dunk      :    ''',player_1[10]-player_2[10],'''
          Skill     :    ''',player_1[11]-player_2[11],'''
          Choose your strategy wisely!!!''' )

input('<Press Enter to Continue>')



###############################################################################
###############################################################################
###############################################################################
              
# Creat judgements of each decision

###############################################################################
# Judgement for dribbling and steal
###############################################################################
def drib(a,b,c,d,e,f): # a for speed dif, b for agiltity dif, c for skill, d for steal, e and f for 3/2 shoot
    '''Inputs are speed difference, agility difference, skill of offence player, steal of def player and 2/3-shoot of off player'''
    speeddif = 0
    agildif = 0
    ski_ste = 0
    shootab = 0
    result = 10

# level speed difference    
    if a < 0:
        speeddif = 0
    elif a < 20:
        speeddif = 1
    elif a < 50:
        speeddif = 2
    else:
        speeddif = 3

# level agility difference
    if b < 0:
        agildif = 0
    elif b < 20:
        agildif = 1
    elif b < 50:
        agildif = 2
    else:
        agildif = 3

# level difference of skill and steal
    if (c - d) < 0:
        ski_ste = 0
    elif (c - d) < 20:
        ski_ste = 1
    elif (c - d) < 50:
        ski_ste = 2
    else:
        ski_ste = 3
    
# Add weight of shooting ability, which obviously will affect the defence
    shootab = (e+f)/2
    
# Give result 
    jf = speeddif + agildif + ski_ste
    
    if jf > 6:
        total = shootab / 2 + 10
    elif jf >3:
        total = shootab / 2
    else:
        total = shootab / 2 - 10
        
    judge = rd.randint(0,100)
    if total > judge:
        result = 1
    else:
        result = 0
    
    return result;
###############################################################################
#judgement for outer-shooting with deffence
###############################################################################
def oshoot(a,b,c,d,e,f):# a for 3/2 shoot, b for block, c for height dif, d for speed dif, e for jump dif, f for agility dif
    '''Inputs are 2/3-points shoot of off player, block of def player, difference of height/speed/jump/agility'''
 
# level difference of height 
    if c < -30:
        h = 1
    elif c < -10:
        h = 2
    elif c < 0:
        h = 3
    else:
        h = 4
 # level difference of speed
    if d < 30:
        s = 0
    else:
        s = 1
# level jump difference
    if e < -30:
        j = 1
    elif e < -10:
        j = 2
    elif e < 0:
        j = 3
    elif e < 10:
        j = 4
    else:
        j = 5
# level agility
    if f < 30:
        ag = 0
    else:
        ag = 1

# set up weight of shoot and block
    jf = h + s + j + ag
    
    if jf > 10:
        if a > b:
            total = a/2 + 15
        else:
            total = a/2 + 10
    elif jf > 8:
        if a > b:
            total = a/2 + 5
        else:
            total = a/2
    elif jf > 6:
        if a > b:
            total = a/2 - 5
        else:
            total = a/2 - 10
    else:
        if a > b:
            total = a/2 - 15
        else:
            total = a/2 - 20

# give result
    judge = rd.randint(0,100)
    if total > judge:
        result = 1
    else:
        result = 0
    
    return result;
    
###############################################################################   
# Judgement for inner-shooting with deffence
###############################################################################
def ishoot(a,b,c,d,e,f,g,i = 0):# a for 2 shoot, b for block, c for height dif, d for power dif, e for jump dif, 
                          # f for weight dif, g for dunk, i for dunk or shoot, 1 for dunk 0 for shoot
    '''Inputs are 2/3-points shoot of off player, block of def player, difference of height/speed/jump/agility'''
 
# level difference of height 
    if c < -30:
        h = 1
    elif c < -10:
        h = 2
    elif c < 0:
        h = 3
    else:
        h = 4
 # level difference of power
    if c < -30:
        p = 1
    elif c < -10:
        p = 2
    elif c < 0:
        p = 3
    else:
        p = 4
# level jump difference
    if e < -30:
        j = 1
    elif e < -10:
        j = 2
    elif e < 0:
        j = 3
    elif e < 10:
        j = 4
    else:
        j = 5
# level weight difference
    if c < -50:
        w = 1
    elif c < -20:
        w = 2
    elif c < 0:
        w = 3
    else:
        w = 4

# set up weight of shoot and block
    jf = h + p + j + w
    if i == 1:
        if jf > 15:
            if a > b:
                total = a/2 + 15
            else:
                total = a/2 + 10
        elif jf > 12:
            if a > b:
                total = a/2 + 5
            else:
                total = a/2
        elif jf > 8:
            if a > b:
                total = a/2 - 5
            else:
                total = a/2 - 10
        else:
            if a > b:
                total = a/2 - 10
    else:
        if jf > 15:
            if g > b:
                total = g/2 + 30
            else:
                total = g/2 + 20
        elif jf > 12:
            if g > b:
                total = g/2 + 10
            else:
                total = g/2
        elif jf > 8:
            if a > b:
                total = g/2 - 10
            else:
                total = g/2 - 20
        else:
            if a > b:
                total = g/2 - 20
            else:
                total = g/2 - 30 

# give result
    judge = rd.randint(0,100)
    if total > judge:
        result = 1
    else:
        result = 0
    
    return result;    

###############################################################################
# Judgement for free-shoot
###############################################################################
def fshoot(a): # a for 3/2 shoot
    shoot = a / 2 + 40

# give result
    total = shoot
    judge = rd.randint(0,100)
    if total >= judge:
        result = 1
    else:
        result = 0
    
    return result;    

###############################################################################
# Judgement for fake-shoot
###############################################################################
def fake(a): #a for 3/2 shoot
    if a >= 80:
        fake = 80
    elif a >= 60:
        fake = 50
    else:
        fake = 0
    judge = rd.randint(0,100)
    if fake >= judge:
        result = 1
    else:
        result = 0
    return result;
    
###############################################################################
###############################################################################
###############################################################################
# creat list playerd, which is difference between
###############################################################################
playerd = []
player_1 = list(player_1)
player_2 = list(player_2)
for i in range(0,11):
    playerd.append(player_1[i] - player_2[i])
###############################################################################   
# Player offense
###############################################################################
     
def off():
     
    r = 3
    result = 0
    d = 1
    print('''
          Now you hold the ball and look directly into Bodmer's eyes.
          It is the time for you to make up your mind for your first move!''')
    while r != 0: # Creat Loop for 3 steps game
        if r == 3: # First step of the game, which is outside the 3-point line
            print('''
                  Now you are holding the ball behind the three-point line. What you wanna do?
                      1. 3-point shoot fake move
                      2. Dribbling inside
                      3. Make the 3-point shoot''', end = '')
            c = int(input('>'))
        elif r == 2:
            if d == 1: # 2-Point area, and d stands for with defender
                print('''
                      Now you are inside of 2-point area. What is your next move?
                              1. 2-point shoot fake move
                              2. Dribbling inside
                              3. Make the 2-point shoot''', end = '')
                c = int(input('>'))
            elif d == 0: # 2-Point area, and d stands for without defender
                print('''
                      Now you are all free in 2-point area. What is your next move?
                              2. Dribbling inside
                              3. Make the 2-point shoot''', end = '')
                c = int(input('>'))
        else: # Painting area
            print('''
                  Now you get into the painting area. What is your choice now?
                          1. Fake move
                          3. Shoot 
                          4. Dunk''', end = '')
            c = int(input('>'))

        if c == 1: # Fake move
            if r == 3: # if loop for judge of 3-point or 2-point
                n = fake(player_1[8])
            else:
                n = fake(player_1[9])
            if n == 1: # the result of fake move, getting from the function
                if r != 1: # Not in Painting area
                    print('''
                          You made one good fake move and totally fooled him.
                          Now you get rid of the defender, what is your next step?
                                  1. Make the free shoot
                                  2. Dribbling in side''', end = '')
                    j = int(input('>'))
                    if j == 1:
                        result = fshoot(player_1[8]) # result of free shoot
                        place = r  # place is used to record where player made the shoot
                        r = 0 # While loop ends
                        print('''
                              You took the chance of clear shoot and make a nice shoot''')
                    else:
                        r = r - 1 # Get one step further
                        d = 0 # since the dribbling move made, the defender is assumed to be lost.
                        print('''
                              You dribbling inside with Bodmer fall behind you.''')
                else:
                    print('''
                          Bodmer is now nowhere!!! Make the free shoot!!!''')    
                    result = 1
                    q = input('DUNK? Or Hook? D/H >')
                    if q == 'D':
                        place = r - 1
                        r = 0
                    else:
                        place = r
                        r = 0
            else:
                print('''
                      Bodmer don't buy it at all! You have to make the tough shoot now.''') # fake move fails, only option is to shoot
                if r == 3:
                    result = oshoot(player_1[8],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 3
                    r = 0
                elif r == 2:
                    result = oshoot(player_1[9],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 2
                    r = 0
                else:
                    result = ishoot(player_1[9],player_2[6],playerd[0],playerd[4],playerd[5],playerd[1],player_1[10])
                    place = 1
                    r = 0
        elif c == 2: # Dribbling inside
            n = drib(playerd[2],playerd[3],player_1[11],player_2[7],player_1[8],player_1[9])
            if n == 1:
                if playerd[2] > 20: # if the speed difference between two players is higher than 20, a successful dribbling will lose defender
                    d = 0
                    print('''
                          You made a nice cross-over and get pass Bodmer as a flash! You finished him!''')
                else:
                    print('''
                          Though you got pass Bodmer with a nice move, you cannot get rid of him and he is still
                          right behind you!''')
                r = r - 1 # dribbling inside
            else:
                print('''
                      You cannot get pass Bodmer, now you have to make the tough shoot!''')
                if r == 3:
                    result = oshoot(player_1[8],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 3
                    r = 0
                elif r == 2:
                    result = oshoot(player_1[9],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 2
                    r = 0
                else:
                    result = ishoot(player_1[9],player_2[6],playerd[0],playerd[4],playerd[5],playerd[1],player_1[10])
                    place = 1
                    r = 0
        elif c == 3:# Simply make the shoot
            print('''
                  You decided to shoot right away!''')
            if d == 0:
                if r == 3:
                    result = fshoot(player_1[8])
                    place = r
                    r = 0
                elif r == 1:
                    result = 1
                    place = 0
                    r = 0
                else:
                    result = fshoot(player_1[9])
                    place = r
                    r = 0
            else:
                if r == 3:
                    result = oshoot(player_1[8],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 3
                    r = 0
                elif r == 2:
                    result = oshoot(player_1[9],player_2[6],playerd[0],playerd[2],playerd[5],playerd[3])
                    place = 2
                    r = 0
                else:
                    result = ishoot(player_1[9],player_2[6],playerd[0],playerd[4],playerd[5],playerd[1],player_1[10])
                    place = 1
                    r = 0
        else: # Dunk 
            print('''
                  You decided to make a slamdunk!''')
            result = ishoot(player_1[9],player_2[6],playerd[0],playerd[4],playerd[5],playerd[1],player_1[10],1)
            place = 0
            r = 0    
    return result,place; # The output is the result of whether this round of offense is succeed and the place this round ends

###############################################################################
# Deffense round    
###############################################################################

def deff():
    
    r = 3 #initialize
    d = 1
    result = 0
    place = 0
    
    print('''
          Bodmer is holding the ball in front of you, he's looking at you with 
          a smile. Suddenly, seems like he has made up his mind and start his first
          move!''', end = '')
    input(' Now he is starting the game!')

    while r != 0:
        # step 1
        if r == 3:
            # make choice for Bodmer.
            # if Bodmer is not a 3-point shooter, there is no need for him to play fake move or 3-point shoot.
            if player_2[8] < 65: 
                c = 2 
            else:
                c = rd.randint(1,3)
                # Indentify the move
            if c != 2:
                print('''
                      Bodmer is looking direct towards the hoop for a while. He suddenly
                      raise both his hands with the ball and take his right foot fall away.
                      It seems like he's about to make the 3-point shoot!
                      What will be you reaction now?
                      1. You jump hard to make a nice block, though it may cause you a losing
                      of position, which means you lose your defense.
                      2. You just stand there steady, beware for a fake move.''', end = '')
                a = int(input('>'))
            else:
                print('''
                      Bodmer starts dribbling the ball with some kind of rhythm, looking for
                      a perfect opportunity of attacking. He is trying to dribbling pass you!
                      What is your next move?
                      1. You try to make a steal, with a risk of totally lose your defense
                      2. Do nothing and keep you attention on his move. He starts his move 
                      and you follow him tightly, without losing deffense.''', end = '')
                a = int(input('>'))
                # give result of first round
            if c == 1:
                if a == 1:
                    d = 0
                    r = r - 1
                    print('''
                          Oh no! That is a fake move and Bodmer totally fooled you! Now
                          he is all free!!!''', end = '')
                elif a == 2:
                    print('''
                          Bodmer does make that shoot and that is for sure a fake move.
                          You definitely saw through him. Now he has no choice but to make
                          the shoot''', end = '')
                    result = oshoot(player_2[8],player_1[6],-playerd[0],-playerd[2],-playerd[5],-playerd[3])
                    place = r
                    r = 0
            elif c == 2:
                if a == 1:
                    n = drib(-playerd[2],-playerd[3],player_2[11],player_1[7],player_2[8],player_2[9])
                    if n == 0:
                        r = 0
                        print('''
                              You made it!!! What a superb steal!!!''', end = '')
                    else:
                        d = 0
                        print('''
                              He used a wonderful cross over to get pass you and left you all 
                              behind!''', end = '')
                        r = r - 1
                elif a == 2:
                    r = r - 1
                    print('''
                          You followed him get into the 2-point area''', end = '')
            elif c == 3: 
                if a == 1:
                    print('''
                          He was doing the 3-point shoot. You jumped as high as you can
                          to block him.''', end = '')
                    result = oshoot(player_2[8],player_1[6],-playerd[0],-playerd[2],-playerd[5],-playerd[3])
                    place = r
                    r = 0
                else:
                    print('''
                          He made the shoot without your effort of deffense. It was a clean shoot!''', end = '')
                    result = fshoot(player_2[8])
                    place = r
                    r = 0
        # Bodmer make it in 2-point area
        if r == 2:
            input('''
                  Now Bodmer make it into 2-point shooting area!''')
            # He lost defense and made the shoot
            if d == 0:
                print(''' Once Bodmer find out he totally lost your defense, he made the
                      shoot right away!!!''')
                result = fshoot(player_2[9])
                place = r
                r = 0
            else:
                # randomly decide to stop the ball and shoot or to keep dribbling
                c = rd.randint(1,3)
                if c != 2:
                    print('''
                          He stop dribbling and start the move of shooting!!!
                          What will be your next move?
                          1. You jump hard to make a nice block, though it may cause you a losing
                          of position, which means you lose your defense.
                          2. You just stand there steady, beware for a fake move. ''')
                    a = int(input('>'))
                    if c == 1:
                        if a == 1:
                            d = 0
                            r = 0
                            place = 2
                            print('''
                                  Fake move!!! He earned himself a lot of space for free shooting!!!''')
                            result = fshoot(player_2[9])
                        elif a == 2:
                            print('''
                                  You got him! It was a fake move! He had to make a tough shoot with 
                                  your defense.''')
                            r = 0
                            result = oshoot(player_2[9],player_1[6],-playerd[0],-playerd[2],-playerd[5],-playerd[3])
                            place = 2
                    elif c == 3:
                        if a == 1:
                            print('''
                                  He make the shoot with your tight defense!''')
                            result = oshoot(player_2[9],player_1[6],-playerd[0],-playerd[2],-playerd[5],-playerd[3])
                            place = r
                            r = 0
                        else:
                            print('''It is a clean shoot without your deffense!!!''')
                            result = fshoot(player_2[9])
                            place = r
                            r = 0 
                    else:
                        print('''
                              There is no sign of his stoping. It seems like he will keep dribbling!
                              What will you do?
                              1. You try to make a steal, with a risk of totally lose your defense
                              2. Do nothing and keep you attention on his move. He starts his move 
                              and you follow him tightly, without losing deffense.''')
                        a = int(input('>'))
                        if a == 1:
                            n = drib(-playerd[2],-playerd[3],player_2[11],player_1[7],player_2[8],player_2[9])
                            if n == 0:
                                r = 0
                                print('''
                                      You made it!!! What a superb steal!!!''')
                            else:
                                d = 0
                                print('''
                                      He used a wonderful cross over to get pass you and left you all 
                                      behind!''')
                                r = r - 1
                        else:
                            r = r - 1
                            print('''
                                  Now you followed him to painting area!''')
        if r == 1:
            input('''
                  Now you followed him into painting area.''')
            if d == 0:
                print('''
                      You can no longer stop him now. Bodmer is all alone in the dunk area.''')
                r = 0
                place = 0
                result = 1
            else:
                print('''
                      Now you are all in the painting area. It seems like a close fighting is inevasible!!!''')
                input('''Game is keep going''')
                print('''
                      Bodmer makes a fancy footwork, what will you do now?
                      1. You try to make a steal
                      2. You just follow his move''', end = '')
                a = int(input('>'))
                if a == 1:
                    n = drib(-playerd[2],-playerd[3],player_2[11],player_1[7],player_2[8],player_2[9])
                    if n == 0:
                        print('''
                              You stop him with a steal!!
                              What a superb steal!!!''', end = '')
                        r = 0
                        place = 1
                    else:
                        print('''
                              He fooled you and won a lot of space for himself!''')
                        result = 1
                        r = 0
                        place = 1
                else:
                    c = rd.randint(0,1)
                    if c == 1:
                        print('''
                              I cannot believe it!!! Bodmer is seeking for a forced slam dunk!!!''')
                        place = 0
                    else:
                        print('''
                              Bodmer decided to play a baby hook.''')
                        place = 1
                    
                    result = ishoot(player_2[9],player_1[6],-playerd[0],-playerd[4],-playerd[5],-playerd[1],player_2[10],c)
                    r = 0
    return result,place;

###############################################################################
# define fail function
###############################################################################

def fail():
    print('''
          Though you lost the game against Bodmer, it was one of most exciting
          game you ever had! After all, such experience playing against legend Bodmer
          was not that everyone can have.''')
###############################################################################

###############################################################################
# Game Start
###############################################################################
###############################################################################
    
# Start the game with flip a coin
print('''
      Now it is time to flip a coin to decide who is going to start in front.''')
print('''
      Choose Head or Tail.(H/T)''',end = '')
ht = input('>')

# Flip the coin
i = rd.randint(0,1)
if i == 0:
    ht_0 = 'H'
else: ht_0 = 'T'

# Compare the choice and the coin
x = 0
while x == 0:
    if ht == ht_0:
        playerstart = 1
        x = 1
        if ht_0 == 'T':
            print('''
                  It is Tail! You\'ll start the game! Bravo!!''')
        else:
            print('''
                  It is Head! You\'ll start the game! Bravo!!''')
    elif ht !='H':
        if ht != 'T':
            print('''
                  Something is wrong! Please input H/T!''') 
            ht = input('>')
    else:
        playerstart = 0
        x = 1
        if ht_0 == 'T':
            print('''
                  It is Tail! Bodmer will start the game!''')
        else:
            print('''
                  It is Head! Bodmer will start the game!''')

input('<Press Enter to continue>')
    
###############################################################################

import pandas as pd

score_p = 0
score_b = 0
score = 0
statement = []
state_p = []
state_b = []
    
while score < 5:
    gameboard = []
    if playerstart == 1:
        gameboard = off()
        state_p.append(gameboard)
        state_b.append([0,0])
        input('<Press Enter to continue>')
        if gameboard[0] == 1:
            playerstart = 0
            if gameboard[1] == 0:
                score_p = score_p + 1
                print(''' 
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                Boom!!! Nice DUNK!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXX
                         XXXXXXXXXXXXXXXXX                SCORE!!!
                          XXXXXXXXXXXXXXXX
                           XXXXXXXXXXXXXXXX
                            xXXXXXXXXXXXXXX
                            
                                oooPOOqooo
                              ooOOPOOOOqOOoo
                             oOOOPOOOOOOqOOOo
                            oOOOPOOOOOOOOqOOOo
                             oOOOPOOOOOOqOOOo
                              ooOOPOOOOqOOoo
                                oooPOOqooo
                                   ooOoo''')    
            elif gameboard[1] == 1:
                score_p = score_p + 1
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Nice Hook from inside!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
            elif gameboard[1] == 2:
                score_p = score_p + 1
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Nice shoot!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
            else:
                score_p = score_p + 2
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 You scored from downtown!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
        else:
            print('''
                  You didn\'t make it this round, now keep focus on defending!''')
            playerstart = 0
    else:
        gameboard = []
        gameboard = deff()
        state_p.append([0,0])
        state_b.append(gameboard)
        statement.append(gameboard)
        input('<Press Enter to continue>')
        playerstart = 1
        if gameboard[0] == 1:
            score_b = score_b + 1
            if gameboard[1] == 0:
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Nice Hook from inside by Bodmer!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
            elif gameboard[1] == 1:
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Nice Hook from inside by Bodmer!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
            elif gameboard[1] == 2:
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Nice shoot from Bodmer!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
            else:
                score_b = score_b + 1
                print('''
                      _____________________
                      |LLLLLLLLLLLLLLLLLLL|                 Bodmer scored from downtown!!!!      
                        XXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXX                SCORE!!!
                             XXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXX
                                xXXXXXXXXXXXXXX
                                
                                      oooPOOqooo
                                    ooOOPOOOOqOOoo
                                   oOOOPOOOOOOqOOOo
                                  oOOOPOOOOOOOOqOOOo
                                   oOOOPOOOOOOqOOOo
                                    ooOOPOOOOqOOoo
                                      oooPOOqooo
                                         ooOoo''')
        else:
            print('''
                  Bodmer did not score this round! 
                  Now it's your turn to fight back''')
    
    print(f'''
          Now the score is
          You      :   ''',score_p)
    print('''
          Bodmer   :   ''',score_b)
    input('<Press Enter to continue next round>')
    score = max(score_p,score_b)

###############################################################################
# Game statement creation
###############################################################################

report = []
statement = {'player' :state_p,'Bodmer' :state_b}
report = pd.DataFrame(statement)

###############################################################################

if score_p > score_b:
    print('''
          You won that game against Legend Bodmer, which was one big news by then.
          It even earned a chance of trial invitation from Golden State Warrior! It is one of 
          the moments that you proud of all time!''')
else:
    fail()

###############################################################################
# After game analysis
###############################################################################

m = int(input('''
              Press \'1\' if you want to see the game statement.
              Press \'2\' if not.
              '''))
v = 0
while v != 1:
    if m == 1:
        print(report)
        print('''
              The first number in \'()\' means the result of this round, 1 for score and 0 for nothing.
              The second number in \'()\' means the place you made the shoot.
              3 for 3-point shoot,
              2 for 2-point shoot,
              1 for painting area shoot,
              and 0 for a dunk''')
        v = 1   
    elif m == 2:
        v = 1
    else:
        print('''
              Sorry, you may make a mistake. Please do that again.''')

###############################################################################

print('''
      Now the game is over. 
      Hope you enjoy yourself during the time!!!
      ''')

###############################################################################
       
                
                
        
                
                
            
        
            
            
                    
                        
                
            
            
            
        
        
        




















    


        







    