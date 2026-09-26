class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic = {}
        for i in range(len(knowledge)):
            word = knowledge[i]
            dic[word[0]] = word[1]
        brackets = []
        for i in range(len(s)):
            if s[i] in ["(", ")"]:
                brackets.append(i)
        for i in range(len(brackets)-2, -1, -2):
            start = brackets[i]
            end = brackets[i+1]
            key = s[start+1:end]
            if key in dic:
                value = dic[key]
            else:
                value = "?"
            s = s[:start] + value + s[end+1:]
        return s