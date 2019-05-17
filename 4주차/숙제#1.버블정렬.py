def bubblesort(ns):
    for k in range(len(ns)):
        for i in range(len(ns)-1):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns
