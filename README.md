# diceroll
## Final Group 1 - Dice Roll Project: Source Code

### Use the random module
```python
import random
```
### Makes the code loop indefinitely
```python
while True:
  #Accept user input
```
### Ask the user for the number of dice to roll
```python
num_dice = int(input("Enter the number of dice to roll: "))
```
### If the user enters 0, terminate the program
```python
if num_dice == 0:
  break
```

### Ask the user for the number of sides per die
```python
num_sides = int(input("Enter the number of sides per die: "))
```
### If the user enters 0, terminate the program
```python
if num_sides == 0:
  break
```

### Inititalize a list to hold the results of the dice rolls
```python
results = []
```

### Roll the dice and add the result to the list using the random module
```python
for i in range(num_dice):
  result = random.randint(1, num_sides)
  results.append(result)
```

### Print the results
```python
print("The result is:", results)
```
