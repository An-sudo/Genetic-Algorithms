# Population chromosomes 100
import numpy as np


def oneChromosomes():  # Generate ONE line of chromosomes without 1 and 0
    mean = 0  # Each chromosomes mean is 0
    std_dve = 1.15  # Each chromosomes standard deviation is 1.15
    temp = []
    chromosomes = []
    while (len(temp) != 4):
        num = np.random.normal(mean, std_dve, 2)
        if num[0] <= num[1]:
            temp.append(num[0])
            temp.append(num[1])
    for x in temp:
        temp = round(x, 2)  # Keep .2 number
        chromosomes.append(temp)
    return chromosomes


# Generate (number) line chromosomes with 1 and 0, 1,0 is 50-50
def finalChromosomes(number):
    array = []
    while (len(array) != (number/2)):
        array.append(0)
    while (len(array) != number):
        array.append(1)
    np.random.shuffle(array)  # shuffle the array from order to non-order

    finalChromosomes = []
    while (len(array) != 0):  # append 0 or 1 into chromosomes
        temp = oneChromosomes()
        temp.append(array.pop())
        finalChromosomes.append(temp)
    return finalChromosomes  # Fully 100 Chromosomes


def loadData(inputdata):  # Load current directory data named inputdata return 2-D array
    number_array = []
    try:
        with open(inputdata, "r") as file:
            for line in file:
                values = line.strip().split()
                # Convert the values to float and append them to the number array
                number_array.append([float(value) for value in values])
            return number_array
    except FileNotFoundError:
        print(
            f"The file '{inputdata}' does not exist in the current directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def oneFS(ch, data):  # Apply all data into one chromosome return the finial score
    mark = False
    fs = 0
    for x in data:
        if (x[0] >= ch[0] and x[0] <= ch[1]) and (x[1] >= ch[2] and x[1] <= ch[3]):
            if ch[4] == 1:
                fs = fs + x[2]
                mark = True
            else:
                fs = fs + ((-1) * x[2])
                mark = True
    if mark == True:
        temp = round(fs, 2)
        ch.append(temp)
    else:
        ch.append(-5000)
    return ch


def fScore(chromosomes, data):  # go through all chromosomes and append the fitness score at end of list
    fChromosomes = []
    for x in chromosomes:
        temp = oneFS(x, data)
        fChromosomes.append(temp)
    return fChromosomes


def reviseFitnessChromosomes(f):
    filtered_data = [arr for arr in f if arr[-1] != -5000]
    return filtered_data


def maxminaverage(f):
    total = 0
    number = len(f)
    temp = []
    for i in f:
        total = total + i[5]
        temp.append(i[5])
    maxValue = np.max(temp)
    minValue = np.min(temp)
    averageScore = round(total / number, 2)
    temp.clear()
    temp.append(minValue)
    temp.append(maxValue)
    temp.append(averageScore)
    return temp


def cloneXChromosomes(ch, x):
    newlength = int(len(ch) * x * 0.01)
    if newlength < 1:
        newlength = 1
    clone = []
    for x in ch[0:newlength]:
        clone.append(x)
    return clone


def optimizeClone(ch):
    newarray = []
    for x in ch:
        x.pop()
        newarray.append(x)
    return newarray


def parenetChromosomes(ch, x):
    newlength = int(len(ch) * x * 0.01)
    # i = len(ch) - newlength
    parent = []
    for x in ch[newlength:len(ch)+1]:
        parent.append(x)
    return parent


def uniform(parent, i):
    i1 = 0
    array = []
    p_len = len(parent)
    # parent = sorted(parent,key=lambda x:x[5],reverse = True)
    t1 = 0
    t = parent[-1][-1]
    for x in parent:
        x[-1] = int(x[-1] + abs(t) + 10)
    for x in parent:
        t1 = int(t1 + x[-1])

    for x in parent:
        t = int((x[-1]/t1) * 1000)
        for _ in range(t):
            array.append(i1)
        i1 = i1 + 1

    childSet = []
    for _ in range(i):
        child = []
        n1 = np.random.choice(array)
        while True:
            n2 = np.random.choice(array)
            if n2 != n1:
                break
        p1 = parent[n1]
        p2 = parent[n2]

        rs1 = np.random.choice(p1[0:3], size=1)
        rs1 = rs1[0]
        rs2 = np.random.choice(p2[0:3], size=1)
        rs2 = rs2[0]

        if rs1 > rs2:
            rs1, rs2 = rs2, rs1  # Swap rs1 and rs2

        child.extend([rs1, rs2])

        while True:
            rs3 = np.random.choice(p1[0:3], size=1)
            rs3 = rs3[0]
            if rs3 != rs1:
                break

        while True:
            rs4 = np.random.choice(p2[0:3], size=1)
            rs4 = rs4[0]
            if rs4 != rs2:
                break

        if rs3 > rs4:
            rs3, rs4 = rs4, rs3  # Swap rs3 and rs4

        child.extend([rs3, rs4])

        zo = np.random.choice([p1[4], p2[4]], size=1)
        z0 = zo[0]
        child.append(zo[0])

        childSet.append(child)

    return childSet


def kpoint(parent, i):
    i1 = 0
    array = []
    p_len = len(parent)
    # parent = sorted(parent,key=lambda x:x[5],reverse = True)
    t1 = 0
    t = parent[-1][-1]
    for x in parent:
        x[-1] = int(x[-1] + abs(t) + 10)
    for x in parent:
        t1 = int(t1 + x[-1])

    for x in parent:
        t = int((x[-1]/t1) * 1000)
        for _ in range(t):
            array.append(i1)
        i1 = i1 + 1

    childSet = []
    for _ in range(i):
        child = []
        n1 = np.random.choice(array)
        while True:
            n2 = np.random.choice(array)
            if n2 != n1:
                break
        parent[n1]
        parent[n2]
        i = np.random.randint(0, 1)
        if i == 1:
            child.append(parent[n1][0])
            child.append(parent[n1][1])
            child.append(parent[n2][2])
            child.append(parent[n2][3])
        else:
            child.append(parent[n2][0])
            child.append(parent[n2][1])
            child.append(parent[n1][2])
            child.append(parent[n1][3])
        i = np.random.randint(0, 1)
        child.append(i)
        childSet.append(child)
    return childSet


def generationCreate(f, x, number):  # chromosomes, X% , number of chromosomes
    clone = cloneXChromosomes(f, x)
    clone = optimizeClone(clone)
    parent = parenetChromosomes(f, x)
    numberChild = number-len(clone)
    child = uniform(parent, numberChild)
    newGeneration = clone + child
    return newGeneration


def generationCreate2(f, x, number):  # chromosomes, X% , number of chromosomes
    clone = cloneXChromosomes(f, x)
    clone = optimizeClone(clone)
    parent = parenetChromosomes(f, x)
    numberChild = number-len(clone)
    child = kpoint(parent, numberChild)
    newGeneration = clone + child
    return newGeneration


def sFS(ch, data):
    f = fScore(ch, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
    return f


def mGenerationCreate(ch, z):
    final = ch
    number1 = int(len(ch) * z * 0.01)
    number2 = int(len(ch) * z * 0.01)

    while number1 > 0:
        random_number = np.random.randint(0, len(ch))
        final.pop(random_number)
        number1 = number1 - 1
    for _ in range(number2):
        temp = oneChromosomes()
        random_number = np.random.randint(0, 1)
        temp.append(random_number)
        final.append(temp)
    return final


def arraystate(array):
    finalarray = []
    length = len(array)
    maxTotal = 0
    minTotal = 0
    Total = 0
    for i in array:
        minTotal = minTotal + i[0]
        maxTotal = maxTotal + i[1]
        Total = Total + i[2]
    averageMin = round(minTotal/length, 2)
    finalarray.append(averageMin)
    averageMax = round(maxTotal/length, 2)
    finalarray.append(averageMax)
    average = round(Total/length, 2)
    finalarray.append(average)
    return finalarray


def mainkpoint(n, x, z, data1, g):
    mma = []
    data = loadData(data1)
    # Create first Chromosomes
    temp = finalChromosomes(n)

    # Create a .txt file named Chromosomes.txt included c_n random chromosomes
    file_name = "Chromosomes.txt"
    np.savetxt(file_name, temp, fmt='%.2f', delimiter='  ')

    # Initialzing the chromosomes fScore(chromosomes,data)
    chromosomes = loadData(file_name)

    # put every fitness score into array
    f = fScore(chromosomes, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
    mma.append(maxminaverage(f))
    counter = 0
    g1 = generationCreate2(f, x, n)
    mg = mGenerationCreate(g1, z)

    for _ in range(g-1):
        f = fScore(mg, data)
        f = sorted(f, key=lambda x: x[5], reverse=True)
        f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
        mma.append(maxminaverage(f))
        counter = counter + 1
        if counter % 10 == 0:
            print("Every 10 Generation state(Min,Max,Average)", arraystate(mma))
            mma.clear()
        g1 = generationCreate2(f, x, n)
        mg = mGenerationCreate(g1, z)

    f = fScore(mg, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
    g1 = generationCreate2(f, x, n)
    mg = mGenerationCreate(g1, z)
    f = fScore(mg, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000

    print("From the final generation:")
    print("The Highest fitness score: ", f[0][5])
    print("The Highest fitness chromosome:", f[0][0:-1])
    return 0


def mainuniform(n, x, z, data1, g):
    mma = []
    data = loadData(data1)
    # Create first Chromosomes
    temp = finalChromosomes(n)

    # Create a .txt file named Chromosomes.txt included c_n random chromosomes
    file_name = "Chromosomes.txt"
    np.savetxt(file_name, temp, fmt='%.2f', delimiter='  ')

    # Initialzing the chromosomes fScore(chromosomes,data)
    chromosomes = loadData(file_name)

    # put every fitness score into array
    f = fScore(chromosomes, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
    mma.append(maxminaverage(f))
    counter = 0
    g1 = generationCreate(f, x, n)
    mg = mGenerationCreate(g1, z)

    for _ in range(g-1):
        f = fScore(mg, data)
        f = sorted(f, key=lambda x: x[5], reverse=True)
        f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
        mma.append(maxminaverage(f))
        counter = counter + 1
        if counter % 10 == 0:
            print("Every 10 Generation state(Min,Max,Average)", arraystate(mma))
            mma.clear()
        g1 = generationCreate(f, x, n)
        mg = mGenerationCreate(g1, z)

    f = fScore(mg, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000
    g1 = generationCreate(f, x, n)
    mg = mGenerationCreate(g1, z)
    f = fScore(mg, data)
    f = sorted(f, key=lambda x: x[5], reverse=True)
    f = reviseFitnessChromosomes(f)  # remove all fitness score is -5000

    print("From the final generation:")
    print("The Highest fitness score: ", f[0][5])
    print("The Highest fitness chromosome:", f[0][0:-1])
    return 0


def main():
    c_n = input("Please enter the number of chromosomes: ")
    print("Initial Population will be:", c_n)
    c_n = int(c_n)

    x_n = input("Please enter the number of X(0-100%): ")
    print("X will be", x_n, "%")
    x_n = int(x_n)

    z_n = input("Please enter the number of Z(0-100%): ")
    print("Z will be", z_n, "%")
    z_n = int(z_n)

    data = input(
        "Please enter the data name .txt(must be on the current directory): ")
    print("Your data file name", data)
    data = str(data)

    al = input("Please input crossover algorithm(u=uniform,k=kpoint):")
    if al == 'k':
        print("The crossover algorithm is k-point")
    elif al == 'u':
        print("The crossover algorithm is uniform")

    g_n = input("Please input the number of generation you want(Interger):")
    print(g_n, " generation you want create.")
    g_n = int(g_n)
    if al == 'k':
        mainkpoint(c_n, x_n, z_n, data, g_n)
    elif al == 'u':
        mainuniform(c_n, x_n, z_n, data, g_n)
    return 0


main()

