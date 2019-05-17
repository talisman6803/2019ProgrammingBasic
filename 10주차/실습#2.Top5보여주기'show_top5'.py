def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    for i in range(5):
        if sorted_members [i][1][3] != 0:
            print(i+1, '.', sorted_members[i][0], ':', sorted_members[i][1][3])
        else:
            continue
