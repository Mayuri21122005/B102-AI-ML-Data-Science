
# QUESTION 1: Second-largest unique element
#==============================================================================
#def second_largest(arr):
#     largest = second = None
#    for num in arr:
#         if largest is None or num > largest:
#             if num != largest:
#                second = largest
#            largest = num
#         elif num != largest and (second is None or num > second):
#             second = num
#     return second
#print(second_largest([10, 5, 8, 10, 3])) 

#==============================================================================
# QUESTION 2: All pairs whose sum equals target
#==============================================================================
#def pairs_with_sum(arr, target):
#    seen = set()
#     pairs = set()
#     for num in arr:
#         needed = target - num
#         if needed in seen:
#            pairs.add(tuple(sorted((num, needed))))
#         seen.add(num)
#     return sorted(pairs)

#print(pairs_with_sum([2, 4, 3, 5, 7, 8], 10))  

#==============================================================================
# QUESTION 3: Move zeros to the end
#==============================================================================
#def move_zeros(arr):
#     non_zero = [num for num in arr if num != 0]
#     return non_zero + [0] * (len(arr) - len(non_zero))

#print(move_zeros([0, 1, 0, 3, 12])) 

#==============================================================================
# QUESTION 4: Find the missing number from 1 to N
#==============================================================================
# def missing_number(arr, n):
#     expected_sum = n * (n + 1) // 2
#     return expected_sum - sum(arr)
# print(missing_number([1, 2, 4, 5], 5))  

#==============================================================================
# QUESTION 5: Find duplicate elements without nested loops
#==============================================================================
# from collections import Counter
# def find_duplicates(arr):
#     counts = Counter(arr)
#     return [num for num, count in counts.items() if count > 1]
# print(find_duplicates([1, 2, 3, 2, 4, 1]))  

#==============================================================================
# QUESTION 6: First non-repeating character
#==============================================================================
# from collections import Counter
# def first_non_repeating(s):
#     counts = Counter(s)
#     for char in s:
#         if counts[char] == 1:
#             return char
#     return None
# print(first_non_repeating("swiss")) 

#==============================================================================
# QUESTION 7: Check anagrams without sorted()
#==============================================================================
# from collections import Counter
# def are_anagrams(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     counts = Counter(s1)
#     for char in s2:
#         if char not in counts:
#             return False
#         counts[char] -= 1
#         if counts[char] < 0:
#             return False
#     return all(value == 0 for value in counts.values())
# print(are_anagrams("listen", "silent"))  

#==============================================================================
# QUESTION 8: Merge two sorted arrays without sort()
#==============================================================================
# def merge_sorted_arrays(a, b):
#     i = j = 0
#     result = []
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     result.extend(a[i:])
#     result.extend(b[j:])
#     return result
# print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  

#==============================================================================
# QUESTION 9: Rotate array right by K positions
#==============================================================================
# def rotate_right(arr, k):
#     if not arr:
#         return []
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k] if k else arr[:]
# print(rotate_right([1, 2, 3, 4, 5], 2))  

#==============================================================================
# QUESTION 10: Intersection including duplicate occurrences
#==============================================================================
# from collections import Counter
# def intersection_with_duplicates(a, b):
#     counts = Counter(a)
#     result = []
#     for num in b:
#         if counts[num] > 0:
#             result.append(num)
#             counts[num] -= 1
#     return result
# print(intersection_with_duplicates([1, 2, 2, 3], [2, 2, 4]))  

#==============================================================================
# QUESTION 11: Maximum sum of contiguous subarray
#==============================================================================
# def max_subarray_sum(arr):
#     if not arr:
#         return None
#     current = best = arr[0]
#     for num in arr[1:]:
#         current = max(num, current + num)
#         best = max(best, current)
#     return best
# print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 

#==============================================================================
# QUESTION 12: Longest substring without repeating characters
#==============================================================================
# def longest_unique_substring_length(s):
#     last_seen = {}
#     left = best = 0
#     for right, char in enumerate(s):
#         if char in last_seen and last_seen[char] >= left:
#             left = last_seen[char] + 1
#         last_seen[char] = right
#         best = max(best, right - left + 1)
#     return best
# print(longest_unique_substring_length("abcabcbb")) 

