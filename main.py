from PIL import Image, ImageDraw
import colour
import numpy as np
import random
import matplotlib.pyplot as plt
import argparse

"""
Author: Yucheng An
Usage: Please run command as: (test.png) is variables of input target image
python3 main.py test.png

required library:
Pillow
colour
numpy
random
matplotlib.pyplot
argparse
"""
pngFiles = []

class OneImage:
    """
    Initialize object as One single image
    5 variables:
    length, width of picture
    fitness score : infinite
    image.array = None
    image = None
    Call function initialize a random pic
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.fitness = float('inf')
        self.array = None
        self.image = None
        self.generateRandomImageArray()

    # Generate a random color as HEX format
    """
    Return a HEX format color code as string
    """
    @staticmethod
    def randomColor():
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    
    
    """
    Using CIE1976 to compare the target image array and self array
    return a fitness score (smaller is better)
    """
    def updateFitness(self, target):
        # It calculates the mean color difference between a target color
        # and an array of colors using the CIE1976 color difference metric
        # Lower fitness scores indicate closer resemblance to the target.
        self.fitness = np.mean(colour.difference.delta_e.delta_E_CIE1976(target, self.array))

    """
    based on the image array to show image to user (for testing)
    """
    def arrayToImage(self):
        im = Image.fromarray(self.array)
        im.show()

    """
    based on the image to get image.array
    """
    @staticmethod
    def imageToArray(image):
        return np.array(image)

    """
    generate a image array randomly
    last few line is updating to local object variable
    """
    def generateRandomImageArray(self):
        counter = random.randint(1, 6)
        region = (self.length + self.width) // 8
        img = Image.new("RGBA", (self.length, self.width), self.randomColor())
        for _ in range(counter):
            pointNumber = random.randint(3, 6)
            xLocation = random.randint(0, self.length)
            yLocation = random.randint(0, self.width)
            locationSet = []
            for _ in range(pointNumber):
                locationSet.append((random.randint(xLocation - region, xLocation + region),
                                    random.randint(yLocation - region, yLocation + region)))
            img1 = ImageDraw.Draw(img)
            img1.polygon(locationSet, fill=self.randomColor())
        self.image = img
        self.array = self.imageToArray(img)


"""
based on the image convert to image.array
"""
def imageToArray(image):
    return np.array(image)

"""
GA processing class
input as target file
"""
class GeneticProcessing:
    def __init__(self, filename):
        image = Image.open(filename)
        self.targetImage = image.resize((200, 200))
        self.length, self.width = self.targetImage.size
        self.targetImageArray = imageToArray(self.targetImage)

    # Starting Running GA !!! 
    def GeneticAlgorithm(self, populationSize, numberGeneration):
        population = []
        # initialize starting population, and update fitness with target_image
        for _ in range(populationSize):
            newOneImage = OneImage(self.length, self.width)
            newOneImage.updateFitness(self.targetImage)
            population.append(newOneImage)

        # GA start
        for i in range(numberGeneration):
            newPopulation = []
            generationSmallestFitness = float('inf')
            # estimate for fitness of fittest OneImage from current epoch's population
            # populate our new population
            while len(newPopulation) < len(population):
                # select parents for crossover
                firstChromosome = self.select(population)
                secondChromosome = self.select(population)

                generationSmallestFitness = min(
                    firstChromosome.fitness, secondChromosome.fitness, generationSmallestFitness)

                # probabilistically determine how child of both parents is created
                randomNumber = random.uniform(0, 1)

                if randomNumber < 0.3:
                    child = self.clone(firstChromosome, secondChromosome)
                    while child is None:
                        firstChromosome = self.select(population)
                        secondChromosome = self.select(population)
                        child = self.clone(firstChromosome, secondChromosome)
                elif randomNumber <= 0.9:
                    child = self.crossover(firstChromosome, secondChromosome)
                    while child is None:
                        firstChromosome = self.select(population)
                        secondChromosome = self.select(population)
                        child = self.crossover(firstChromosome, secondChromosome)
                else:
                    child = self.mutate(firstChromosome)
                    while child is None:
                        firstChromosome = self.select(population)
                        child = self.mutate(firstChromosome)

                # Append the child to newPopulation
                newPopulation.append(child)

            # Set population = newPopulation prepare to next generation
            population = newPopulation

            # Terminal record the fitness and output image as .png
            if i % 25 == 0 or i == numberGeneration - 1:
                print("In generation " + str(i) + " The smallest fitness score = " + str(generationSmallestFitness))
                # Sort based on the object's fitness score, from small to big
                population.sort(key=lambda ind: ind.fitness)
                output = population[0]
                output.image.save("PicturesOutput/Generation=" + str(i) + ".png")
                pngFiles.append("PicturesOutput/Generation=" + str(i) + ".png")
        # Above one generation completed!

        # Finish last generation and sort return the smallest fitness object to main
        population.sort(key=lambda ind: ind.fitness)
        finalFitness = population[0]
        return finalFitness
    def select(self, population):
        subSetSize = 5
        number = np.random.choice(len(population), subSetSize)
        subSet = [population[i] for i in number]
        final = None
        for i in subSet:
            if final is None:
                final = i
            elif i.fitness < final.fitness:
                final = i
        return final

    def clone(self, firstChromosome, secondChromosome):
        child = OneImage(self.length, self.width)
        # Random generate 0 to 1, if alphaPoint = 0 child from firstChromosome
        alphaPoint = random.random()
        childImage = Image.blend(firstChromosome.image, secondChromosome.image, alphaPoint)
        child.image = childImage
        child.array = np.array(childImage)
        child.updateFitness(self.targetImage)
        if child.fitness == min(firstChromosome.fitness, secondChromosome.fitness, child.fitness):
            return child
        return None

    def crossover(self, firstChromosome, secondChromosome):
        number = random.randrange(0, 1)

        # Horizontal crossover point merger image
        if number <= 0.5:
            # random generate crossover point
            crossoverPoint = random.randint(1, self.width)
            first = np.ones((crossoverPoint, self.length))
            first = np.vstack((first, np.zeros((self.width - crossoverPoint, self.length))))
        # Vertical crossover point merger image
        else:
            # random generate crossover point
            crossoverPoint = random.randint(1, self.length)
            first = np.ones((self.width, crossoverPoint))
            first = np.hstack((first, np.zeros((self.width, self.length - crossoverPoint))))
        second = 1 - first

        # Creates the 4 dimensional versions to perform the multiplying across all color channels
        first = np.dstack([first, first, first, first])
        second = np.dstack([second, second, second, second])

        # Multiply firstChromosome with first and multiply secondChromosome with second.
        tempChromo1 = np.multiply(first, firstChromosome.array)
        tempChromo2 = np.multiply(second, secondChromosome.array)
        # produce the crossover child.
        childArray = np.add(tempChromo1, tempChromo2)
        # Create a new child with empty
        child = OneImage(self.length, self.width)
        # Update object image result
        child.image = Image.fromarray(childArray.astype(np.uint8))
        # Update object image array result
        child.array = childArray.astype(np.uint8)
        # Update object image fitness result
        child.updateFitness(self.targetImage)
        # Calculate the child fitness score with two chromosome
        if child.fitness == min(firstChromosome.fitness, secondChromosome.fitness, child.fitness):
            return child
        return None

    def mutate(self, targetObject):
        # counter = the number of image add to
        counter = random.randint(1, 5)
        region = random.randint(1, (self.length + self.width) // 4)
        # Based on the object, run randomColor to create an image
        img = targetObject.image
        for i in range(counter):
            # pointNumber = Each image include the point, start from 3 to number
            pointNumber = random.randint(3, 6)
            xLocation = random.randint(0, self.length)
            yLocation = random.randint(0, self.width)
            locationSet = []
            for j in range(pointNumber):
                locationSet.append((random.randint(xLocation - region, xLocation + region),
                                    random.randint(yLocation - region, yLocation + region)))
            img1 = ImageDraw.Draw(img)
            img1.polygon(locationSet, fill=targetObject.randomColor())
        child = OneImage(targetObject.length, targetObject.width)
        child.image = img
        child.array = child.imageToArray(child.image)
        child.updateFitness(self.targetImage)
        return child
    def imageToArray(image):
        return np.array(image)



def main():
    parser = argparse.ArgumentParser(description="Genetic Algorithm")
    parser.add_argument("inputfile", help="Input target image file, format as .PNG")
    args = parser.parse_args()
    initialPopulation = input("Please input the number of initial population (Integer): ")
    generation = input("Please input the number of generation (Integer): ")
    temp = args.inputfile
    runAlgorithm = GeneticProcessing(temp)
    # Population, Generation
    finalResult = runAlgorithm.GeneticAlgorithm(int(initialPopulation), int(generation))

    plt.imshow(finalResult.image)
    plt.show()

    images = []
    for items in pngFiles:
        img = Image.open(items)
        images.append(img)
    # Save the list of images as a GIF
    images[0].save("Output.gif", save_all=True,
                   append_images=images[1:], duration=500, loop=0)
    print("gif file has been successfully created!")


if __name__ == "__main__":
    main()
