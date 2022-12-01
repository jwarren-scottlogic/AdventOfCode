def elfCalorieCalc(input):
    elfBackpack = input.split('\n\n')
    elfItemized =[]
    maxCal = 0
    totalCalList =[]
    for item in elfBackpack:
        elfItemized.append(list(map(int, item.split('\n'))))
    for pack in elfItemized:
        totalCal = sum(pack)
        totalCalList.append(totalCal)
        if maxCal < totalCal:
            maxCal = totalCal
    # print('input is: '+input)
    print('items in each backpack are: ')
    print(elfItemized);
    print('calories in each backpack is: ')
    print(totalCalList);
    print('\n')
    print('The elf with the most calories has: '+str(maxCal))


puzzleInput = open('puzzleInput.txt', 'r').read()

elfCalorieCalc(puzzleInput)
