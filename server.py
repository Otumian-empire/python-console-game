import random
import os
import time
import keyboard



print("Server is running")
print("Game is starting")


# enemy
# hero
# area


# TODO: generate random positions for the characters
# TODO: Check the positioning so that they are not out of bounds
HERO = "#"
INITIAL_HERO_POSITION = 0

ENEMY ="*"
INITIAL_ENEMY_POSITION = 10000

ENVIRONMENT_TILE = "_" 
ENVIRONMENT_HEIGHT = 50
ENVIRONMENT_WIDTH = 100

# blocks basically define the edges of your environment
BLOCK = "\n"

RENDER_TIME = 5 # seconds



def render_environment():
    area = ""
    
    for _ in range(ENVIRONMENT_HEIGHT):
        area += ENVIRONMENT_TILE * ENVIRONMENT_WIDTH + BLOCK
            
    return area


def is_valid_position(area:str, position: int):
    return  0 <= position < len(area)


def is_block_position(area: str, position:int):
    return area[position] == BLOCK
        

def position_character(area:str, character:str, position:int):
    return area[:position] + character + area[position+1:]


def find_proper_position(area: str, position:int):
    if not is_valid_position(area, position):
        position = random.randint(0, len(area)-1)
    
    if is_block_position(area, position):
        position -= 1
        
    return position


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def initialize_game():
    clear_console()
    # before we render the environment, we have to position the character
    # these are the hero and enemy
    area = render_environment()
    print(f"Area: {len(area)}")
    # print(area)

    # position the hero and the enemy
    hero_position = find_proper_position(area, INITIAL_HERO_POSITION)
    area = position_character(area, HERO, hero_position)
    print(f"Hero: {hero_position}")

    enemy_position = find_proper_position(area, INITIAL_ENEMY_POSITION)
    area = position_character(area, ENEMY, enemy_position)
    print(f"Enemy: {enemy_position}")
    
    return area, hero_position, enemy_position


def game_loop():
    hero_position = INITIAL_HERO_POSITION
    # while True:        
    if keyboard.is_pressed("left arrow"):
        print("left pressed")
        hero_position -= 1
    elif  keyboard.is_pressed("right"):
        print("right pressed")
        hero_position += 1
    else:
        print("No key pressed")
        
    # Initialize the game
    area, hero_position, enemy_position = initialize_game()
    
    # Update character positions
    hero_position = find_proper_position(area, hero_position)
    area = position_character(area, HERO, hero_position)

    enemy_position = find_proper_position(area, enemy_position)
    area = position_character(area, ENEMY, enemy_position)

    # Draw the updated screen
    # this is where we render the area for the first time
    print(area)
    time.sleep(RENDER_TIME)


# Start the game loop
game_loop()