class Solutions:
    def letter_case_permutation(self, s):
        result = []
        def backtrack(index, path):
            if index == len(s):
                result.append("".join(path))
                return
            if s[index].isalpha():
                path.append(s[index].lower())
                backtrack(index + 1, path)
                path.pop()

                s[index].isalpha()
                path.append(s[index].upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(s[index])
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result

sol = Solutions()
res = sol.letter_case_permutation("a1b2")    
print(res)