class Character:
    def __init__(self, *, level) -> None:
        self.level = level
        self.health = self.base_health_level * level
        self.attack_power = self.base_attack_power * level

    def attack(self) -> None:
        print(f"{self.race_name} attack with {self.attack_power} power!")

    def __str__(self) -> str:
        return f"{self.race_name}: level {self.level}, hp: {self.health}"


class Ork(Character):
    race_name = 'Ork'
    base_health_level = 100
    base_attack_power = 10


class Elf(Character):
    race_name = 'Elf'
    base_health_level = 50
    base_attack_power = 15


ork = Ork(level=25)
elf = Elf(level=27)

print(ork)
print(elf)

elf.attack()
ork.attack()
