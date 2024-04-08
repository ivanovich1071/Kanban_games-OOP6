import random

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Ход игрока {self.player.name}...")
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось здоровья: {self.computer.health}")

            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            print(f"Ход компьютера {self.computer.name}...")
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось здоровья: {self.player.health}")

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")

player_name = input("Введите имя игрока: ")
player_health = int(input("Введите здоровье игрока (10-250): "))
player_attack_power = int(input("Введите силу удара игрока (10-20): "))

computer_health = random.randint(10, 250)
computer_attack_power = random.randint(10, 20)

player = Hero(player_name, player_health, player_attack_power)
computer = Hero("Компьютер", computer_health, computer_attack_power)

game = Game(player, computer)
game.start()

