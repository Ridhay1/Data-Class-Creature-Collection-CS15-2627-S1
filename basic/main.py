from dataclasses import dataclass
@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float

creature1 = Creature("Drako","Dragon", 10, 95.5)
creature2 = Creature("Blazer","Gecko", 9, 100)
creature3 = Creature("Blazer","Gecko", 15, 90)

print(creature1.species)
print(creature2.species)
print(creature3.species)
print(creature1.health)
print(creature2.health)
print(creature3.health)
print(creature1.name)
print(creature2.name)
print(creature3.name)
print(creature1.level)
print(creature2.level)
print(creature3.level)

creature1.health = 140
creature1.level = 20
print(creature1.health)
print(creature1.level)
print(creature1.name)
print(creature1.species)

print(creature2.level)
print(creature2.health)

print(creature3.level)
print(creature3.health)