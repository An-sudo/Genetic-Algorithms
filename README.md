# Genetic Algorithm

Author: Yucheng An 

[Genetic Algorithm Practice Project](GA-Practice/README.md)

![Output.gif](Output.gif)
![test.PNG](test.PNG)

## What is this...
This project implements a Genetic Algorithm (GA) to evolve an image based on a given target image. The algorithm iteratively refines a population of candidate images until they closely resemble the target. A .gif is generated to visualize the evolution process.

## Dependencies
To install related libraries

`pip install Pillow colour numpy matplotlib argparse`

Required library:
* Pillow
* colour
* numpy
* random
* matplotlib.pyplot
* argparse

## Run Code
Please run command as: test.png 

>**Note**: Input Image must .png format

`python3 main.py test.png`

>**_Note:_** Please make sure work directory includes an empty directory named "PicturesOutput"
This directory will save every 50 generation of smallest fitness image


## Detail Usage
After running `python3 main.py test.png`

The terminal will have instruction as:

Please input the number of initial population (Integer): _userinput_

Please input the number of generation (Integer): _userinput_

--------------------------------------------------------------------------
For faster computing, program will resize input file as 200 * 200 Pixel

You can change parameter in line:

`self.targetImage = image.resize((200, 200))`

--------------------------------------------------------------------------
> _**Note:**_ Program will generate a named Output.gif file for
every 50 generation of smallest fitness image as gif file after Genetic Algorithm processing