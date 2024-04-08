class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0
hero1 = Hero("Герой 1")
hero2 = Hero("Герой 2")

print(f"{hero1.name} атакует {hero2.name}...")
hero1.attack(hero2)
print(f"У {hero2.name} осталось здоровья: {hero2.health}")

print(f"{hero1.name} жив? {hero1.is_alive()}")
print(f"{hero2.name} жив? {hero2.is_alive()}")