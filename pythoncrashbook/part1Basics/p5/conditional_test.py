car = 'subaru'
print("Is car = 'subaru' ? I predict True.")
print(car == 'subaru')
print("\n","Is car = 'audi' ? I predict False.")
print(car == 'audi')

#conditional-test

print("\n","1")
banned = ['videogames', 'games', 'gossip']

print("Is banned = 'talk' ? I predict False.")

Is_banned = 'talk' in banned

print(Is_banned)

print("\n","Is banned = 'games' ? I predict True.")

Is_banned = 'games'in banned 

print(Is_banned)


print("\n","2")

soda = ['cocacola', 'drpepper', 'fanta']

print("Is soda not have 'pepsi' ? I predict True.")

Is_soda = 'pepsi' not in soda

print(Is_soda)

print("\n","Is soda not have 'fanta' ? I predict False.")

Is_soda = 'fanta'not in soda 

print(Is_soda)


print("\n","3")

age_0 = 10

age_1 = 18

Under_age = age_1 <= age_0

print("\n","Is Under_age  False.")

print(Under_age)

Under_age = age_1 >= age_0

print("\n","Is Under_age  True.")


print(Under_age)


print("\n","4")

Topic = 'Artificial inteligence'

Other_topic = Topic.lower() == 'artificial inteligence'

print("\n","Is  Other_topic not have 'articial inteligence' ? I predict True.")

print(Other_topic)

Other_topic = Topic.lower() != 'artificial inteligence'


Other_topic = Topic.lower() != 'artificial inteligence'

print("\n","Is  Other_topic not have 'articial inteligence' ? I predict False.")

print(Other_topic)

print("\n","4")

Crush = 'martha'

Old_crush = Crush == 'antonia'


print("\n",f"Is {Crush} not antonia? I predict False")
print(Old_crush)

Old_crush = Crush == 'martha'

print("\n",f"Is {Crush} equal to martha? I predict True")
print(Old_crush)


print("\n","5")

companies = ['dc', 'marvel']

for company in companies:
    if company == 'dc':
        print(f'Batman is the best superheroe in {company}')
    else:
        print(f'Spiderman is the  best superheroe in {company}')

companies = ['marvel', 'dc']


for company in companies:
    if company == 'dc':
        print(f'Spiderman is the  best superheroe in {company}')
    else:
        print(f'Batman is the best superheroe in {company}')


