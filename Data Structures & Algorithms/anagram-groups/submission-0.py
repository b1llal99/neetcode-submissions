class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}
        # groups = {(('a', 1), ('c', 1), ('t', 1)): ["act", "cat"]}

        for s in strs:
            letter_count = {}
            for i in s:
                letter_count[i] = 1 + letter_count.get(i, 0)

            key = tuple(sorted(letter_count.items())) # a:1,c:1,t:1 -> ((a,1), (c,1), (t,1))

            if key not in group:
                group[key] = []
            group[key].append(s)

        return list(group.values())
        





            