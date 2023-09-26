class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        counter = defaultdict(list)
        chars = set()
        last_at = {}

        for index, ch in enumerate(s): 
            counter[ch].append(index)
            chars.add(ch)
            last_at[ch] = index

        print(counter, chars)

        index = -1
        ans = []
        L = len(chars)
        done = set()
        remaining_chars = set(ch for ch in chars)


        def good(ch, at):
            if(ch not in chars or ch in done): return False

            while(len(counter[ch]) > 0 and counter[ch][0] < at): counter[ch].pop(0)
            
            if(not counter[ch]): return False
            
            found_at = counter[ch][0]
            return all(last_at[rem_char] > found_at for rem_char in remaining_chars if rem_char != ch)

        
        index = -1
        while(len(ans) < L):
            for ch in string.ascii_lowercase:
                if(ch not in chars or  ch in done): continue
                if(good(ch, index)):
                    index = counter[ch][0]
                    done.add(ch)
                    remaining_chars.remove(ch)
                    ans.append(ch)
                    break

        
        return "".join(ans)



