from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Build graph
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # Invalid case: ["abc", "ab"]
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

    # Step 2: Topological sort using Kahn's Algorithm
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Cycle detection
    if len(order) != len(in_degree):
        return ""

    return ''.join(order)

if __name__ == "__main__":
    print("Enter comma-separated sorted words from the alien language:")
    user_input = input().strip()
    words = [word.strip() for word in user_input.split(',') if word.strip()]

    if not words:
        print("No valid input provided.")
    else:
        result = alien_order(words)
        if result:
            print("Character order in the alien language:", result)
        else:
            print("Invalid word order or cycle detected.")



def run_tests():
    tests = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["z", "x", "z"], ""),  # Cycle
        (["abc", "ab"], ""),   # Invalid prefix
        (["a", "b", "ca", "cc"], "abc"),
        (["a"], "a"),
    ]
    
    for i, (words, expected) in enumerate(tests):
        output = alien_order(words)
        print(f"Test Case {i+1}: {'Pass' if output == expected else f'Fail (Expected: {expected}, Got: {output})'}")

# To run the tests:
# run_tests()

