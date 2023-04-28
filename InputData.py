
Make, New, Change = True, True,True
while Make==True :
    Answer =str(input('Ввести новую матрицу (Д/Н):'))
    if Answer in ['N','n','Н','н'] : 
        print ('\n До новых встреч !')
        Make = False
#    else:
#        d=Matrica() 
#        d.Input_Matrica()
#        d.Print_Matrica('Новая матрица')