# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:38:03 2021

@author: Brandon


"""

import numpy as np
from hillclimbing import hillclimbing
from Node import Node
import random
from simulatedAnnealing import Anneal
import copy
# Used this for plots
import matplotlib.pyplot as plt

# I added this so I could easily paste a random numpy array into the prebuild with commas.
# printBoardWithCommas takes a numpy array.
# Usage: After you run a random board, 
# type printBoardWithCommas(board) into the console.
def printBoardWithCommas(board):
    print(np.array2string(board, separator=","))
    
#######################
### graph lists
pltxhh = []
pltyhh = []
pltxhhpoint = []
pltxh = []
pltyh = []
pltxhpoints = []
pltxa = []
pltya = []
pltxapoints = []
###################
print("Welcome to the Traveling Salesperson program.")
                                                # Edit the pre-build for your own boards
print("Would you like to randomize a choosen number of cities(r) or use the pre-build?(~ anything else)")
userChoice = input("r / ~: ")
if(userChoice == "r" or userChoice == "R"):
    print("How many cities do you want on your board?")
    print("Please choose at least more than 2.")
    citiesNum = input("Number of cities: ")
    citiesNum = int(citiesNum)
    board = np.zeros([citiesNum,citiesNum],dtype=np.int)
    for i in range(0, citiesNum):
        for j in range(0, citiesNum):
            if(i == j):
                board[i][j] = 0
            else:
                board[i][j] = random.randint(100, 2500)
else:
##############################################################
    # Make your own board here
    
    
    
#######################################################
# These first two were my test boards.
#    board = np.array([[0, 100, 200, 300],
#                      [200,0,300,400],
#                      [700,500,0,290],
#                      [120,123,690,0]])
#    board = np.array([[0, 100, 200, 300, 400],
#                      [100, 0, 200, 300, 400],
#                      [100, 200, 0, 300, 400],
#                      [100, 300, 200, 0, 400],
#                      [100, 400, 200, 300, 0]])
########################################################
# This was board #1 used in my tests
    board = np.array([[   0,  695,  196, 1656, 1386, 1400, 1968, 2304,  399, 1292],
                      [1681,    0,  248, 1348, 2112,  882,  234, 1341,  711,  609],
                      [ 204, 2497,    0,  970, 2467, 1512, 1335, 2187,  836, 2297],
                      [2302, 1518, 1234,    0, 1300,  433, 2395,  992, 1399, 1577],
                      [2002, 2456, 2421, 1849,    0, 1526, 1195, 1561, 1494,  495],
                      [1050, 1596,  387,  713, 1693,    0, 1589, 1960, 1041, 2130],
                      [2015, 1599, 1280,  521, 1770, 1193,    0, 1389, 2081, 2234],
                      [1935, 2115, 2275,  704, 1147,  754, 1533,    0, 1490, 1714],
                      [1915, 2044, 2145, 1686,  407, 1422, 2091, 2138,    0, 1141],
                      [ 613, 1338, 2345, 2449, 2448,  844, 1523,  958,  537,    0]])
# This was board #2 in my tests
#    board = np.array([[   0,1375,2480, 570,2364,1316,1532, 351,1304,1755,2131],
#                      [1463,   0, 507,1101,1239,1884, 526, 633,2183,2009,1696],
#                      [1951, 721,   0,1298,2293, 285, 836,1374, 392,2235,1189],
#                      [ 821, 525, 247,   0,1186,1337, 888,1020, 381,1167, 188],
#                      [2014, 315,2180,1372,   0, 921, 967, 437,2160,2042,1583],
#                      [2500, 219,2266,2033,1899,   0,1565, 466,1735, 479,2221],
#                      [2247, 671,2014,2412,1296, 731,   0, 921, 250,1133,2216],
#                      [ 112,2297,1907,2449, 273,1974,1920,   0, 580,1456,1259],
#                      [ 386, 944,2255, 230,1447,1048, 735,1253,   0,2134,2406],
#                      [2067,1068,1312, 111,2281,1414,1032,1251, 959,   0, 175],
#                      [ 921, 375,1409,1903, 478,2317, 180,1671,1366,1066,   0]])
# This was board #3 in my tests
#    board = np.array([[   0,1511,2134,1398,1464,1712,1465,2075,1961, 410,1806,1550],
#                      [2467,   0, 385,2500, 866, 973,1203, 383, 944, 718,1803,1968],
#                      [1567,2309,   0,1102,1416, 277, 705, 165,1591,1117, 748,1971],
#                      [ 700,2209, 889,   0, 574, 996,1452,1616,1302, 280,2375,1890],
#                      [1159,2042,1673,1194,   0,2455, 498, 834,2308, 801, 281,1881],
#                      [ 622,1862,1656, 177,2313,   0,1843, 586,1408,2246, 331, 763],
#                      [2177,1764,1538,1147,1137, 812,   0,1035,1221,1350, 476,2278],
#                      [1873, 172, 163,2454, 156, 327,1858,   0,1543,2328, 649, 672],
#                      [2416,1371, 765,1090,2261,1701,2343,1121,   0,2290,2026,1485],
#                      [2048, 861,1694, 194,1024,1721, 636,1957, 498,   0,1192,1775],
#                      [ 173, 592,1391,1732, 401, 269,1957,1634,2098, 828,   0,2493],
#                      [1180,2112,1196,1357,1587,1397,1223,1525,2095,1999,1654,   0]])
# This was board #4 in my tests
#    board = np.array([[   0,2443,1614, 220,2157,2107,2490, 839,2464,2292,1395, 767, 555,1118,2331],
#                      [1429,   0,1260, 588, 483, 589,1666,2014,2343,2228,1753,2096, 347,1494,1982],
#                      [ 595,2077,   0,1106,2091,2134,1268, 533,1535,1784, 964,1641, 902,2410,1870],
#                      [2132,2135,1975,   0,1814,1922,1948, 902,1772,1007,1390, 526,1298,1676,1674],
#                      [2357,1479, 401,1301,   0,2100, 903,2190,1017,2192, 163, 734,2461,1030,2421],
#                      [1222, 232,1225, 267,2105,   0, 959, 206, 917, 799,1634,1744, 341, 770, 344],
#                      [1224, 461,2228, 314, 301,2262,   0, 688, 654, 480,1988,2371,1545,1599,1274],
#                      [2314,1841,2246,2222, 595,2104,1940,   0,2360,1031, 268,1932,1164,2464,2452],
#                      [ 515, 107,1306,1188,2393, 102,2120, 604,   0,1539,1163,1039, 265, 839,1342],
#                      [1755,1032, 531, 442,2013, 526,1661,1352, 971,   0, 549,1170,2083,1079,1018],
#                      [ 833,1222, 469, 723,1549,1309, 708,1641,1434,1292,   0,2109, 481,1342,1075],
#                      [1433, 891,1552,1227,1662,1298,1838, 341, 994,1296, 641,   0,1564, 260,1104],
#                      [2164, 768, 805,1484,2309, 688, 601,2179, 242,1244, 744,1993,   0,2484,2243],
#                      [2287,1243,1491,1971, 301, 296,1170,1442,1701,1281, 355, 799,2094,   0,566],
#                      [1914, 966,2442,1399,2241, 990,1050,2141, 796, 386,1040,2304,1445,1780,0]])
# This was board #5 in my tests
#    board = np.array([[   0, 965, 842,2305, 979,2177,1246,2008,1763, 927,1248, 696, 692, 378, 1915, 448, 387,1908,2069, 681],
#                      [1312,   0, 739, 834,1161, 711,2023, 808, 401,1290,1770,1434, 636, 534, 1484, 113,1722,1242,1458,1629],
#                      [ 436,1412,   0,1361,2447, 813,1030,1758,2253, 361,1171, 259,2293,2017, 2442,1291,1106,1063,2030,1383],
#                      [1461,1577,1546,   0, 969, 761,1387, 207,2362,1315,2074,1567,2388, 756, 1512, 196,2098,1849, 767, 205],
#                      [2103, 959, 554,2338,   0,1069,2014,1961,1762,2110,1973,2095,1694, 177, 1990, 849, 403,1938,1784,1035],
#                      [1003,1087,1752,1539,1071,   0,2341,1610,1891,1274,1573, 903,1771, 391,  139,2076, 666,2032,1333,1995],
#                      [1947,1186, 857,1056,1671,2101,   0,1396, 845, 945,1659,2239,1705, 820, 2203, 232,1368,1828, 354,1772],
#                      [2370, 108,1146,2319,1041,1057, 138,   0, 595,1637,1935, 309,1551,1295, 1479,2461,1994,2364,1812, 922],
#                      [ 469,1041,2072,1399,1169, 185,1748, 193,   0,1432, 186,1502, 345, 585, 2238,1991, 448,1114, 956,1867],
#                      [1091, 233,1472, 757, 754,2156,2128, 631,2369,   0,1954,1316,2267, 946, 1159,2167,1225, 881, 556,1804],
#                      [ 562, 476, 733,2024,1360,2428,1688,2458,2227,1162,   0,1633, 167,1263, 2024, 822,2223,1212,1364,2444],
#                      [1187, 691,2338, 166, 201,1222, 797, 823,1169,1782, 600,   0, 512,1186,  282,1104,1026,1705,1440, 506],
#                      [ 379,1952,2441, 111, 204,2003, 266,2268, 587, 377,1442, 642,   0,1722, 2469, 480,1728,1057,1929,1485],
#                      [ 428,2211, 855, 997,2448,1440, 244,2401,2137,1914, 507, 364, 566,   0, 1891, 265,1294, 587, 935, 267],
#                      [1843,1981,1797,2125,2123, 437,2399,1689,2278, 404,1404,1186,1801,2145,    0, 836,1003,1913,1884,1055],
#                      [1050,1439,1683,1984, 590,1715,1184,2162,2301, 150,1648,2107,2280, 162, 1250,   0,1856,1641,2279,1048],
#                      [2022, 175, 407, 205,1754, 260, 184, 827,1355,2212, 862,1117,2217, 345, 2408,2476,   0,1939,2415,2269],
#                      [1727,1497, 982,2377,1856,1817,1550,1478,2499, 810,2077,1190, 624, 435,  479,2453, 383,   0,2307, 225],
#                      [ 654, 802,2233, 374, 146,1172,2031,1354,1405, 528, 604,1697,2425,1762, 1429,2355, 791,2291,   0, 722],
#                      [ 980,1872, 194, 274,1832,1066,1645, 418, 483,2031,1971,1542,1572,1737,  213,2282,1396,1611, 324,   0]])
################################################################
### More lists for the program 
outcomes = []
a = []
schedule = []
List = []
############################################################
# Graveyard of bad temp functions.
#for i in range(100, 0, -1):
#    schedule.append(round((511 + (i * 5.12)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((255 + (i * 2.56)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((127 + (i * 1.28)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((63 + (i * 0.64)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((31 + (i * 0.32)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((15 + (i * 0.16)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((7 + (i * 0.08)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((3 + (i * 0.04)), 2))
#for i in range(100, 0, -1):
#    schedule.append(round((1 + (i * 0.02)), 2))
#for i in range(100, -1, -1):
#    schedule.append(round((0 + (i * 0.01)), 2))
####

#for i in range(100,0,-1):
#    schedule.append((760 + (i * 3)))
#for i in range(100,0,-1):
#    schedule.append((510 + (i * 2.5)))
#for i in range(100,0, -1):
#    schedule.append((310 + (i * 2)))
#for i in range(100,0, -1):
#    schedule.append((160 + (i * 1.5)))
#for i in range(100,0, -1):
#    schedule.append((60 + (i * 1)))
#for i in range(100,0, -1):
#    schedule.append((10 + (i * 0.5)))
#for i in range(100, -1, -1):
#    schedule.append(round((0 + (i * 0.1)), 1))
###
### I found just using this range seemed best.
### It also made the graphs look less cluttered.
### Because the value didn't change as much.
### When temp is too high nothing really happens.
### Just a lot of fluctuating.
for i in range(250, 0, -1):
    schedule.append(round((150 + (i * 1)), 1))
for i in range(250, 0, -1):
    schedule.append(round((25 + (i * 0.5)), 1))
for i in range(250, -1, -1):
    schedule.append(round((0 + (i * 0.1)), 1))
### ^ This schedule still has problems.

#for i in range(0, 901):
#    if(i < 11):
#        schedule.append(i)  
#    elif(i < 101):
#        schedule.append(i + round(i / 10))
#    elif(i < 201):
#        schedule.append(i + round(i / 9))
#    elif(i < 301):
#        schedule.append(i + round(i / 8))
#    elif(i < 401):
#        schedule.append(i + round(i / 7))
#    elif(i < 501):
#        schedule.append(i + round(i / 6))
#    elif(i < 601):
#        schedule.append(i + round(i / 5))
#    elif(i < 701):
#        schedule.append(i + round(i / 4))
#    elif(i < 801):
#        schedule.append(i + round(i / 3))
#    elif(i < 901):
#        schedule.append(i + round(i / 2))
#schedule.reverse()
######################################
### Start of main
print("\nThe board for your runs.")
print(board)
#########################################
### Second hill climbing 
### With what I believe is actual random restart.
print("\n5 Hill-Climbs with correct Random Restart\n")
size = board.shape[0]

for j in range(5):
    ### Number of total boards is (size - 1)! this holds true from 1-4 at least.
    ### I assume this will only be used for bigger boards and do
    ### size^3
    num = 0
    restarts = 0
    ranRe = (size*size*size)
    best = Node(None, 0)
    while True:
        val = hillclimbing(board, pltyhh)
        # First pass through
        if(best.cost == 0):
            best = copy.deepcopy(val)
            num = (len(pltyhh) - 1)
        elif(best.cost > val.cost):
            best = copy.deepcopy(val)
            num = (len(pltyhh) - 1)
        if(restarts >= ranRe):
            print("Run ",(j + 1))
            print(best.cost, best.path)
            ## I decide more plots will probably be needed with
            ## more restarts.
            pltxhhpoint.append(num)
            f, ax = plt.subplots()
            ax.set_xticks(pltxhhpoint, minor=False)
            ax.xaxis.grid(True, which='major')
            for i in range(len(pltyhh)):
                pltxhh.append(i)
            plt.plot(pltxhh, pltyhh)
            plt.show()
            plt.clf()
            pltyhh = []
            pltxhh = []
            pltxhhpoint = []
            break
        restarts += 1;
##########################################
### Old Hill climbing RR section
print("\n5 Hill-Climbs with Random, Random Restarts\n")
# I decided to put the random restart part in main.
size = board.shape[0]
for j in range(5):
    ranRe = []
    numOfRestarts = 0
    ##########################################
    ### size^3 might be overkill? 
    for i in range((size*size*size)):
        ranRe.append(i + 1)
    # Wasn't entirly sure how to add random restart.
    # This is not correct if it needs to be specific.
    #########################################
    best = Node(None, 0)
    while True:
        val = hillclimbing(board, pltyh)
        # First pass through
        if(best.cost == 0):
            best = copy.deepcopy(val)
        elif(best.cost > val.cost):
            best = copy.deepcopy(val)
        num = random.randint(1, (size*size*size))
        if(ranRe[num - 1] == num):
            ranRe[num - 1] = 0
            numOfRestarts += 1
        else:
            print("Run ",(j + 1))
            print(best.cost, best.path)
            print("With", numOfRestarts, "Restarts.\n")
            pltxhpoints.append(len(pltyh) - 1)
            break

# I don't know mathplot.
#https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot
f, ax = plt.subplots()
ax.set_xticks(pltxhpoints, minor=False)
ax.xaxis.grid(True, which='major')
for i in range(len(pltyh)):
    pltxh.append(i)
plt.plot(pltxh, pltyh)
plt.show()
plt.clf()
#########################################
print()
####################################
### The Annealing section
for i in range(0,5):
    vala = Anneal(board, schedule, pltya)
    a.append(vala)
    pltxapoints.append(len(pltya) - 1)
print("5 Simulated Anneals\n")
for i in range(0,5):
    print("Run ",(i + 1))
    print(a[i].cost, a[i].path, "\n")
### This plot will look awful with very few cities.
### 3 being the best example, I'm not sure why
f, ax = plt.subplots()
ax.set_xticks(pltxapoints, minor=False)
ax.xaxis.grid(True, which='major')
for i in range(len(pltya)):
    pltxa.append(i)
plt.plot(pltxa,pltya)
plt.show()
plt.clf()
## I don't know why the figure size and axes are printing out.
## They aren't errors so I tried to not worry about them.
######################################