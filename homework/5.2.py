import collections
persons = [
    {
        "name": "Anna",
        "age": "51",
        "gender": "Female"
    },
    {
        "name": "Konstantsin",
        "age": "37",
        "gender": "Male"
    },
    {
        "name": "Anna",
        "age": "17",
        "gender": "Female"
    },
    {
        "name": "Fedor",
        "age": "36",
        "gender": "Male"
    }
]
man = 0
woman = 0
all = 0
vosrast18 = 0
for i in (persons):
    all +=1
    if i['gender']=='Male':
        man+=1
    if i['gender']=='Female':
        woman+=1
    if i['age']>='18':
        vosrast18+=1
print (f'В списке всего {all} человек. Из них {man} мужчин и {woman} женщин. Совершеннолентних - {vosrast18} .')

names = [i['name'] for i in persons]
print (f'Список: {names}')

ages = [i['age'] for i in persons]
print (f'Список возрастов без повторений: {sorted (set(ages)) }')

man_35 = [i['name'] for i in persons if i['age']>'35' and i['gender'] == 'Male' and 'F' in i['name']]
print (f'Мужчины старше 35-ти с именем на "F" : {man_35}')

Counter = collections.Counter(names)
print (f'Три самых встречающихся имени: {Counter.most_common(3)}')
    
