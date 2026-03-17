from parser import load_test
from search import climb_hill
from gui import show_table

def main():

    test_id = input("Test number: ").strip()

    start, goal, graph = load_test(test_id)

    path, steps = climb_hill(start, goal, graph)

    show_table(steps, path, goal)

    print("Path:", " -> ".join(path))

if __name__ == "__main__":
    main()