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

print('\n')

for company in companies:
    if company == 'dc':
        print(f'Spiderman is the  best superheroe in {company}')
    else:
        print(f'Batman is the best superheroe in {company}')

#More conditional tests

print("\n","6")

pets = ['fish', 'dog', 'cat', 'lion']


if 'cow' not in pets: 
        Not_in = 'cow' not in pets
        print(f'The cows cant be a mascot  and that is {Not_in}')
else:
        print(f'The cows cant be a mascot  and that is {Not_in}')

    
pets = ['fish', 'dog', 'cat', 'lion']


Is_in = 'serpient' in pets

print("\n")

if Is_in == False: 
        print(f'The serpient can be a mascot  and that is {Is_in}')
else:
        print(f'The cows cant be a mascot  and that is {Not_in}')

print("\nTest for equality and inequality with string")

Cat = 'maine coon'

Other_cat = Cat == 'british'

if Other_cat == Cat: 
    print(f"Is cat == 'british' ? I predict {Other_cat}.")
else:
    print(f"Is cat == 'british' ? I predict {Other_cat}.")


Cat = 'maine coon'

Other_cat = Cat != 'dog'

if Other_cat != Cat: 
    print(f"Is cat != 'dog' ? I predict {Other_cat}.")
else:
    print(f"Is cat != 'dog' ? I predict {Other_cat}.")


print("\nTest using the lower() method")

boy = 'Marcus'

Adult = boy.lower() == 'marcus'

print("Is boy = 'marcus' ? I predict True.")
print(Adult)


Adult = boy.lower() == 'josh'

print("Is boy = 'josh' ? I predict False.")
print(Adult)


print("\nNumerical test")

x = 20

y = 5 

Is_greather = x > y

print("Is x greather than y ? I predict True.")
print(Is_greather)

Is_greather = x < y

print("Is x less than y ? I predict False.")

print(Is_greather)


Kid = 17

Grown_up = 25


No_kid = Kid <= Grown_up

if No_kid == True:
    print("\nAre you a grown up? I predict true")
    print(No_kid)
else:
    print("\nAre you a grown up? I predict false")
    print(No_kid)


No_kid = Kid >= Grown_up

if No_kid == False:
    print("\nAre you a grown up? I predict False")
    print(No_kid)
else:
    print("\nAre you a grown up? I predict True")
    print(No_kid)

d = 43

c = 62

Statement = (d < c) or (c > d)

if Statement == False:
    print("\nThis statement is real? I predict False")
    print(Statement)
else:
    print("\nThis stamente is real ?I predict True")
    print(Statement)

Statement = (d < c) and (c > d)

if Statement == False:
    print("\nThis statement is real? I predict True")
    print(Statement)
else:
    print("\nThis stamente is real ?I predict False")
    print(Statement)
print("\nThis statement will absolute true cause the statement will not be there cause is true and if is false is not going to be anywhere unless will be in a loop")
print(Statement)

if (64 > 10 ) or (10 > 64):
    print("\nYou got it")
else:
    print("\nYou don't got it")

if (64 > 10 ) and (10 < 64):
    print("\nYou got it")
else:
    print("\nYou don't got it")


print("\nTests using the and keyword and the or keyword")
Garage = ['tesla', 'bmw', 'ferrari', 'ford']

if ('porsche' in Garage) or ('tesla' in Garage):
    print('\nWhether of the two cars are in my garage')
else:
    print('Whether of the two cars are not in my garage')


if ('bmw' in Garage) or ('tesla' in Garage):
    print('\nWhether of the two cars are in my garage')
else:
    print('Whether of the two cars are not in my garage')


if ('volkswagen' in Garage) or ('seat' in Garage):
    print('\nWhether of the two cars are in my garage')
else:
    print('\nWhether of the two cars are not in my garage')



print("\nTest whether an item is in a list")

subjects = ['english', 'regional language', 'computer basic']

def favorite(subjects):
    n = 0
    for subject in subjects:  
        n = n + 1
        print("\n",n," ",subject)

if 'regional language' in subjects:
    print('\nYou chose regional language as your favorite subject:')
    del subjects[1]
    subjects.insert(0,'regional language')

favorite(subjects)

print("\nTest whether an item is not in a list")

if 'computer science' not in subjects:
    print('\nYou chose computer science as your favorite subject:')
    subjects.insert(0,'computer science')

favorite(subjects)
