def load_test(test_id):
    fileName = f'test/test{test_id}.txt'

    with open(fileName, 'r') as f:
        # strip() removes the newline character at the end of each line
        lines = [line.strip() for line in f.readlines()]
    
    start = lines[0]
    end = lines[1]
    graph = {}
    for line in lines[3:]:
        parts = line.split()
        node = parts[0]
        h = int(parts[1])
        neighbors = parts[2:]
        graph[node] = (h, neighbors)

    return start, end, graph