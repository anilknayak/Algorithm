import numpy as np
list_a = [1,2,3,4,5,6,7,8,9,10]

flag = True
start = 0
end = 1
count = 1
new_list = []
while flag:
    count = count + 1
    new_list.append(list_a[start:end])

    start = end
    end = end + count

    if end > len(list_a):
        flag = False

for lst in new_list:
    print(lst, "Sum:",np.sum(lst),"Average:", np.average(lst))