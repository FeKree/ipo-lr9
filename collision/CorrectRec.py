def isCorrectRect(rectangles):
    counter = 0
    flag = False
    
    for i in rectangles:
        counter += 1
        if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
            flag = True
            raise ValueError(f'Один из прямоугольников некорректный номер {counter}')

    if flag == True:
        return True
    else:
        return False
