# Implement Genetic-Algorithms

## Files Structure

`GA.py`: Source-code built by Python3

`genAlgData1.txt` and `genAlgData2.txt `contain training data based on 30 years of price data for the S&P 500.

---

## Example of training data:

-0.12 -0.81 -6.8

-0.81 -0.41 5.2

-0.41 0.32 -3.21

0.32 -0.2 -4.48

.....

---

## Explanation: 

Each row of the file contains `3` real numbers:

  • The `first` number represents the percentage price change from one day to the next of the S&P
500 stock index.

  • The `second` number represents the percentage price change on the following day.
  
  • The `third` number represents the profit in dollars that you would have made if you had bought an ETF of the stock market index and held it for one day 
  **(negative numbers represent losing money)**.

---

## Instruction to use:

1. Repo clone:

```bash
git clone https://github.com/Yucheng-An/Genetic-Algorithms.git
```

2. Access work directory:

```bash
cd Genetic-Algorithms
```

3. Run `GA.py`

```bash
python3 GA.py
```

4. Follow the instructions and input the value

Example: `genAlgData1.txt` or `genAlgData2.txt`

    Please enter the number of chromosomes: 100
    The initial Population will be: 100
    Please enter the number of X(0-100%): 10
    X will be 10 %
    Please enter the number of Z(0-100%): 10
    Z will be 10 % 
    Please enter the data name .txt(must be on the current directory): genAlgData1.txt
    Your data file name genAlgData1.txt
    Please input crossover algorithm(u=uniform,k=kpoint):u
    The crossover algorithm is uniform
    Please input the number of generations you want(Integer):100
    100  generations you want to create.
    Every 10 Generation state(Min,Max,Average) [-2278.13, 4182.46, 627.6]
    Every 10 Generation state(Min,Max,Average) [-816.38, 4358.92, 956.95]
    Every 10 Generation state(Min,Max,Average) [-572.97, 4540.3, 1018.74]
    Every 10 Generation state(Min,Max,Average) [-695.34, 4444.36, 918.1]
    Every 10 Generation state(Min,Max,Average) [-709.11, 4546.03, 936.7]
    Every 10 Generation state(Min,Max,Average) [-523.7, 4291.81, 957.63]
    Every 10 Generation state(Min,Max,Average) [-672.28, 4253.16, 964.94]
    Every 10 Generation state(Min,Max,Average) [-721.25, 4400.01, 1029.82]
    Every 10 Generation state(Min,Max,Average) [-692.56, 4551.64, 1042.95]
    From the final generation:
    The Highest fitness score:  4618.97
    The Highest fitness chromosome: [-0.73, 1.36, -2.02, 1.15, 0.0]