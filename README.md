# ALGOINVEST&TRADE

This is my third Python project for Openclassrooms courses.

In this scenario I have just joined AlgoInvest&Trade, a financial company. The company seeks to optimize its investment strategies using algorithms, in order to generate more profits for their customers.

Here are the constraints:

Each share can only be purchased once.

We cannot buy a fractional share.

We can spend a maximum of 500 euros per customer.

The first program tries all the different combinations of actions that fit our constraints, and chooses the best result. This type of algorithm is called "Bruteforce". It is accurate but his algorithmic complexity is O(n^2) which is problematic with a lot of data

The second program use different approach with dynamic programming. He uses a matrix to find the best optimize results and avoid lot of calculations. His algorithm complexity is O(n)

## Installation

This script needs Python installed and some packages detailled in requirements.txt.

Clone the repo with your terminal 

```
```bash
  git clone https://github.com/bendms/algoinvest.git

```
    
## Configuration 

Go to the project directory

```
  cd algoinvest/
```

Run the script using Python commande in terminal from chess_tournament_manager folder :

```
  python bruteforce.py 
```

```
  python optimized.py 
```
