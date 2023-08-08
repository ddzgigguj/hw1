class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        return f"Hero's name: {self.name}"

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}\nSuperpower: {self.superpower}\nHealth: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)



hero = SuperHero("Clark Kent", "Superman", "Flight", 100, "Up, up and away!")


print(hero.display_name())
print(f"Health points before: {hero.health_points}")
hero.double_health()
print(f"Health points after doubling: {hero.health_points}")
print(str(hero))
print(f"Catchphrase length: {len(hero)}")
