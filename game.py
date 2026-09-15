from enemies.goblin import Goblin
from heros.equipment.weapons import Weapon
from heros.equipment.armor import Armor
from heros.heros.hero import Hero


ARENA_NAME = "Paradox Ring"

def battle(hero: Hero, enemy: Goblin):
    """Simulate a battle between a hero and an enemy."""
    print(f"\n{hero.name} engages in battle with {enemy.name}!")

    while hero.is_alive and enemy.is_alive:
        # Hero attacks first
        damage = hero.attack()
        enemy.take_damage(damage)

        # Enemy attacks back if still alive
        if enemy.is_alive:
            damage = enemy.attack()
            hero.take_damage(damage)

    if hero.is_alive:
        print(f"{hero.name} has defeated {enemy.name}!")
    else:
        print(f"{hero.name} has been defeated by {enemy.name}...")
        
def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    # Create enemies
    goblin = Goblin("Scribble")
    goblinTwo = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    # Create hero and starting armor
    hero = Hero("Peak")

    helmet = Armor("helmet")
    chestplate = Armor("chestplate")
    sword = Weapon("sword")

    hero.equip(helmet)
    hero.equip(chestplate)
    hero.equip(sword)

    hero.show_equipment()

    print(f"\nAttack Power: {hero.attack_power}")

    print(f"{hero.name} enters the arena with {hero.health} health.")


    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
