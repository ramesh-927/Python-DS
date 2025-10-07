class Solution:
    def greedy_activity(start, finish):

        # Step 1: Combine start and finish times into a list of tuples and sort by finish time
        activites = list(zip(start, finish)) 
        activites.sort(key=lambda x: x[1])

        selected = [activites[0]]     # Step 2: Initialize result with the first activity
        last_finish = activites[0][1]

        for numbers in activites[1:]:      # Step 3: Iterate through remaining activities
            start_time, finish_time = numbers

            if start_time >= last_finish:
                selected.append(numbers)
                last_finish = finish_time
        return selected

Solution()
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
result = Solution.greedy_activity(start, finish)
print("Selected activities:", result)


