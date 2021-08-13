user_list = input(("Enter ur List separated by commas (ex: 4 , 5 , 6):"))
devisor = int(input("Enter The Devisor: "))
ans = []
for each_element in user_list.split(', '):
    if int(each_element) % devisor == 0:
        ans.append(int(each_element))
print("ur list after edition is:", end=' ')
print(ans)
