# Some usefull functions

def find_TBU(x, y_array):
    if y_array == []:                   #To jest związane z wartością domyslna funkcji wyżej, gdzie jak arra = [] to wtedy liczy po całym
        return 1
    else:
        for i in range(0,len(y_array)): #Iteracja po mojej zgłoszonej liście kolumn
            if x == y_array[i]:         #Jeżeli gdzieś się pojawi ta moja to wtedy zwracaj True i program wyższy jedzie dalej 
                return 1
            
def zapisz_txt(my_array, delimit, file_name):
    plik_2 = open(file_name, 'w')
    for i in my_array:
        try: 
            for j in i: 
                plik_2.writelines(str(j)+ delimit)
            plik_2.writelines("\n")
        except:
            plik_2.writelines(str(i)+ "\n")
  
    plik_2.close()