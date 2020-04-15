import random

# example of how random.seed(num) will produce the same random result given the same num.
# for i in range(5):
#     random.seed(i)
    # print(random.random())

# print("First random", random.random())
# print("Second random", random.random())
# print("Third random", random.random())
# print("Fourth random", random.random())
# print("Fifth random", random.random())


# Fisher-Yates Shuffle  -  https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
'''
Here's the basic algorithm:
    - Begin with a list of N elements
    - Swap the first element with the i-th element, where i is a random position.
    - Repeat this for each element, in order, until you reach the end of the list.
'''


l = [0,1,2,3,4,5,6]
print(f"original List: {l}")
# get random index between 0 and the lenght of the list -1 (n-1) and use that number as the location to swap with the first element l[0] in list.  i.e. if we get 2, then we would swap l[0] with l[2]
for i in range(len(l)):
    # print(f"current index is: {i}")
    rand_index = random.randint(i,len(l)-1)
    # print(f"random index: {rand_index}")

    # swap first element with randomly generated indexed element
    l[i], l[rand_index] = l[rand_index], l[i]
    print(f"swapping index l[{i}] with random index l[{rand_index}]")

    print(f"altered list: {l}\n\n")





