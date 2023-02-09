points = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}
      
word = input("Enter word: ").upper()
sum = 0
for i in word:
    for k, v in points.items():
        if i in v:
            sum+=k
print(sum)
