def radixsort(ds,length) :
    for i in range(length) :
        part = [[],[],[],[],[],[],[],[],[],[]]
        for j in range(len(ds)) :
            part[int(ds[j][length-i-1])].append(ds[j])
        ds = part[0] + part[1] + part[2] + part[3] + part[4] + part[5] + part[6] + part[7] + part[8] + part[9]
    return ds
