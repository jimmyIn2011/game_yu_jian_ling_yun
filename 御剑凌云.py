# 境界：练气、筑基、金丹、元婴、化神、炼虚、合体、大乘、渡劫、飞升、散仙、人仙、地仙、天仙、金仙、仙王、仙皇、仙尊、仙圣、仙帝 区域划分：0~150;200、250、300、350、400、450、500、550、600
# 颜色：白-》练气、筑基、金丹、元婴；绿-》化神、炼虚、合体；蓝-》大乘、渡劫、飞升；紫-》散仙、人仙、地仙；橙-》天仙、金仙；黑色-》仙王、仙皇；金色-》仙尊、仙圣；彩-》仙帝 EXP-》30 100 200 500 1000
# 2000 3500 6000 9000 14000 20000 40000 65000 100000 195000 300000 500000 1000000 5000000 10000000
import pygame as pg
import random as rd

pg.init()
pg.display.init()
screen = pg.display.set_mode([800, 800])
pg.display.set_caption("御剑凌云")
running = True
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
RED = [255, 0, 0]
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GOLDEN = (205, 127, 50)
ch = ["凡人", "练气", "筑基", "金丹", "元婴", "化神", "炼虚", "合体", "大乘", "渡劫", "飞升", "散仙", "人仙", "地仙",
      "天仙", "金仙",
      "仙王", "仙皇", "仙尊", "仙圣", "仙帝"]
ji = [30, 100, 200, 500, 1000, 2000, 3500, 6000, 9000, 14000, 20000, 40000, 65000, 100000, 195000, 300000,
      500000, 1000000, 5000000, 10000000]
myself = pg.image.load("./character.png")
imgs = [[pg.image.load("./danyao1.png"), pg.image.load("./renshen.png")],
        [pg.image.load("./yaoshou1.png")], [pg.image.load("./shit.png")]]
mymap = []
mapjs = 0
place = 0
while mapjs < 10000000:
    place += 4
    if mapjs == 0:
        nk = [[1, rd.randint(1, 100), [place * 100 + 200, 100], rd.choice(imgs[0])], [1, rd.randint(1, 100),
                                                                                      [place * 100 + 200, 500],
                                                                                      rd.choice(imgs[0])]]
        # [tpe, num, img]  tpe->1 仙药/灵丹;tpe->2 妖魔;tpe->3 毒丹;
        mapjs += max(nk[0][1], nk[1][1])
        mymap.append(nk)
    else:
        nk = [[rd.choice([1, 1, 2, 3]), rd.randint(1, int(mapjs * 1.2)), [place * 100 + 200, 100]],
              [rd.choice([1, 1, 2, 3]),
               rd.randint(1, int(mapjs * 1.2)),
               [place * 100 + 200, 500]]]
        nk[0].append(rd.choice(imgs[nk[0][0] - 1]))
        nk[1].append(rd.choice(imgs[nk[1][0] - 1]))
        if nk[0][0] != 1:
            nk[0][1] = - nk[0][1]
        if nk[1][0] != 1:
            nk[1][1] = - nk[1][1]
        while mapjs + max(nk[0][1], nk[1][1]) < 0:
            nk = [[rd.choice([1, 1, 2, 3]), rd.randint(1, int(mapjs * 1.2)), [place * 100 + 200, 100]],
                  [rd.choice([1, 1, 2, 3]),
                   rd.randint(1, int(mapjs * 1.2)),
                   [place * 100 + 200, 500]]]
            nk[0].append(rd.choice(imgs[nk[0][0] - 1]))
            nk[1].append(rd.choice(imgs[nk[1][0] - 1]))
            if nk[0][0] != 1:
                nk[0][1] = - nk[0][1]
            if nk[1][0] != 1:
                nk[1][1] = - nk[1][1]
        mapjs += max(nk[0][1], nk[1][1])
        mymap.append(nk)
