num = int (input('Введите количество треугольников ',))             
list = []                                                            
c = 0                                                               
for i in range (1,num+1):                                           
    k1 = int (input(f'Введите первый катет {i}-го треугольника '))
    list.append(k1)
    k2 = int (input(f'Введите второй катет {i}-го треугольника '))
    list.append(k2)
for l in range (0,len(list),2):                                        
    square = ((list[l])*(list[l+1])/2)
    gipot = ((((list[l])**2))+(((list[l+1])**2)))**0.5
    c+=1
    print(f'Треугольник {c} c катетами {list[l]} и {list[l+1]} имеет площадь {square} и гипотенузу {gipot}')
