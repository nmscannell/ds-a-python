class MinHeap:
    def __init__(self):
        self.heap_list = []

    def __str__(self):
        return str(self.heap_list)

    def display(self):
        pass
    
    def insert(self, element):
        self.heap_list.append(element)
        self.bubble_up(len(self.heap_list) - 1)

    def bubble_up(self, curr_index):
        parent_index = (curr_index - 1) // 2
        while parent_index >= 0:
            curr_element = self.heap_list[curr_index]
            parent = self.heap_list[parent_index]
            if curr_element < parent:
                self.heap_list[parent_index] = curr_element
                self.heap_list[curr_index] = parent
                curr_index = parent_index
                parent_index = (curr_index - 1) // 2
            else:
                break
    
    def min(self):
        return self.heap_list[0]

    def remove(self):
        element = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        del self.heap_list[-1]
        self.bubble_down(0)
        return element

    def bubble_down(self, curr_index):
        left_index = (curr_index * 2) + 1
        right_index = (curr_index * 2) + 2
        while left_index < len(self.heap_list):
            curr_element = self.heap_list[curr_index]
            left_element = self.heap_list[left_index]
            if right_index < len(self.heap_list):
                right_element = self.heap_list[right_index]
            else:
                right_element = float('inf')
            if curr_element > left_element or curr_element > right_element:
                swap = min(left_element, right_element)
                if swap == left_element:
                    self.heap_list[left_index] = curr_element
                    self.heap_list[curr_index] = left_element
                    curr_index = left_index
                else:
                    self.heap_list[right_index] = curr_element
                    self.heap_list[curr_index] = right_element
                    curr_index = right_index
            else:
                break
            left_index = (curr_index * 2) + 1
            right_index = (curr_index * 2) + 2
