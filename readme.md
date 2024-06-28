# Multiverse Experiment 1

## Introduction
This experiment is a simple demonstration of the multiverse concept. The experiment is based on the idea that every time a decision is made, the universe splits into multiple universes, each representing a different outcome of the decision. In this experiment, we will explore the concept of the multiverse by simulating a series of decisions and observing the resulting universes.

## How it works
The script will ask you 4 questions, 2 of them have 2 possible answers, and 2 of them have 3 possible answers.

The script will generate all possible combinations of answers to the questions, creating a universe for each combination.
```python3
def generate_universes(questions):
    keys = sorted(questions.keys())
    options = [questions[key] for key in keys]
    universes = []

    for combo in itertools.product(*options):
        universe = {keys[i]: combo[i] for i in range(len(keys))}
        universes.append(universe)

    return universes
```
All it does is generate all possible combinations of answers to the questions, creating a universe for each combination.


## Running the experiment
To run the experiment, simply run the script `main.py` and follow the instructions.

```bash
Please answer the following questions:
Q1: Do you like ice cream? (yes/no) yes
Q2: Is today a sunny day? (true/false) true
Q3: Choose a random letter (a, b, c) b
Q4: Pick a random number (1, 2, 3) 2

Your answers:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): b
Q4: Pick a random number (1, 2, 3): 2

Generating possible universes...

Interactive shell:

Enter command ('all' to show all universes, 'vX' to visit universe X, 'exit' to quit): v30
+-------------------------+-------------------------+
|      Your Universe      |       Universe 30       |
+-------------------------+-------------------------+
| yes                     | no                      |
| true                    | false                   |
| b                       | a                       |
| 2                       | 3                       |
+-------------------------+-------------------------+
```

## Example output of some of the universes
```
Universe 1:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): a
Q4: Pick a random number (1, 2, 3): 1

Universe 2:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): a
Q4: Pick a random number (1, 2, 3): 2

Universe 3:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): a
Q4: Pick a random number (1, 2, 3): 3

Universe 4:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): b
Q4: Pick a random number (1, 2, 3): 1

Universe 5:
Q1: Do you like ice cream? (yes/no): yes
Q2: Is today a sunny day? (true/false): true
Q3: Choose a random letter (a, b, c): b
Q4: Pick a random number (1, 2, 3): 2
```
As you can see, each universe represents a different combination of answers to the questions, nothing too fancy.

## Conclusion
The multiverse concept is a fascinating idea that has captured the imagination of many people. While it is still a theoretical concept, it is interesting to think about the implications of a multiverse on our understanding of the universe and our place in it. This experiment is a simple demonstration of the multiverse concept and how it might work in practice. It is a fun way to explore the idea of multiple universes and how they might be created by the decisions we make.
