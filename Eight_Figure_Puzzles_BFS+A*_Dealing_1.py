import numpy
import copy
import time

#This is the first idea about A*
#In A*, F = G + H
# F means the total cost
# G means the price we have paid to achieve this situation
# H means the estimated left cost we will need to pay, it is not exact
start_pre = time.time()
total_steps = 0

have_been_exist_or_not = numpy.zeros((9, 9, 9, 9, 9, 9, 9, 9, 9))

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


def set_get_have_been_exist_or_not_value___judge_end(data):
    global total_steps
    total_steps += 1

    if (data - result).any() == False:
        return -1

    index = []
    for i in range(3):
        for j in range(3):
            index.append(data[i + 1][j + 1] - 1)

    if have_been_exist_or_not[int(index[0])][int(index[1])][int(index[2])][int(
                                  index[3])][int(index[4])][int(index[5])][int(
                                  index[6])][int(index[7])][int(index[8])] == 1:
        return 0

    else:
        have_been_exist_or_not[int(index[0])][int(index[1])][int(index[2])][int(
                                   index[3])][int(index[4])][int(index[5])][int(
                                   index[6])][int(index[7])][int(index[8])] = 1
        return 1


#This fun is used to count the H
#It count in this situation how many blocks are different from result
def count_left_estimated_cost(data):
    different_blocks = 0
    for i in range(3):
        for j in range(3):
            if data[i + 1][j + 1] != result[i + 1][j + 1]:
                different_blocks += 1
    return different_blocks


class node:
    price_paid = 0
    total_estimated_cost = 0
    parent = None
    children = []
    data = []
    access = 1

    def __init__(self):
        self.parent = None

    def add_data(self, data):
        self.data = data

    def change_data(self, data):
        self.data = data

    def add_parent(self, parent):
        #The price_paid means the G
        #It means to achieve this situation the num of nodes we have traveled
        self.parent = parent
        self.price_paid = parent.get_price_paid() + 1

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_price_paid(self):
        return self.price_paid

    #To count the F of this situation
    #At the same time it can return the F
    def get_total_estimated_cost(self):
        self.total_estimated_cost = self.price_paid + count_left_estimated_cost(
            self.data)
        return self.total_estimated_cost

    def add_child(self, kid):
        self.children.append(kid)

    #When this node is not access, we make its access value to be '0'
    # When we inflate a node, its access value is '1'
    def set_not_access(self):
        self.access = 0

    def get_access_value(self):
        return self.access

    #Choose the first child who is accessable
    #If there are no children satisfied, return None
    def get_child(self):
        num_of_children = len(self.children)
        for i in range(num_of_children):
            if self.children[i].get_access_value() == 1:
                return self.children[i]
        return None


open_list = []
close_list = []

end_pre = time.time()

print("input you init nums")

for i in range(3):
    for j in range(3):
        position_tip = i * 3 + j + 1
        init_num[i + 1][j + 1] = int(
            input("input " + str(position_tip) + " num" + "\n"))

start_dealing = time.time()

init_node = node()
init_node.add_data(init_num)
set_get_have_been_exist_or_not_value___judge_end(init_num)
open_list.append(init_node)

result_node = node()
result_node.add_data(result)
set_get_have_been_exist_or_not_value___judge_end(result)
close_list.append(result_node)

