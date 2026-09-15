from goblin import Goblin
from hero import Hero


ARENA_NAME = "Paradox Ring"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Gribble")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    hero = Hero("Peak")

    print(f"{hero.name} enters the arena with {hero.health} health.")

    current_attack = hero.attack()

    goblin.take_damage(current_attack)
    if goblin.is_alive:
        current_attack = goblin.attack()
        hero.take_damage(current_attack)


    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
