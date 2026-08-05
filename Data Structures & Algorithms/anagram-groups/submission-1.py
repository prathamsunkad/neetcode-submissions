class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dic = {}
        for word in strs:
            temp_dic = {}
            for char in word:
                temp_dic[char] = temp_dic.setdefault(char,0) + 1
            key_tuple = tuple(sorted(temp_dic.items()))

            main_dic.setdefault(key_tuple, []).append(word)

        final_list = []
        for keys,values in main_dic.items():
            final_list.append(values)

        return final_list