################################
## ITERATIVE TOWER OF HANOI
## Name: Eitan Yehuda
## Date: Mar.31,2017
################################

## Class and Methods ##

class Stack:
    def __init__(self,name):
        self.items = []
        self.name = name            ## Added name for each tower stack

    def isEmpty(self):
        return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def index(self,index):              ##
        return self.items[index]        ## New index method for tower stacks

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

## Functions ##

def legalMove(t1,t2,disk_num,tA,tB,tC):
    if t1.isEmpty() == False and (t2.isEmpty() or t1.peek() < t2.peek()):           ##
        t2.push(t1.pop())                                                           ## Legal move between 2 poles
    elif t2.isEmpty() == False and (t1.isEmpty() or t2.peek() < t1.peek()):         ##
        t1.push(t2.pop())                                                           ##

    draw(tA,tB,tC,disk_num,t1,t2)       ## Call draw function


def draw(tA,tB,tC,disk_num,t1,t2):
    print('\n\n< Move',draw.moves,'>')      ## Print move number
    draw.moves+=1                           ## and add 1 to moves variable

## Pic 1 ##
##    print('Tower A: ', tA)        ##
##    print('Tower B: ', tB)        ## Simple printing of towers (pic 1)
##    print('Tower C: ', tC)        ##
##    print('----------')           ##


## Pic 2 ##
    for i in range(disk_num,0,-1):

        print(drawFancy(tA,i),end='')           ##
        print(drawFancy(tB,i),end='')           ## Call fancy print function for each line and check each tower (pic 2)
        print(drawFancy(tC,i))                  ##

    print('#'*45)                                                   ##
    print('Moved a disk from', t1.name, 'pole to', t2.name, 'pole') ## Display what move was made


def drawFancy(tower,index):
    if index-1 < tower.size():                      ##
        disk = str('='*(2*tower.index(index-1)+1))  ## Fancy printing of poles by line called from draw function
        return disk.center(disk_num*2+2)            ## check if index is in range to print current disk
    else:                                           ## otherwise prind empty pole section
        return '|'.center(disk_num*2+2)             ##

## Variables ##

disk_num = int(input('How many disks do you want to use? '))
towerA = Stack('First')
towerB = Stack('Second')
towerC = Stack('Third')
draw.moves = 1

## Main ##

for i in range(disk_num,0,-1):      ##
    towerA.push(i)                  ## generates first pole with requested number of disks

while towerC.size() != disk_num:

    if disk_num%2==0:                                                   ##
                                                                        ## Calls legal move function between 2 poles
        legalMove(towerA,towerB,disk_num,towerA,towerB,towerC)          ## According to even number of disks solving algorithm
        legalMove(towerA,towerC,disk_num,towerA,towerB,towerC)          ## for tower of Hanoi
        legalMove(towerB,towerC,disk_num,towerA,towerB,towerC)          ##

    elif disk_num%2!=0:                                                 ##
                                                                        ##
        legalMove(towerA,towerC,disk_num,towerA,towerB,towerC)          ## Same but for odd number of disks instead
        if towerC.size() == disk_num:                               ## checks to see if puzzle is complete and breaks loop. This happens here sometimes depending on number of disks
            break

        legalMove(towerA,towerB,disk_num,towerA,towerB,towerC)
        legalMove(towerC,towerB,disk_num,towerA,towerB,towerC)


