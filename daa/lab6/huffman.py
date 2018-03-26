class MinHeap:
    def __init__(self, in_list=[]):
        self.arr = None
        self.build_heap(in_list)

    @classmethod
    def parent_index(cls, index):
        return (index - 1) // 2 if index != 0 else None

    def left_index(self, index):
        return 2 * index + 1 if 2 * index + 1 <= self.last_index() else None

    def right_index(self, index):
        return 2 * index + 2 if 2 * index + 2 <= self.last_index() else None

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def heapify(self, index):
        li = self.left_index(index)
        ri = self.right_index(index)
        if li is None and ri is None:
            return
        if li is None or ri is None:
            mini = li if ri is None else ri
        else:
            mini = li if self.arr[li] < self.arr[ri] else ri
        if self.arr[mini] < self.arr[index]:
            self.swap(mini, index)
            self.heapify(mini)

    def insert(self, key):
        index = len(self.arr)
        self.arr.append(key)
        parent_index = self.parent_index(index)
        while parent_index is not None and self.arr[parent_index] > self.arr[index]:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = self.parent_index(index)

    def minimum(self):
        if len(self.arr) == 0:
            return None
        return self.arr[0]

    def extract_min(self):
        if len(self.arr) == 0:
            return None
        max_value = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.heapify(0)
        return max_value

    def last_index(self):
        return len(self.arr) - 1

    def build_heap(self, in_list):
        self.arr = in_list
        if self.last_index() <= 0:
            return
        for i in range(self.parent_index(self.last_index()), -1, -1):
            self.heapify(i)

class TreeNode:
    def __init__(self,f=0,s=None,l=None,r=None):
        self.left=l
        self.right=r
        self.symbol=s
        self.freq=f
    def __lt__(self,o):
        return self.freq<o.freq
    def __gt__(self,o):
        return self.freq>o.freq
    def printTree(self, s='',l=[]):
        if(self.symbol!=None):
            l[self.symbol]=s
        if(self.left):
            self.left.printTree(s+'0',l)
        if(self.right):
            self.right.printTree(s+'1',l)

def huffman(S,F):
    n=len(S)
    leaves=[]
    for i in range(n):
       leaves.append(TreeNode(F[i],i))
    H=MinHeap(leaves)
    while not len(H.arr)<2:
        m1=H.extract_min()
        m2=H.extract_min()
        p=TreeNode(m1.freq+m2.freq,None,m1,m2)
        H.insert(p)
    return H.extract_min()

def main():
    s=[i for i in input().split()]
    f=[int(i) for i in input().split()]
    n=len(s)
    t=huffman(s,f)
    print("\nSymbol Table is:")
    print("-----------------")
    l=[0 for i in range(n)]
    t.printTree('',l)
    for i in range(n):
        print(str(s[i])+":"+str(l[i]))
if __name__=='__main__':
    main()