#==============================================================================
# QUESTION 13: Longest common prefix
#==============================================================================
# def longest_common_prefix(strings):
#     if not strings:
#         return ""
#     prefix = strings[0]
#     for word in strings[1:]:
#         while not word.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix
# print(longest_common_prefix(["flower", "flow", "flight"]))  

#==============================================================================
# QUESTION 14: Group strings into anagram groups
#==============================================================================
# from collections import defaultdict
# def group_anagrams(words):
#     groups = defaultdict(list)
#     for word in words:
#         key = tuple(sorted(word))
#         groups[key].append(word)
#     return list(groups.values())
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#==============================================================================
# QUESTION 15: Kth largest element in an unsorted array
#==============================================================================
# import heapq
# def kth_largest(arr, k):
#     if k < 1 or k > len(arr):
#         raise ValueError("k must be between 1 and the array length")
#     return heapq.nlargest(k, arr)[-1]
# print(kth_largest([3, 2, 1, 5, 6, 4], 2))  

#==============================================================================
# QUESTION 16: Balanced parentheses using a stack
#==============================================================================
# def balanced_parentheses(s):
#     stack = []
#     matching = {')': '(', ']': '[', '}': '{'}
#     for char in s:
#         if char in "([{":
#             stack.append(char)
#         elif char in matching:
#             if not stack or stack.pop() != matching[char]:
#                 return False
#     return len(stack) == 0
# print(balanced_parentheses("{[()]}")) 

#==============================================================================
# QUESTION 17: All subarrays whose sum equals target
#==============================================================================
# from collections import defaultdict
# def subarrays_with_target_sum(arr, target):
#     prefix_positions = defaultdict(list)
#     prefix_positions[0].append(-1)
#     prefix_sum = 0
#     result = []
#     for i, num in enumerate(arr):
#         prefix_sum += num
#         needed = prefix_sum - target
#         for start_index in prefix_positions[needed]:
#             result.append(arr[start_index + 1:i + 1])
#         prefix_positions[prefix_sum].append(i)
#     return result

# print(subarrays_with_target_sum([1, 2, 3, 2], 5)) 

#==============================================================================
# QUESTION 18: Merge overlapping intervals
#==============================================================================
# def merge_intervals(intervals):
#     if not intervals:
#         return []
#     intervals = sorted(intervals, key=lambda item: item[0])
#     merged = [list(intervals[0])]
#     for start, end in intervals[1:]:
#         if start <= merged[-1][1]:
#             merged[-1][1] = max(merged[-1][1], end)
#         else:
#             merged.append([start, end])
#     return merged
# print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])) 

#==============================================================================
# QUESTION 19: Search in a rotated sorted array
#==============================================================================
# def search_rotated(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         if arr[left] <= arr[mid]:
#             if arr[left] <= target < arr[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if arr[mid] < target <= arr[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return -1
# print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0)) 

#==============================================================================
# QUESTION 20: Longest consecutive sequence
#==============================================================================
# def longest_consecutive(arr):
#     values = set(arr)
#     best = 0
#     for num in values:
#         if num - 1 not in values:
#             length = 1
#             while num + length in values:
#                 length += 1
#             best = max(best, length)
#     return best
# print(longest_consecutive([100, 4, 200, 1, 3, 2]))  

#==============================================================================
# QUESTION 21: Trapped rainwater
#==============================================================================
# def trapped_rainwater(height):
#     left, right = 0, len(height) - 1
#     left_max = right_max = water = 0
#     while left < right:
#         if height[left] <= height[right]:
#             left_max = max(left_max, height[left])
#             water += left_max - height[left]
#             left += 1
#         else:
#             right_max = max(right_max, height[right])
#             water += right_max - height[right]
#             right -= 1
#     return water
# print(trapped_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) 

