import itertools
def main():
    digits = "235"
    keyphone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    ans = []
    if (digits == ""):
        return ans
    permutations = list(itertools.product(*(keyphone[i] for i in digits)))
    for str in permutations:
        ans.append("".join(str))
    print(ans)
if __name__ == "__main__":
    main()