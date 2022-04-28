A,B,C,D=input().split(' ')
a=float(A)
b=float(B)
c=float(C)
d=float(D)
F=((a*2)+(b*3)+(c*4)+d*1)/10
print(f'Media: {F:.1f}')
if F>=7:
 print('Aluno aprovado.')
if F<5:
 print('Aluno reprovado.')
if 5<=F<=6.9:
   print('Aluno em exame.')
   E=float(input('Nota do exame: '))
   F2=(E+F)/2
   if F2>=5:
    print('Aluno aprovado.')
    print(f'Media final: {F2:.1f}')
   else:
    print('Aluno reprovado.')
    print(f'Media final: {F2:.1f}')