class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # 1. Impossible case
        if len(s1) > len(s2):
            return False

        # 2. Store character frequencies
        need = {}
        window = {}

        # 3. Build the frequencies we NEED from s1
        for c in s1:
            need[c] = 1 + need.get(c, 0)

        # 4. Left side of sliding window
        l = 0

        # 5. Move right pointer through s2
        for r in range(len(s2)):

            # 6. Add new right character to window
            window[s2[r]] = 1 + window.get(s2[r], 0)

            # 7. If window gets too big, shrink from left
            if r - l + 1 > len(s1):

                # Remove left character from frequency count
                window[s2[l]] -= 1

                # If none of that character remain, remove the key
                if window[s2[l]] == 0:
                    del window[s2[l]]

                # Move left pointer forward
                l += 1

            # 8. Same frequencies = permutation found
            if window == need:
                return True

        # 9. Never found a permutation
        return False
        