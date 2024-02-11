class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_node(input_list):
        head = ListNode(input_list[0])
        current = head
        for x in input_list[1:]:
            new_node = ListNode(x)
            current.next = new_node
            current = new_node

        return head

def addTwoNumbers(l1,l2):
        res_l1 = []
        res_l2 = []
        current_node_l1 = l1
        current_node_l2 = l2
        while current_node_l1 is not None:
            res_l1.append(current_node_l1.val)
            current_node_l1 = current_node_l1.next
        while current_node_l2 is not None:
            res_l2.append(current_node_l2.val)
            current_node_l2 = current_node_l2.next

        out_l1 = 0
        out_l2 = 0
        for i in range(len(res_l1),0,-1):
            num_l1 = res_l1[i-1]*pow(10,i-1)
            out_l1 += num_l1

        for i in range(len(res_l2),0,-1):
            num_l2 = res_l2[i-1]*pow(10,i-1)
            out_l2 += num_l2

        sum = [int(x) for a,x in enumerate(str(out_l1+out_l2))]
        
        sum_rev = [sum[x-1] for x in range(len(sum),0,-1)]

        return sum_rev

        


l1 = [9,9,9,9]
l2 = [9,9,9,9,9,9,9]
node_l1 = list_to_node(l1)
node_l2 = list_to_node(l2)

print(addTwoNumbers(node_l1,node_l2))



