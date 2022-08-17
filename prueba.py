'''    for i in probando:
        if i not in archivos:
            archivos.append(i)
        else:
            repetidos.append(i)
    print(repetidos)'''
'''if str(prueba[0]) in probando[contador]:
            print("Yo ya existo")
            probando[contador][0] = str(prueba[0])
            probando[contador][1] = str(prueba[1])
            probando[contador][2] = str(prueba[2])
            probando[contador][3] = str(prueba[3])
            probando[contador][4] = str(prueba[4])
            probando[contador][5] = str(prueba[5])
            probando[contador][6] = str(prueba[6])'''

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    visited = set()
    dup = [x for x in nums if x in visited or (visited.add(x) or False)]
 
    print(dup)  # [1, 5, 1]