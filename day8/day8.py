with open('day8.txt') as f:
    input = f.readlines()[0].split(" ")
    input = [int(i) for i in input]

class node():
    def __init__(self, metadata, children):
        self.metadata = metadata
        self.children = children

    def __repr__(self):
        return "Node with {} children and metadata: {}".format(len(self.children), self.metadata)

def get_node(numbers, index):
    num_children = numbers[index]
    num_metadata = numbers[index + 1]
    if num_children == 0:
        metadata = numbers[index+2:index+2+num_metadata]
        return node(metadata, []), index + 2 + num_metadata
    else: 
        children = []
        next_index = index+2
        for i in range(num_children):
            child, width = get_node(numbers, next_index)
            next_index = width
            children.append(child)
        metadata = numbers[next_index:next_index+num_metadata]
        return node(metadata, children), next_index + num_metadata

node, _ = get_node(input, 0)

def sum_metadata(node):
    personal_metadata = sum(node.metadata)
    if len(node.children) == 0:
        return personal_metadata
    else:
        return personal_metadata + sum([sum_metadata(child) for child in node.children])

def node_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        relevant_children = []
        for i in node.metadata:
            if (i-1) < len(node.children):
                relevant_children.append(node.children[i-1])
        return sum([node_value(child) for child in relevant_children])

print("Part 1: ", sum_metadata(node))
print("Part 2: ", node_value(node))