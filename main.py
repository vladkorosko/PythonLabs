from lab1.demo import demo as d1
from lab2.demo import demo as d2
from lab3.demo import demo as d3
from lab4.demo import demo as d4
from lab5.demo import demo as d5


if __name__ == '__main__':
    lab = 5
    if lab == 1:
        d1()
    elif lab == 2:
        d2()
    elif lab == 3:
        d3()
    elif lab == 4:
        d4()
    elif lab == 5:
        d5()
    else:
        pass
