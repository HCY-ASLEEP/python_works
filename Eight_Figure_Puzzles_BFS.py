import numpy
import copy
import time

#Notice how to use numpy to develop multidimensional array
#Notice how to find out if two mulitimensional array same or not created by numpy
#Notice how to use global variable
#Notice how to make a list resersed
#Notice how to get length of a list
#Notice ususally data in a list is not interger!See line 63!

#Every node can generate four different nodes at most, one is the father, the others are the sons

#There are for values to calculate the runningtime
#There three periods in this programe, first peroid before input, second period during input, third peroid after input
#When I count the total time, I ignore the inputting time
start_pre=time.time()


#Count total steps
total_steps = 0


#Count factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


#To avoid record the same
have_been_exist_or_not = numpy.zeros((9, 9, 9, 9, 9, 9, 9, 9, 9))

#Every matrix has a wall surrounded by '0'
#Every matrix chooses '9' to be the empty
init_num = numpy.zeros((5, 5))
result = numpy.zeros((5, 5))

result[1][1] = 1
result[1][2] = 2
result[1][3] = 3

result[2][1] = 8
result[2][2] = 9
result[2][3] = 4

result[3][1] = 7
result[3][2] = 6
result[3][3] = 5


#Set value in have_been_exist_or_not_value
#Judge if it is the end we want
def set_get_have_been_exist_or_not_value___judge_end(data):

    global total_steps
    total_steps += 1

    #If result founded, return -1
    #Notice!
    if (data - result).any() == False:
        return -1

    #Find out index of have_been_exist_or_not list for every matrix
    index = []
    for i in range(3):
        for j in range(3):
            index.append(data[i + 1][j + 1] - 1)

    #If it has already existed, return 0
    #Notice!
    if have_been_exist_or_not[int(
        index[0])][int(index[1])][int(index[2])][int(
        index[3])][int(index[4])][int(index[5])][int(
        index[6])][int(index[7])][int(index[8])] == 1:
        return 0

    #If it has not existed, make this matrix recorded in have_been_exist_or_not list, then return 1
    else:
        have_been_exist_or_not[int(index[0])][int(index[1])][int(index[2])][int(
                                   index[3])][int(index[4])][int(index[5])][int(
                                   index[6])][int(index[7])][int(index[8])] = 1
        return 1


class node:
    parent = None
    data = []

    def __init__(self, data):
        self.data = data

    def add_parent(self, parent):
        self.parent = parent

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent


#A node should be in open_list if it has not children
#A node should be in close_list if it already has children
open_list = []
close_list = []

end_pre=time.time()

print("input you init nums")

for i in range(3):
    for j in range(3):
        position_tip = i * 3 + j + 1
        init_num[i + 1][j + 1] = int(
            input("input " + str(position_tip) + " num" + "\n"))

start_dealing=time.time()

init_node = node(init_num)
set_get_have_been_exist_or_not_value___judge_end(init_num)
open_list.append(init_node)

result_node = node(result)
set_get_have_been_exist_or_not_value___judge_end(result)
close_list.append(result_node)

#There are factorial(9) nodes at most
size = factorial(9)
for t in range(size):

    father = open_list[0].get_data()
    i_9 = 0
    j_9 = 0

    #Find where is the empty one in a matrix
    for i in range(3):
        for j in range(3):
            if father[i + 1][j + 1] == 9:
                i_9 = i + 1
                j_9 = j + 1
                break


    if father[i_9 - 1][j_9]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9 - 1][j_9]
        kid[i_9 - 1][j_9] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:

            node_up = node(kid)
            node_up.add_parent(open_list[0])
            open_list.append(node_up)

    if father[i_9 + 1][j_9]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9 + 1][j_9]
        kid[i_9 + 1][j_9] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Beak now!")
            break

        if flag == 1:

            node_down = node(kid)
            node_down.add_parent(open_list[0])
            open_list.append(node_down)


    if father[i_9][j_9 - 1]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9][j_9 - 1]
        kid[i_9][j_9 - 1] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:

            node_left = node(kid)
            node_left.add_parent(open_list[0])
            open_list.append(node_left)

    if father[i_9][j_9 + 1]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9][j_9 + 1]
        kid[i_9][j_9 + 1] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:

            node_right = node(kid)
            node_right.add_parent(open_list[0])
            open_list.append(node_right)

    #Change a node from kid to parent
    close_list.append(open_list[0])
    del (open_list[0])

print("Total steps is:", total_steps)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

finder = close_list[0]

final_list = []
while finder != None:
    final_list.append(finder.get_data())
    finder = finder.get_parent()

#Notice!
length_final_list = len(final_list)

#Notice!
final_list.reverse()

print("The final_list length is", length_final_list)

for i in range(length_final_list):
    print(final_list[i])
    print("*********************************")

end_dealing=time.time()
runningtime_except_input_time=(end_pre-start_pre)+(end_dealing-start_dealing)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("runningtime_except_input_time is: ",runningtime_except_input_time,'s')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("runningtime_except_input_time is: ",runningtime_except_input_time/60.0,'min')
