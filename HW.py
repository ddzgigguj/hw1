class SuperHero:
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase

    def Name_Hero(self):
        return (f'Hero`s name: {self.name}')

    def Health_is_double(self):
        self.health_points *= 2

    def __str__(self):
        return (f'NickName: {self.nickname}\nSuperPower: {self.superpower}\nHealthPoints: {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)

Hero=SuperHero(name='Samael', nickname='Angel', superpower='Flight', health_points=100,catchphrase='deus lo vult')

print(Hero.Name_Hero())
print(f'HealthPoints before: {Hero.health_points}')
Hero.Health_is_double()
print(f'Health points after doubling: {Hero.health_points}')
print(str(Hero))
print(f'Catchphrase length: {len(Hero)}')

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def Health_is_double(self):
        SuperHero.Health_is_double(self)
        self.health_points **= 2
        self.fly=True
    def fly_phrase(self):
        return 'fly in the True_phrase'

class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def Health_is_double(self):
        SuperHero.Health_is_double(self)
        self.health_points **= 2
        self.fly=True
    def fly_phrase(self):
        return "Fly in the True_phrase: Yes"

# Создание экземпляров подклассов
air_hero=AirHero(name='Aeris',nickname='Skyhawk',superpower='Wind Manipulation',
                 health_points=50,catchphrase='Soaring High',damage=80)
space_hero=SpaceHero(name='Stella',nickname='Star Voyager',superpower='Gravity Control',
                     health_points=100, catchphrase='Exploring the Cosmos',damage=70)
class Villain(SpaceHero):
    people = 'monster'

    def gen_x(self):...

    def crit(self, damage):
        return damage ** 2

villain=Villain(name='Eddie',nickname='Venom',superpower='Buff physical strength',
                health_points=100,catchphrase='You only disgrace us',damage=50)

print('\n')
print(air_hero.Name_Hero())
print(f'HealthPoints before: {air_hero.health_points}')
air_hero.Health_is_double()
print(f'Health points after doubling: {air_hero.health_points}')
print(str(air_hero))
print(f'Catchphrase length: {len(air_hero)}')
print(f'Damage: {air_hero.damage}')
print(f'Fly: {air_hero.fly}')

print('\n')
print(space_hero.Name_Hero())
print(f'HealthPoints before: {space_hero.health_points}')
space_hero.Health_is_double()
print(f'Health points after doubling: {space_hero.health_points}')
print(str(space_hero))
print(f'Catchphrase length: {len(space_hero)}')
print(f'Damage: {space_hero.damage}')
print(f'Fly: {space_hero.fly}')

print('\n')
print(villain.Name_Hero())
print(f'HealthPoints before: {villain.health_points}')
villain.Health_is_double()
print(f'Health points after doubling: {villain.health_points}')
print(str(villain))
print(f'Catchphrase length: {len(villain)}')
print(f'Damage: {villain.damage}')
print(f'Fly: {villain.fly}')

hero_damage = 50
hero_crit_result = villain.crit(hero_damage)
print(f'Critical damage for hero: {hero_crit_result}')