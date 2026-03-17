from pathlib import Path


def load_test(test_id):
    normalized_test_id = str(test_id).strip()
    file_name = f"test{normalized_test_id}.txt"
    file_path = Path(__file__).resolve().parent.parent / "test" / file_name

    with open(file_path, 'r', encoding='utf-8') as f:
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