from tkinter import *
import numpy as np
import random

# neighborhood
neighborhood = 0

# bc
boundary = 0

# rozmiar siatki
startSize = 100

# kolory
colors = []
for i in range(100):
    colors.append([])


# RGB Color Selecting Function
def rgb(x, y, z):
    return "#%02x%02x%02x" % (x, y, z)


# Random Color Chooser
def random_color():
    x = random.randint(1, 255)
    y = random.randint(1, 255)
    z = random.randint(1, 255)
    return rgb(x, y, z)


changeColorVal = []
for i in range(10):
    changeColorVal.append([0])
global changeColorCount
changeColorCount = 0

grid = []
# create 2 dimensional array
for row in range(startSize):
    grid.append([])
    for column in range(startSize):
        grid[row].append('#FFFFFF')

subGrid = []
for row in range(startSize):
    subGrid.append([])
    for column in range(startSize):
        subGrid[row].append('#FFFFFF')

newGrid = []
for row in range(startSize):
    newGrid.append([])
    for column in range(startSize):
        newGrid[row].append('#FFFFFF')


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master = master
        self.master.title("Multiscale modelling")

        def setPeriodic():
            global rule
            rule = 0

        def setAbsorbing():
            global rule
            rule = 1

        def drawSize():
            global gridSize
            gridSize = int(xSizeInput.get())
            # create 2 dimensional array
            for row in range(gridSize):
                for column in range(gridSize):
                    grid[row][column] = '#FFFFFF'

            for row in range(gridSize):
                for column in range(gridSize):
                    newGrid[row][column] = '#FFFFFF'

            for i in range(0, gridSize):
                for j in range(0, gridSize):
                    drawRectangle(i, j, '#FFFFFF')
                    # x = 8 * i + 10
                    # y = 8 * j + 10
                    # c.create_rectangle(x, y, x + 6, y + 6, outline='white', fill='white')

        def exportTXT():
            f = open('D:\multiscale modeling\data.txt', 'a')
            for row in range(gridSize):
                for column in range(gridSize):
                    f.write("%d\t" % (row))
                    f.write("%d\t" % (column))
                    f.write("%s\n" % grid[row][column])
            f.close()

        def importTXT():
            results = []
            with open('D:\multiscale modeling\data.txt', 'r') as inputFile:
                for line in inputFile:
                    # grid[line.split(''\t')][] = inputFile
                    results = line.split('\t')
                    arg = results[2].replace('\n', '')

                    drawRectangle(int(results[0]), int(results[1]), arg)

        def exportBMP():
            c.postscript('D:\multiscale modeling\data123.ps')

        def drawRectangle(i, j, arg):
            x = 8 * i + 10
            y = 8 * j + 10
            c.create_rectangle(x, y, x + 8, y + 8, outline=arg, fill=arg)

        def drawBoundary(i, j):
            x = 8 * i + 10
            y = 8 * j + 10
            c.create_rectangle(x, y, x + 8, y + 8, outline='#000000', fill='#000000')

        def vonNeumann(i, j, arg):
            global gridSize
            if i - 1 >= 0:
                if grid[i - 1][j] == '#FFFFFF':
                    newGrid[i - 1][j] = arg
                    drawRectangle(i - 1, j, arg)
            if i + 1 < gridSize:
                if grid[i + 1][j] == '#FFFFFF':
                    newGrid[i + 1][j] = arg
                    drawRectangle(i + 1, j, arg)
            if j - 1 >= 0:
                if grid[i][j - 1] == '#FFFFFF':
                    newGrid[i][j - 1] = arg
                    drawRectangle(i, j - 1, arg)
            if j + 1 < gridSize:
                if grid[i][j + 1] == '#FFFFFF':
                    newGrid[i][j + 1] = arg
                    drawRectangle(i, j + 1, arg)

        def moore(i, j, arg):
            global gridSize
            if i - 1 >= 0:
                if grid[i - 1][j] == '#FFFFFF':
                    newGrid[i - 1][j] = arg
                    drawRectangle(i - 1, j, arg)
            if i + 1 < gridSize:
                if grid[i + 1][j] == '#FFFFFF':
                    newGrid[i + 1][j] = arg
                    drawRectangle(i + 1, j, arg)
            if j - 1 >= 0:
                if grid[i][j - 1] == '#FFFFFF':
                    newGrid[i][j - 1] = arg
                    drawRectangle(i, j - 1, arg)
            if j + 1 < gridSize:
                if grid[i][j + 1] == '#FFFFFF':
                    newGrid[i][j + 1] = arg
                    drawRectangle(i, j + 1, arg)
            if i - 1 >= 0:
                if j + 1 < gridSize:
                    if grid[i - 1][j + 1] == '#FFFFFF':
                        newGrid[i - 1][j + 1] = arg
                        drawRectangle(i - 1, j + 1, arg)
            if i - 1 >= 0:
                if j - 1 >= 0:
                    if grid[i - 1][j - 1] == '#FFFFFF':
                        newGrid[i - 1][j - 1] = arg
                        drawRectangle(i - 1, j - 1, arg)
            if i + 1 < gridSize:
                if j - 1 >= 0:
                    if grid[i + 1][j - 1] == '#FFFFFF':
                        newGrid[i + 1][j - 1] = arg
                        drawRectangle(i + 1, j - 1, arg)
            if i + 1 < gridSize:
                if j + 1 < gridSize:
                    if grid[i + 1][j + 1] == '#FFFFFF':
                        newGrid[i + 1][j + 1] = arg
                        drawRectangle(i + 1, j + 1, arg)

        def pentagonal(i, j, arg):
            global gridSize
            if i + 1 < gridSize:
                if grid[i + 1][j] == '#FFFFFF':
                    newGrid[i + 1][j] = arg
                    drawRectangle(i + 1, j, arg)
            if j - 1 >= 0:
                if grid[i][j - 1] == '#FFFFFF':
                    newGrid[i][j - 1] = arg
                    drawRectangle(i, j - 1, arg)
            if j + 1 < gridSize:
                if grid[i][j + 1] == '#FFFFFF':
                    newGrid[i][j + 1] = arg
                    drawRectangle(i, j + 1, arg)
            if i + 1 < gridSize:
                if j - 1 >= 0:
                    if grid[i + 1][j - 1] == '#FFFFFF':
                        newGrid[i + 1][j - 1] = arg
                        drawRectangle(i + 1, j - 1, arg)
            if i + 1 < gridSize:
                if j + 1 < gridSize:
                    if grid[i + 1][j + 1] == '#FFFFFF':
                        newGrid[i + 1][j + 1] = arg
                        drawRectangle(i + 1, j + 1, arg)

        def hexagonal(i, j, arg):
            global gridSize
            if i - 1 >= 0:
                if grid[i - 1][j] == '#FFFFFF':
                    newGrid[i - 1][j] = arg
                    drawRectangle(i - 1, j, arg)
            if i + 1 < gridSize:
                if grid[i + 1][j] == '#FFFFFF':
                    newGrid[i + 1][j] = arg
                    drawRectangle(i + 1, j, arg)
            if j - 1 >= 0:
                if grid[i][j - 1] == '#FFFFFF':
                    newGrid[i][j - 1] = arg
                    drawRectangle(i, j - 1, arg)
            if j + 1 < gridSize:
                if grid[i][j + 1] == '#FFFFFF':
                    newGrid[i][j + 1] = arg
                    drawRectangle(i, j + 1, arg)
            if i - 1 >= 0:
                if j + 1 < gridSize:
                    if grid[i - 1][j + 1] == '#FFFFFF':
                        newGrid[i - 1][j + 1] = arg
                        drawRectangle(i - 1, j + 1, arg)
            if i + 1 < gridSize:
                if j - 1 >= 0:
                    if grid[i + 1][j - 1] == '#FFFFFF':
                        newGrid[i + 1][j - 1] = arg
                        drawRectangle(i + 1, j - 1, arg)

        def random():
            i = 0
            while i < (int(nucleonAmountInput.get())):
                row = np.random.randint(0, int(xSizeInput.get()))
                column = np.random.randint(0, int(xSizeInput.get()))
                if grid[row][column] == '#FFFFFF':
                    grid[row][column] = random_color()
                    colors[i] = grid[row][column]
                    drawRectangle(row, column, grid[row][column])
                    i += 1

        def addInclusion():
            i = 0
            global gridSize
            while i < (int(inclusinAmountInput.get())):
                row = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                column = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                for j in range(int(inclusinSizeInput.get())):
                    for k in range(int(inclusinSizeInput.get())):
                        x = row + j
                        y = column + k
                        grid[x][y] = '#000000'
                        colors[i] = '#000000'
                        drawRectangle(x, y, grid[row][column])
                i += 1

        def addCircularInclusion():
            global gridSize
            k = 0
            while k < (int(inclusinAmountInput.get())):
                x = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                y = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                for i in range(int(inclusinSizeInput.get())):
                    for j in range(int(inclusinSizeInput.get())):
                        if (y + j + 1 - i) >= y:
                            drawRectangle(x - i, y + j + 1 - i, '#000000')
                            grid[x - i][y + j + 1 - i] = '#000000'
                        if (y - j - 1 + i) <= y:
                            drawRectangle(x + i, y - j - 1 + i, '#000000')
                            grid[x + i][y - j - 1 + i] = '#000000'
                        if (x + j + 1 - i) >= x:
                            drawRectangle(x + j + 1 - i, y + i, '#000000')
                            grid[x + j + 1 - i][y + i] = '#000000'
                        if (x - j - 1 + i) <= x:
                            drawRectangle(x - j - 1 + i, y - i, '#000000')
                            grid[x - j - 1 + i][y - i] = '#000000'
                drawRectangle(x, y, '#000000')
                grid[x][y] = '#000000'
                k += 1

        def drawInclusion(i, j):
            i1 = int(inclusinSizeInput.get())
            for x in range(int(-((i1 - 1) / 2)), int((i1 + 1) / 2)):
                for y in range(int(-((i1 - 1) / 2)), int((i1 + 1) / 2)):
                    row = i + x
                    column = j + y
                    newGrid[row][column] = '#000000'
                    drawRectangle(row, column, '#000000')

        def addIncusionAfter():
            incSize = int(inclusinAmountInput.get())
            num = 0
            check = FALSE
            global gridSize
            while num < incSize:
                i = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                j = np.random.randint(int(inclusinSizeInput.get()), gridSize - int(inclusinSizeInput.get()))
                if i - 1 >= 0:
                    if grid[i - 1][j] != grid[i][j]:
                        drawInclusion(i, j)
                        num += 1
                        check = TRUE
                if i + 1 < gridSize:
                    if grid[i + 1][j] != grid[i][j]:
                        if check == FALSE:
                            drawInclusion(i, j)
                            num += 1
                            check = TRUE
                if j - 1 >= 0:
                    if grid[i][j - 1] != grid[i][j]:
                        if check == FALSE:
                            drawInclusion(i, j)
                            num += 1
                            check = TRUE
                if j + 1 < gridSize:
                    if grid[i][j + 1] != grid[i][j]:
                        if check == FALSE:
                            drawInclusion(i, j)
                            num += 1
                            check = TRUE
                if i - 1 >= 0:
                    if j + 1 < gridSize:
                        if grid[i - 1][j + 1] != grid[i][j]:
                            if check == FALSE:
                                drawInclusion(i, j)
                                num += 1
                                check = TRUE
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        if grid[i - 1][j - 1] != grid[i][j]:
                            if check == FALSE:
                                drawInclusion(i, j)
                                num += 1
                                check = TRUE
                if i + 1 < gridSize:
                    if j - 1 >= 0:
                        if grid[i + 1][j - 1] != grid[i][j]:
                            if check == FALSE:
                                drawInclusion(i, j)
                                num += 1
                                check = TRUE
                if i + 1 < gridSize:
                    if j + 1 < gridSize:
                        if grid[i + 1][j + 1] != grid[i][j]:
                            if check == FALSE:
                                drawInclusion(i, j)
                                num += 1
                                check = TRUE
                check = False

        # shape control
        def shapeControl():
            colorTab = []
            for z in range(9):
                colorTab.append([0])

            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]
            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] == '#FFFFFF':
                        counter = 0
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                colorTab[counter] = grid[i + a][j + b]
                                counter += 1

                        c = 0
                        maxColor = '#FFFFFF'
                        max = 0
                        for v in colorTab:
                            if v != '#FFFFFF':
                                c = colorTab.count(v)
                                if c >= max:
                                    max = c
                                    maxColor = v

                        if max >= 5:
                            newGrid[i][j] = maxColor
                            drawRectangle(i, j, maxColor)

                        if max >= 3:
                            if colorTab[1] == colorTab[3] == colorTab[5] or colorTab[1] == colorTab[3] == colorTab[
                                7] or colorTab[3] == colorTab[7] == colorTab[5] or colorTab[1] == colorTab[5] == \
                                    colorTab[7]:
                                newGrid[i][j] = maxColor
                                drawRectangle(i, j, maxColor)

                        if max >= 3:
                            if colorTab[0] == colorTab[2] == colorTab[6] or colorTab[0] == colorTab[2] == colorTab[
                                8] or colorTab[0] == colorTab[6] == colorTab[8] or colorTab[2] == colorTab[6] == \
                                    colorTab[8]:
                                newGrid[i][j] = maxColor
                                drawRectangle(i, j, maxColor)

                        if maxColor:
                            probability = 10
                            n = np.random.randint(1, 100)
                            if n <= probability:
                                newGrid[i][j] = maxColor
                                drawRectangle(i, j, maxColor)

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        def shape():
            for i in range(gridSize):
                for j in range(gridSize):
                    while grid[i][j] == '#FFFFFF':
                        shapeControl()
                        c.update()

        def substructure():
            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] in changeColorVal:
                        newGrid[i][j] = '#FFFFFF'
                        drawRectangle(i, j, '#FFFFFF')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

            random()

            startSimulate()

        def dualPhase():
            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] not in changeColorVal:
                        newGrid[i][j] = '#FFFFFF'
                        drawRectangle(i, j, '#FFFFFF')

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] in changeColorVal:
                        grid[i][j] = '#000000'
                        drawRectangle(i, j, '#000000')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

            random()

            startSimulate()

        def grainBoundary():
            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] in changeColorVal:
                        if i - 1 >= 0:
                            if grid[i - 1][j] != grid[i][j]:
                                newGrid[i - 1][j] = '#000000'
                                drawRectangle(i - 1, j, '#000000')
                        if i + 1 < gridSize:
                            if grid[i + 1][j] != grid[i][j]:
                                newGrid[i + 1][j] = '#000000'
                                drawRectangle(i + 1, j, '#000000')
                        if j - 1 >= 0:
                            if grid[i][j - 1] != grid[i][j]:
                                newGrid[i][j - 1] = '#000000'
                                drawRectangle(i, j - 1, '#000000')
                        if j + 1 < gridSize:
                            if grid[i][j + 1] != grid[i][j]:
                                newGrid[i][j + 1] = '#000000'
                                drawRectangle(i, j + 1, '#000000')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        def clearSelected():
            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] != '#000000':
                        newGrid[i][j] = '#FFFFFF'
                        drawRectangle(i, j, '#FFFFFF')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        def grainBoundaryAll():
            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if i - 1 >= 0:
                        if grid[i - 1][j] != grid[i][j]:
                            if grid[i - 1][j] != '#000000':
                                newGrid[i - 1][j] = '#000000'
                                drawRectangle(i - 1, j, '#000000')
                    if i + 1 < gridSize:
                        if grid[i + 1][j] != grid[i][j]:
                            if grid[i + 1][j] != '#000000':
                                newGrid[i + 1][j] = '#000000'
                                drawRectangle(i + 1, j, '#000000')
                    if j - 1 >= 0:
                        if grid[i][j - 1] != grid[i][j]:
                            if grid[i][j - 1] != '#000000':
                                newGrid[i][j - 1] = '#000000'
                                drawRectangle(i, j - 1, '#000000')
                    if j + 1 < gridSize:
                        if grid[i][j + 1] != grid[i][j]:
                            if grid[i][j + 1] != '#000000':
                                newGrid[i][j + 1] = '#000000'
                                drawRectangle(i, j + 1, '#000000')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        def clearAll():
            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

            for i in range(gridSize):
                for j in range(gridSize):
                    if grid[i][j] != '#000000':
                        newGrid[i][j] = '#FFFFFF'
                        drawRectangle(i, j, '#FFFFFF')

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        # Tworze 6 rzedow i 5 kolumn w oknie
        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)

        # dziele okno na dwie czesci
        Frame1 = Frame(master, bg="SystemButtonFace")
        Frame1.grid(row=0, column=0, rowspan=6, columnspan=1, sticky=W + E + N + S)
        Frame2 = Frame(master, bg="SystemButtonFace")
        Frame2.grid(row=0, column=1, rowspan=6, columnspan=4, sticky=W + E + N + S)

        # label i inputy rozmiar i liczba poczatkwowa
        xSize = Label(Frame1, text='Size').place(x=20, y=20)
        xSizeInput = Entry(Frame1, width=5)
        xSizeInput.place(x=20, y=40)
        drawButton = Button(Frame1, text='Generate grid', command=drawSize).place(x=180, y=20)
        nucleonAmount = Label(Frame1, text='NucleonAmount').place(x=20, y=60)
        nucleonAmountInput = Entry(Frame1, width=5)
        nucleonAmountInput.place(x=20, y=80)

        bc = Label(Frame1, text='Boundary condition').place(x=20, y=120)

        bcVar = ["Absorbing", "Periodic"]
        variableBC = StringVar(self.master)
        variableBC.set(bcVar[0])
        bcMenu = OptionMenu(Frame1, variableBC, *bcVar)
        bcMenu.place(x=180, y=120)

        neigh = Label(Frame1, text='Neighborhood').place(x=20, y=160)
        neighVar = ["von Neumann", "Moore", "Pentagonal", "Hexagonal", "ShapeControl"]
        variableNEIGH = StringVar(self.master)
        variableNEIGH.set(neighVar[0])
        neighMenu = OptionMenu(Frame1, variableNEIGH, *neighVar)
        neighMenu.place(x=180, y=160)

        inclusinAmountLabel = Label(Frame1, text='Inclusion amount').place(x=20, y=200)
        inclusinAmountInput = Entry(Frame1, width=5)
        inclusinAmountInput.place(x=20, y=220)

        inclusinSizeLabel = Label(Frame1, text='Inclusion size').place(x=20, y=240)
        inclusinSizeInput = Entry(Frame1, width=5)
        inclusinSizeInput.place(x=20, y=260)

        inclusionButton = Button(Frame1, text='Add inclusion', command=addInclusion).place(x=180, y=200)

        inclusionAfterButton = Button(Frame1, text="Add inclusion after", command=addIncusionAfter).place(x=180, y=240)
        circuralInclusionButton = Button(Frame1, text='Add circular inclusion', command=addCircularInclusion).place(
            x=180, y=280)

        # start simulate
        def startSimulate():
            for i in range(gridSize):
                for j in range(gridSize):
                    while grid[i][j] == '#FFFFFF':
                        vonNStart()
                        c.update()

        # start/stop
        def vonNStart():
            global gridSize
            for i in range(gridSize):
                for j in range(gridSize):
                    newGrid[i][j] = grid[i][j]
            for k in range(int(nucleonAmountInput.get())):
                for i in range(gridSize):
                    for j in range(gridSize):
                        if grid[i][j] != '#000000':
                            if grid[i][j] == colors[k]:
                                if variableBC.get() == 'Periodic':
                                    if i - 1 < 0:
                                        if grid[gridSize - 1][j] == '#FFFFFF':
                                            newGrid[gridSize - 1][j] = colors[k]
                                            drawRectangle(gridSize - 1, j, colors[k])
                                    if i + 1 == gridSize:
                                        if grid[0][j] == '#FFFFFF':
                                            newGrid[0][j] = colors[k]
                                            drawRectangle(0, j, colors[k])
                                    if j - 1 < 0:
                                        if grid[i][gridSize - 1] == '#FFFFFF':
                                            newGrid[i][gridSize - 1] = colors[k]
                                            drawRectangle(i, gridSize - 1, colors[k])
                                    if j + 1 == gridSize:
                                        if grid[i][0] == '#FFFFFF':
                                            newGrid[i][0] = colors[k]
                                            drawRectangle(i, 0, colors[k])
                                if variableNEIGH.get() == 'von Neumann':
                                    vonNeumann(i, j, colors[k])
                                if variableNEIGH.get() == 'Moore':
                                    moore(i, j, colors[k])
                                if variableNEIGH.get() == 'Pentagonal':
                                    pentagonal(i, j, colors[k])
                                if variableNEIGH.get() == 'Hexagonal':
                                    hexagonal(i, j, colors[k])
                                if variableNEIGH.get() == 'ShapeControl':
                                    shape()

            for i in range(gridSize):
                for j in range(gridSize):
                    grid[i][j] = newGrid[i][j]

        startButton = Button(Frame1, text='Simulate step by step', command=vonNStart)
        startSimulateButton = Button(Frame1, text='Simulate grain grow', command=startSimulate)
        startButton.place(x=20, y=340)
        startSimulateButton.place(x=180, y=340)
        # Menubar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        file = Menu(menubar, tearoff=0)
        microstructure = Menu(file)
        importMenu = Menu(file)
        importMenu.add_command(label='TXT', command=importTXT)
        importMenu.add_command(label='BMP')
        file.add_cascade(label='Import', menu=importMenu, underline=0)
        exportMenu = Menu(file)
        exportMenu.add_command(label='TXT', command=exportTXT)
        exportMenu.add_command(label='BMP', command=exportBMP)
        file.add_cascade(label='Export', menu=exportMenu, underline=0)
        # microstructure.add_command(label='Import', command=importTXT)
        # microstructure.add_command(label='Export', command=exportTXT)
        # file.add_cascade(label='Microstructure', menu=microstructure, underline=0)

        file.add_separator()
        file.add_command(label="Exit", command=self.quit)

        menubar.add_cascade(label="File", menu=file)

        # shape control button
        # shapeControlButton = Button(Frame1, text="ShapeControl", command=shapeControl)
        # shapeControlButton.place(x=20, y=400)

        # grain selection
        grainSelectionButton = Button(Frame1, text="Substructure", command=substructure)
        grainSelectionButton.place(x=20, y=440)

        grainSelectionButton = Button(Frame1, text="DualPhase", command=dualPhase)
        grainSelectionButton.place(x=180, y=440)

        grainBoundaryButton = Button(Frame1, text="Grainboundary", command=grainBoundary)
        grainBoundaryButton.place(x=20, y=480)
        grainBoundaryButtonAll = Button(Frame1, text="GrainBoundaryAll", command=grainBoundaryAll)
        grainBoundaryButtonAll.place(x=20, y=520)

        clearSelectedfButton = Button(Frame1, text="clearSelected", command=clearSelected)
        clearSelectedfButton.place(x=180, y=480)
        clearAllButton = Button(Frame1, text="clearAll", command=clearAll)
        clearAllButton.place(x=180, y=520)

        # random btn
        randomButton = Button(Frame1, text="Random", command=random)
        randomButton.place(x=180, y=60)

        # reset btn
        def reset():
            c.delete("all")

        resetButton = Button(Frame1, text="Reset", command=reset)
        resetButton.place(x=20, y=600)

        # kanvas
        c = Canvas(Frame2, bg="black", height=900, width=900)
        c.place(x=10, y=10)
        global changeColorCount
        changeColorCount = 0

        def callback(event):
            global changeColorCount
            changeColorVal[changeColorCount] = grid[(event.x // 8) - 1][(event.y // 8) - 1]
            changeColorCount += 1

        c.bind("<Button-1>", callback)


def main():
    root = Tk()

    root.geometry("1900x1050+200+200")
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