jj = 0
scene = 1
mes = 275
win = False
score = 0
start = pg.Rect(300, 400, 200, 100)
while running:
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if pg.key.get_pressed()[pg.K_w] or pg.key.get_pressed()[pg.K_UP]:
            mes -= 30 if mes >= 100 else 0
        elif pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
            mes += 30 if mes < 500 else 0
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if start.collidepoint(pos) and scene == 1:
                scene = 2
            elif start.collidepoint(pos) and scene == 3:
                scene = 1
                jj = 0
                win = False
                score = 0
                mymap = []
                mapjs = 0
                place = 0
                while mapjs < 10000000:
                    place += 4
                    if mapjs == 0:
                        nk = [[1, rd.randint(1, 100), [place * 100 + 200, 100], rd.choice(imgs[0])],
                              [1, rd.randint(1, 100),
                               [place * 100 + 200, 500],
                               rd.choice(imgs[0])]]
                        # [tpe, num, img]  tpe->1 仙药/灵丹;tpe->2 妖魔;tpe->3 毒丹;
                        mapjs += max(nk[0][1], nk[1][1])
                        mymap.append(nk)
                    else:
                        nk = [[rd.choice([1, 1, 2, 3]), rd.randint(1, int(mapjs * 1.2)), [place * 100 + 200, 100]],
                              [rd.choice([1, 1, 2, 3]),
                               rd.randint(1, int(mapjs * 1.2)),
                               [place * 100 + 200, 500]]]
                        nk[0].append(rd.choice(imgs[nk[0][0] - 1]))
                        nk[1].append(rd.choice(imgs[nk[1][0] - 1]))
                        if nk[0][0] != 1:
                            nk[0][1] = - nk[0][1]
                        if nk[1][0] != 1:
                            nk[1][1] = - nk[1][1]
                        while mapjs + max(nk[0][1], nk[1][1]) < 0:
                            nk = [[rd.choice([1, 1, 2, 3]), rd.randint(1, int(mapjs * 1.2)), [place * 100 + 200, 100]],
                                  [rd.choice([1, 1, 2, 3]),
                                   rd.randint(1, int(mapjs * 1.2)),
                                   [place * 100 + 200, 500]]]
                            nk[0].append(rd.choice(imgs[nk[0][0] - 1]))
                            nk[1].append(rd.choice(imgs[nk[1][0] - 1]))
                            if nk[0][0] != 1:
                                nk[0][1] = - nk[0][1]
                            if nk[1][0] != 1:
                                nk[1][1] = - nk[1][1]
                        mapjs += max(nk[0][1], nk[1][1])
                        mymap.append(nk)
    if scene == 2:
        screen.blit(pg.image.load("./bj2.jpg"), [0, 0])
        for i in range(len(mymap)):
            if mymap[i][0] != 0:
                mymap[i][0][2][0] -= 2
                mymap[i][1][2][0] -= 2
                screen.blit(mymap[i][0][3], mymap[i][0][2])
                if mymap[i][0][2][0] <= 800:
                    screen.blit(pg.font.SysFont("华文楷体", 30).render(str(mymap[i][0][1]), True, YELLOW),
                                [mymap[i][0][2][0],
                                 mymap[i][0][2][1] - 40])
                    screen.blit(pg.font.SysFont("华文楷体", 30).render(str(mymap[i][1][1]), True, YELLOW),
                                [mymap[i][1][2][0],
                                 mymap[i][1][2][1] - 40])
                screen.blit(mymap[i][1][3], mymap[i][1][2])
                if mymap[i][0][2][0] <= 141 and mes <= 400 - 71:
                    score += mymap[i][0][1]
                    mymap[i] = [0, 0]
                    if score >= ji[jj]:
                        jj += 1
                    elif score < ji[jj - 1] and jj != 0:
                        jj -= 1
                elif mymap[i][1][2][0] <= 141 and mes > 400 - 71:
                    score += mymap[i][1][1]
                    mymap[i] = [0, 0]
                    if score >= ji[jj]:
                        jj += 1
                    elif score < ji[jj - 1] and jj != 0:
                        jj -= 1
        screen.blit(myself, [0, mes])
        screen.blit(pg.font.SysFont("华文楷体", 20).render(str(score), True, BLACK), [20, mes - 70])
        if score < 0:
            scene = 3
        elif score >= 10000000:
            scene = 3
            win = True
        screen.blit(pg.font.SysFont("华文楷体", 20).render(ch[jj], True, YELLOW), [20, mes - 40])
    elif scene == 1:
        screen.blit(pg.image.load("./bg.jpg"), [0, 0])
        pg.draw.rect(screen, GREEN, start, 1)
        if start.collidepoint(pg.mouse.get_pos()):
            pg.draw.rect(screen, GREEN, [301, 401, 198, 98])
        screen.blit(pg.font.SysFont("华文楷体", 65).render("开   始", True, BLACK), [301, 401])
    elif scene == 3:
        screen.blit(pg.image.load("./bg.jpg"), [0, 0])
        pg.draw.rect(screen, GREEN, start, 1)
        if start.collidepoint(pg.mouse.get_pos()):
            pg.draw.rect(screen, GREEN, [301, 401, 198, 98])
        screen.blit(pg.font.SysFont("华文楷体", 65).render("重   来", True, BLACK), [301, 401])
        screen.blit(
            pg.font.SysFont("华文楷体", 50).render("你%s了" % ('赢' if win else '输'), True, BLUE if win else RED),
            [300, 200])
    pg.display.flip()
pg.quit()
