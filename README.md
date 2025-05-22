Rat Breeding Simulator  
======================

By Ellis Simmons – April 2024  
Made with Python  

What is this?
-------------
This is a fun little script that simulates breeding rats to reach a target average weight.  
You start with a bunch of randomly-sized rats, breed the biggest ones, maybe mutate a few, and repeat until you’ve got a population with the average weight you want (or until you run out of time/patience).

What’s actually happening?
-------------------------
- You set a goal weight (it picks a random number between 50k and 75k grams).
- A bunch of rats are created with weights from a triangular distribution (most around 300g).
- Every generation:
  - Only the biggest rats are allowed to breed.
  - They make babies.
  - Some of those babies randomly mutate (some good, some bad).
  - The process repeats until the average population weight hits the goal.

Key settings (aka the knobs you can mess with):
----------------------------------------------
goal = random.randint(50000, 75000)  # How chunky you want the average rat to be  
numRats = 20                         # Number of adult rats in your lab  
initialMinWt = 200                   # Smallest rat weight in the start  
initialMaxWt = 600                   # Biggest rat weight in the start  
initialModeWt = 300                  # Most common weight in the starting group  
mutateOdds = 0.01                   # Chance that a rat mutates  
mutateMin = 0.5                     # Least helpful mutation scale (50% smaller)  
mutateMax = 1.2                     # Most helpful mutation scale (20% bigger)  
litterSize = 8                      # How many pups a pair makes  
generationLimit = 50000             # Max number of generations allowed  
littersPerYear = 5                  # How many generations happen each year  

What you'll see in the console:
-------------------------------
- Initial population and average fitness (how close it is to the goal).  
- Updates every 50 generations.  
- A list of average weights over time.  
- Final number of generations and how many years that took.  
- A win message if the rats hit the weight goal.

How to run it:
--------------
1. Install Python (if you don’t have it).  
2. Run the script in any Python IDE or terminal with:  
   `python your_script_name.py`  
3. Sit back and let the rats do their thing.

Inspired by:
------------
- Daniel Shiffman’s genetic algorithms series  
- Evolutionary biology (in a very, very simplified form)  
- Neil deGrasse Tyson, because he's made me think about science in a cool way  
- The Python Projects book  

Notes:
------
- This isn’t exactly science, but it *is* a decent way to visualize basic evolutionary pressure and selection.  
- If your rats aren't hitting the goal, try cranking up the mutation range or increasing litter size.

---
As per usual, if you're going to steal or use it at least credit me please. Thank you for reading and have a nice day.