#==============================================================================
# QUESTION 22: Median of two sorted arrays in logarithmic time
#==============================================================================
# def median_two_sorted_arrays(a, b):
#     if len(a) > len(b):
#         a, b = b, a
#     m, n = len(a), len(b)
#     if n == 0:
#         raise ValueError("Both arrays cannot be empty")
#
#     low, high = 0, m
#     half = (m + n + 1) // 2
#
#     while low <= high:
#         i = (low + high) // 2
#         j = half - i
#
#         a_left = float("-inf") if i == 0 else a[i - 1]
#         a_right = float("inf") if i == m else a[i]
#         b_left = float("-inf") if j == 0 else b[j - 1]
#         b_right = float("inf") if j == n else b[j]
#
#         if a_left <= b_right and b_left <= a_right:
#             if (m + n) % 2:
#                 return max(a_left, b_left)
#             return (max(a_left, b_left) + min(a_right, b_right)) / 2
#         elif a_left > b_right:
#             high = i - 1
#         else:
#             low = i + 1
#
#     raise ValueError("Input arrays must be sorted")
# print(median_two_sorted_arrays([1, 3], [2]))  

#==============================================================================
# QUESTION 23: Maximum product of contiguous subarray
#==============================================================================
# def max_product_subarray(arr):
#     if not arr:
#         return None
#     max_here = min_here = answer = arr[0]
#     for num in arr[1:]:
#         if num < 0:
#             max_here, min_here = min_here, max_here
#         max_here = max(num, max_here * num)
#         min_here = min(num, min_here * num)
#         answer = max(answer, max_here)
#     return answer
# print(max_product_subarray([2, 3, -2, 4])) 

#==============================================================================
# QUESTION 24: Smallest missing positive integer
#==============================================================================
# def first_missing_positive(arr):
#     values = set(arr)
#     candidate = 1
#     while candidate in values:
#         candidate += 1
#     return candidate
# print(first_missing_positive([3, 4, -1, 1])) 

#==============================================================================
# QUESTION 25: Count subarrays whose sum equals K
#==============================================================================
# def count_subarrays_sum_k(arr, k):
#     counts = {0: 1}
#     prefix_sum = answer = 0
#     for num in arr:
#         prefix_sum += num
#         answer += counts.get(prefix_sum - k, 0)
#         counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
#     return answer
# print(count_subarrays_sum_k([1, 1, 1], 2))  

#==============================================================================
# QUESTION 26: Longest increasing subsequence
#==============================================================================
# def lis_length(arr):
#     tails = []
#     for num in arr:
#         left, right = 0, len(tails)
#         while left < right:
#             mid = (left + right) // 2
#             if tails[mid] < num:
#                 left = mid + 1
#             else:
#                 right = mid
#         if left == len(tails):
#             tails.append(num)
#         else:
#             tails[left] = num
#     return len(tails)
# print(lis_length([10, 9, 2, 5, 3, 7, 101, 18])) 

#==============================================================================
# QUESTION 27: Coin Change using dynamic programming
#==============================================================================
# def coin_change(coins, amount):
#     dp = [float("inf")] * (amount + 1)
#     dp[0] = 0
#     for value in range(1, amount + 1):
#         for coin in coins:
#             if coin <= value:
#                 dp[value] = min(dp[value], dp[value - coin] + 1)
#     return -1 if dp[amount] == float("inf") else dp[amount]
# print(coin_change([1, 2, 5], 11)) 

#==============================================================================
# QUESTION 28: Word Break using dynamic programming
#==============================================================================
# def word_break(s, word_dict):
#     words = set(word_dict)
#     dp = [False] * (len(s) + 1)
#     dp[0] = True
#     for end in range(1, len(s) + 1):
#         for start in range(end):
#             if dp[start] and s[start:end] in words:
#                 dp[end] = True
#                 break
#     return dp[len(s)]
# print(word_break("leetcode", ["leet", "code"]))  

#==============================================================================
# QUESTION 29: Minimum jumps to reach the last index
#==============================================================================
# def minimum_jumps(arr):
#     n = len(arr)
#     if n <= 1:
#         return 0
#     if arr[0] == 0:
#         return -1
#
#     jumps = current_end = farthest = 0
#     for i in range(n - 1):
#         farthest = max(farthest, i + arr[i])
#         if i == current_end:
#             jumps += 1
#             current_end = farthest
#             if current_end >= n - 1:
#                 return jumps
#             if current_end == i:
#                 return -1
#     return -1
# print(minimum_jumps([2, 3, 1, 1, 4])) 

