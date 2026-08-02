from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, there is nothing to search for
        if t == "":
            return ""

        # Count how many of each character we need from t
        t_counts = Counter(t)

        # Counts of characters in the current sliding window
        window_counts = defaultdict(int)

        # Number of unique characters we need to satisfy
        required_matches = len(t_counts)

        # Number of unique characters currently satisfied in the window
        matches = 0

        # Best answer so far: [left_index, right_index]
        res = [-1, -1]

        # Length of the best window found so far
        res_len = float("inf")

        # Left pointer of the sliding window
        l = 0

        # Right pointer expands the window
        for r in range(len(s)):
            # Current character at the right end
            c = s[r]

            # Add this character to the current window count
            window_counts[c] += 1

            # If this character is needed, and we just reached the exact amount needed,
            # then this character type is now satisfied
            if c in t_counts and window_counts[c] == t_counts[c]:
                matches += 1

            # While the current window is valid, try shrinking it from the left
            while matches == required_matches:
                # Update best answer if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Remove the leftmost character from the window
                left_char = s[l]
                window_counts[left_char] -= 1

                # If we removed a needed character and now we have too few,
                # then this character type is no longer satisfied
                if left_char in t_counts and window_counts[left_char] < t_counts[left_char]:
                    matches -= 1

                # Move left pointer inward
                l += 1

        # If we never found a valid window, return empty string
        if res_len == float("inf"):
            return ""

        # Otherwise return the best substring
        left, right = res
        return s[left:right + 1]