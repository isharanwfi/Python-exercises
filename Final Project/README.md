# CALL OF DUTY: Finding Duty

**Ishara Nushangani** 

## Idea and objective
Duty, a friendly Golden Retriever, is lost. The player searches the town, earns coins, collects clues and items, and must bring Duty home safely.

**Objective:** unlock the Clinic (15 coins), buy a dog whistle (5 coins), enter the Forest and find Duty.

## How it works
- Start with your name and age. Under 12 the game says you are a minor and shuts down.
- Main menu: Start a New Game, Continue a saved game, Instructions, or type `lopeta` to quit.
- Locations: Park, Shop, Neighborhood, Clinic, Forest. You can walk to a place or explore a random one.
- Searching is random: coins, clues, bottles or nothing.
- The Park hides a map under the old bench (a hint clue points to it).
- Without the unlocked Clinic and the whistle, the Forest cannot be entered.
- Finding Duty ends the game with a congratulations message.

## Routes to win (several ways to get the coins)
1. **Searching:** keep searching Park, Shop, Neighborhood for random coins.
2. **Recycling:** collect empty bottles and sell them at the Shop (2 coins each).
3. **Map:** find the map under the bench, use it at the Shop for 10 coins.
4. **Helping:** find the neighbour's keys in the Neighborhood and return them for 8 coins.

## Saving
Progress is saved to `saves/<name>.txt`. Choose "Continue a saved game" and use the same name to carry on.

## Project structure
```
project/
  main.py             menus and main loop
  README.md
  data/intro.txt     intro text (read from file)
  data/instructions.txt
  game/classes.py     classes Item, Room, Player
  game/rules.py       game logic and the Game class
  game/files.py       reading text files, saving and loading
  saves/             save files (created while playing)
```

## Sustainable development
- protecting animals and forests.
- recycling bottles earns coins.
- helping neighbours and keeping places clean.
- pet care at the clinic.

## Run
`python main.py` 