#==============================================================================
# QUESTION 30: Maximum stock profit with multiple transactions
#==============================================================================
# def max_stock_profit(prices):
#     profit = 0
#     for i in range(1, len(prices)):
#         if prices[i] > prices[i - 1]:
#             profit += prices[i] - prices[i - 1]
#     return profit
# print(max_stock_profit([7, 1, 5, 3, 6, 4])) 

#==============================================================================
# QUESTION 31: LRU Cache with O(1) get() and put()
#==============================================================================
# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache[key] = self.cache.pop(key)
#         return self.cache[key]
#
#     def put(self, key, value):
#         if self.capacity <= 0:
#             return
#         if key in self.cache:
#             self.cache.pop(key)
#         elif len(self.cache) >= self.capacity:
#             oldest_key = next(iter(self.cache))
#             del self.cache[oldest_key]
#         self.cache[key] = value
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1)) 
# cache.put(3, 3)
# print(cache.get(2)) 

#==============================================================================
# QUESTION 32: Min Stack with O(1) operations
#==============================================================================
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#         if not self.min_stack or value <= self.min_stack[-1]:
#             self.min_stack.append(value)
#
#     def pop(self):
#         if not self.stack:
#             return None
#         value = self.stack.pop()
#         if value == self.min_stack[-1]:
#             self.min_stack.pop()
#         return value
#
#     def top(self):
#         return self.stack[-1] if self.stack else None
#
#     def getMin(self):
#         return self.min_stack[-1] if self.min_stack else None
# stack = MinStack()
# stack.push(5)
# stack.push(2)
# stack.push(8)
# print(stack.getMin()) 
# stack.pop()
# print(stack.top())    

#==============================================================================
# QUESTION 33: Number of islands using DFS
#==============================================================================
# def number_of_islands(grid):
#     if not grid:
#         return 0
#     rows, cols = len(grid), len(grid[0])
#     visited = set()
#
#     def dfs(r, c):
#         if (r < 0 or r >= rows or c < 0 or c >= cols
#                 or grid[r][c] != "1" or (r, c) in visited):
#             return
#         visited.add((r, c))
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)
#
#     islands = 0
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == "1" and (r, c) not in visited:
#                 dfs(r, c)
#                 islands += 1
#     return islands
# grid = [["1", "1", "0", "0"],
#         ["1", "0", "0", "1"],
#         ["0", "0", "1", "1"]]
# print(number_of_islands(grid))

#==============================================================================
# QUESTION 34: Dijkstra shortest path in a weighted graph
#==============================================================================
# import heapq
# def dijkstra(graph, start):
#     distances = {node: float("inf") for node in graph}
#     distances[start] = 0
#     heap = [(0, start)]
#
#     while heap:
#         distance, node = heapq.heappop(heap)
#         if distance != distances[node]:
#             continue
#         for neighbor, weight in graph.get(node, []):
#             new_distance = distance + weight
#             if new_distance < distances.get(neighbor, float("inf")):
#                 distances[neighbor] = new_distance
#                 heapq.heappush(heap, (new_distance, neighbor))
#     return distances
# graph = {"A": [("B", 4), ("C", 1)],
#          "B": [("D", 1)],
#          "C": [("B", 2), ("D", 5)],
#          "D": []}
# print(dijkstra(graph, "A")) 

#==============================================================================
# QUESTION 35: Detect cycles in directed and undirected graphs
#==============================================================================
# def has_cycle_directed(graph):
#     state = {}  
#
#     def dfs(node):
#         state[node] = 1
#         for neighbor in graph.get(node, []):
#             if state.get(neighbor, 0) == 1:
#                 return True
#             if state.get(neighbor, 0) == 0 and dfs(neighbor):
#                 return True
#         state[node] = 2
#         return False
#
#     nodes = set(graph)
#     for neighbors in graph.values():
#         nodes.update(neighbors)
#     for node in nodes:
#         if state.get(node, 0) == 0 and dfs(node):
#             return True
#     return False
#
# def has_cycle_undirected(graph):
#     visited = set()
#
#     def dfs(node, parent):
#         visited.add(node)
#         for neighbor in graph.get(node, []):
#             if neighbor not in visited:
#                 if dfs(neighbor, node):
#                     return True
#             elif neighbor != parent:
#                 return True
#         return False
#
#     nodes = set(graph)
#     for neighbors in graph.values():
#         nodes.update(neighbors)
#     for node in nodes:
#         if node not in visited and dfs(node, None):
#             return True
#     return False
# directed = {1: [2], 2: [3], 3: [1]}
# print(has_cycle_directed(directed))  
# 
# undirected = {1: [2], 2: [1, 3], 3: [2]}
# print(has_cycle_undirected(undirected)) 

