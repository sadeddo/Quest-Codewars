def tribonacci(signature, n):
        i=0
        list=[]
        tr=[]
        list.append(signature[0])
        list.append(signature[1])
        list.append(signature[2])
        while i<n:
            d= list[-1] + list [-2] + list [-3]
            list.append(d)
            tr.append(list[i])
            i=i+1
        return tr
#on a utilisé la fonction append qui nous permet d'ajouter les éléments à une liste
