
#Problem 1
employees=['Beth','Fred','Drew','Alex','Emma','Chad']
years=[15,11,8,5,4,2]
employees.insert(1,'Geena')
years.insert(1,12)
employees.insert(6,'Herb')
years.insert(6,3)
employees.insert(8,'Iris')
years.insert(8,0)
print(employees)
print(years)
#Problem 2
length = [22.7, 22.4, 25.8, 21.3, 20.1, 22.1, 21.1, 25.3, 26.9, 26.9,23.0, 23.8, 26.2, 20.4, 23.0, 21.9, 23.5, 27.8, 25.3, 25.9]
weight = [9.2, 8.8, 10.7, 8.3, 6.2, 8.6, 7.2, 11.2, 10.5, 11.3,9.6, 9.9, 10.9, 5.9, 9.5, 9.1, 9.7, 11.6, 10.2, 10.5]
pred_weight = []

for i in range(0,len(length)):
    calcform = 0.6 * length[i] - 5.2
    pred_weight.append(round(calcform, 2))
    
print(pred_weight)

SSE = 0
for i in range(0,len(weight)):
    squarediff = (weight[i] - pred_weight[i]) ** 2
    SSE = SSE + squarediff
    
print(round(SSE,4))


#Problem 3
correct = ['D', 'B', 'C', 'A', 'C', 'D', 'A', 'C', 'C', 'B', 'D', 'A', 'B', 'D', 'C', 'D', 'C', 'D', 'C', 'A', 'B', 'D', 'C', 'B', 'A']
answers1 = ['A', 'B', 'C', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'D', 'A', 'D', 'C', 'C', 'B', 'C', 'D', 'B', 'A', 'D', 'D', 'C', 'C', 'A']
answers2 = ['D', 'A', 'C', 'A', 'B', 'D', 'A', 'C', 'C', 'B', 'D', 'A', 'B', 'D', 'A', 'D', 'C', 'D', 'C', 'A', 'B', 'C', 'C', 'B', 'A']
count1 = 0
count2 = 0 
for i in range(len(correct)):
    if answers1[i]==correct[i]:
        count1+=1
    if answers2[i]==correct[i]:
        count2+=1
grade1=(int(count1*100/len(correct)))
grade2=(int(count2*100/len(correct)))
print(f'Student 1 Grade: {grade1}%')
print(f'Student 2 Grade: {grade2}%')


#Problem 4
import math
i = 0.4
n = 360
start = 100000
increment = 10000
for k in range(start,200001,increment):
  L = k
  PMT = round((L*i)/(1- math.pow(1+i,-n)),2)
  print('A loan of ${} would require monthly payments of ${}'.format(L,PMT))

#Problem 5
quantities = [84,100,126,150,186,200,216,248]
cost = 0 
for i in range(0, len(quantities)):
    if quantities[i]<=100:
        cost = (quantities[i]*350)
        print(f'The cost for an order of {quantities[i]} is ${cost}.')
    elif quantities[i] >= 100 and quantities[i] <= 200:
        cost = cost + (quantities[i] * 300)
        print(f'The cost for an order of {quantities[i]} is ${cost}.')
    elif quantities[i] >= 200:
        cost = cost + (quantities[i] * 250)
        print(f'The cost for an order of {quantities[i]} is ${cost}.')

#Problem 6
A=[[13,43,28,22,41],[17,39,46,16,21],[41,34,31,25,14]]
B=[[35,29,43,21,31],[48,26,19,17,23],[32,34,24,16,27]]
AplusB = [],[],[]
for i in range(0,3,1):
    for j in range(0,5,1):
        sum=A[i][j] +B[i][j]
        AplusB[i].append(sum)
for i in range(0,3,1):
    for j in range(0,5,1):
        print(AplusB[i][j],end=" ")
    print()