#==============================================================================
# QUESTION 36: Topological sorting of a DAG
#==============================================================================
# from collections import deque
# def topological_sort(graph):
#     nodes = set(graph)
#     for neighbors in graph.values():
#         nodes.update(neighbors)
#
#     indegree = {node: 0 for node in nodes}
#     for node in graph:
#         for neighbor in graph[node]:
#             indegree[neighbor] += 1
#
#     queue = deque([node for node in nodes if indegree[node] == 0])
#     order = []
#     while queue:
#         node = queue.popleft()
#         order.append(node)
#         for neighbor in graph.get(node, []):
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     if len(order) != len(nodes):
#         raise ValueError("Graph contains a cycle; topological order does not exist")
#     return order
# graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
# print(topological_sort(graph)) 

#==============================================================================
# QUESTION 37: N-Queens using backtracking
#==============================================================================
# def solve_n_queens(n):
#     results = []
#     board = [["."] * n for _ in range(n)]
#     columns = set()
#     diagonal1 = set()  # row - column
#     diagonal2 = set()  # row + column
#
#     def backtrack(row):
#         if row == n:
#             results.append(["".join(line) for line in board])
#             return
#         for col in range(n):
#             if (col in columns or row - col in diagonal1
#                     or row + col in diagonal2):
#                 continue
#             board[row][col] = "Q"
#             columns.add(col)
#             diagonal1.add(row - col)
#             diagonal2.add(row + col)
#
#             backtrack(row + 1)
#
#             board[row][col] = "."
#             columns.remove(col)
#             diagonal1.remove(row - col)
#             diagonal2.remove(row + col)
#
#     backtrack(0)
#     return results
# solutions = solve_n_queens(4)
# for board in solutions:
#     for row in board:
#         print(row)
#     print() 

#==============================================================================
# QUESTION 38: Unique permutations without duplicates
#==============================================================================
# def unique_permutations(items):
#     items = list(items)
#     items.sort()
#     result = []
#     used = [False] * len(items)
#     current = []
#
#     def backtrack():
#         if len(current) == len(items):
#             result.append(current[:])
#             return
#         for i in range(len(items)):
#             if used[i]:
#                 continue
#             if i > 0 and items[i] == items[i - 1] and not used[i - 1]:
#                 continue
#             used[i] = True
#             current.append(items[i])
#             backtrack()
#             current.pop()
#             used[i] = False
#
#     backtrack()
#     return result
# print(unique_permutations("AAB")) 

#==============================================================================
# QUESTION 39: Serialize and deserialize a binary tree
#==============================================================================
# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None
#
# class Codec:
#     def serialize(self, root):
#         values = []
#
#         def preorder(node):
#             if node is None:
#                 values.append("#")
#                 return
#             values.append(str(node.val))
#             preorder(node.left)
#             preorder(node.right)
#
#         preorder(root)
#         return ",".join(values)
#
#     def deserialize(self, data):
#         values = iter(data.split(","))
#
#         def build():
#             value = next(values)
#             if value == "#":
#                 return None
#             node = TreeNode(int(value))
#             node.left = build()
#             node.right = build()
#             return node
#
#         return build()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# codec = Codec()
# data = codec.serialize(root)
# print(data)  
# new_root = codec.deserialize(data)
# print(new_root.val)  

#==============================================================================
# QUESTION 40: Lowest common ancestor in a binary tree
  

# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None
#
# def lowest_common_ancestor(root, p, q):
#     if root is None or root is p or root is q:
#         return root
#     left = lowest_common_ancestor(root.left, p, q)
#     right = lowest_common_ancestor(root.right, p, q)
#     if left is not None and right is not None:
#         return root
#     return left if left is not None else right

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# p = root.left.left
# q = root.right
# answer = lowest_common_ancestor(root, p, q)
# print(answer.val)