while True:

    father = open_list[0].get_data()

    i_9 = 0
    j_9 = 0

    for i in range(3):
        for j in range(3):
            if father[i + 1][j + 1] == 9:
                i_9 = i + 1
                j_9 = j + 1
                break

    #The cost_collector is used to collect the F of every kid
    #When q=0, it means node_up
    #When q=1, it means node_down
    #......
    cost_collector = numpy.zeros((4))
    for q in range(4):
        cost_collector[q] = -10
    node_up = node()
    node_down = node()
    node_left = node()
    node_right = node()

    if father[i_9 - 1][j_9]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9 - 1][j_9]
        kid[i_9 - 1][j_9] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        #If this kid exists, make its cost_collector value to be '-1'
        if flag == 0:
            cost_collector[0] = -1

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        #The open_list[0] is the father node
        #When this node is new, not exist yet, we build a two-way relationship between it and its parent
        if flag == 1:
            node_up.add_data(kid)
            node_up.add_parent(open_list[0])
            open_list[0].add_child(node_up)
            cost_collector[0] = node_up.get_total_estimated_cost()

    if father[i_9 + 1][j_9]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9 + 1][j_9]
        kid[i_9 + 1][j_9] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == 0:
            cost_collector[1] = -1

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:
            node_down.add_data(kid)
            node_down.add_parent(open_list[0])
            open_list[0].add_child(node_down)
            cost_collector[1] = node_down.get_total_estimated_cost()

    if father[i_9][j_9 - 1]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9][j_9 - 1]
        kid[i_9][j_9 - 1] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == 0:
            cost_collector[2] = -1

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:
            node_left.add_data(kid)
            node_left.add_parent(open_list[0])
            open_list[0].add_child(node_left)
            cost_collector[2] = node_left.get_total_estimated_cost()

    if father[i_9][j_9 + 1]:

        kid = copy.deepcopy(father)
        kid[i_9][j_9] = father[i_9][j_9 + 1]
        kid[i_9][j_9 + 1] = father[i_9][j_9]

        flag = set_get_have_been_exist_or_not_value___judge_end(kid)

        if flag == 0:
            cost_collector[3] = -1

        if flag == -1:
            close_list[0].add_parent(open_list[0])
            print("```````````````````````````````````````````")
            print("Break now!")
            break

        if flag == 1:
            node_right.add_data(kid)
            node_right.add_parent(open_list[0])
            open_list[0].add_child(node_right)
            cost_collector[3] = node_right.get_total_estimated_cost()

    #To find the max in a unknown array, we need to determine the min in it
    #So as the same to find the min in a unknown array
    max_cost = -2
    max_cost_index = 0
    for q in range(4):
        if cost_collector[q] > max_cost:
            max_cost = cost_collector[q]
            max_cost_index = q

    find_successor_flag = 0
    min_cost_index = max_cost_index
    min_cost = max_cost

    for q in range(4):

        if cost_collector[q] > 0 and min_cost >= cost_collector[q]:
            min_cost_index = q
            find_successor_flag = 1

    #If in this father node, we could not to find the kid to success, it means this node is not accessable
    #At this moment the find_successor should be '0'
    if find_successor_flag == 0:
        #Make this father node not accessable anymore
        open_list[0].set_not_access()
        while True:
            #Make grandpa to be to the father(open_list[0]) again, to choose which son is suitable
            open_list[0] = open_list[0].get_parent()
            another_successor = open_list[0].get_child()
            #If grandpa could not find the suitable son, give the task to father of grandpa
            #If found the suitable son, it can stop finding
            if another_successor != None:
                break
        #If not enter the cycle, father is replaced by its brother
        open_list[0] = another_successor
        #Noticed! This continue is necessary!
        continue

    if min_cost_index == 0:
        open_list.append(node_up)
    if min_cost_index == 1:
        open_list.append(node_down)
    if min_cost_index == 2:
        open_list.append(node_left)
    if min_cost_index == 3:
        open_list.append(node_right)

    close_list.append(open_list[0])
    del (open_list[0])

print(total_steps)
print("***********************************************************")

finder = close_list[0]

final_list = []
while finder != None:
    final_list.append(finder.get_data())
    finder = finder.get_parent()

length_final_list = len(final_list)

final_list.reverse()

print("The final_list length is", length_final_list)

for i in range(length_final_list):
    print(final_list[i])
    print("*********************************")

end_dealing = time.time()
runningtime_except_input_time = (end_pre - start_pre) + (end_dealing -
                                                         start_dealing)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("runningtime_except_input_time is: ", runningtime_except_input_time, 's')
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("runningtime_except_input_time is: ",
      runningtime_except_input_time / 60.0, 'min')
