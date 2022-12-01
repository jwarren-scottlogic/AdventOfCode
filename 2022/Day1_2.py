def elfCalorieInPack(puzzleInput):
    elfBackpack = puzzleInput.split('\n\n')
    elfItemized =[]
    totalCalList =[]
    for item in elfBackpack:
        elfItemized.append(list(map(int, item.split('\n'))))
    for pack in elfItemized:
        totalCal = sum(pack)
        totalCalList.append(totalCal)
    return(totalCalList);


def topElf(totalCalList):
    maxCal=0
    for pack in totalCalList:
        if maxCal < pack:
            maxCal = pack
    return maxCal



puzzleInput = open('puzzleInput.txt', 'r').read()

totalCalList = elfCalorieInPack(puzzleInput)
topElf1=topElf(totalCalList)
totalCalList.remove(topElf1)
print('top elf 1: '+str(topElf1))
topElf2=topElf(totalCalList)
totalCalList.remove(topElf2)
print('top elf 2: '+str(topElf2))

topElf3=topElf(totalCalList)
print('top elf 3: '+str(topElf3))

print('top elf sum: '+str(topElf1+topElf2+topElf3))

