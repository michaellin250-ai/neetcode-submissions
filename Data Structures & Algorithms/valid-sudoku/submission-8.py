class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) 

        for r in range(9):
            for c in range(9):
                val = board[r][c] 

                if val == '.':
                    continue 
                
                box_key = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
        return True 


        #The defaultdict(set) makes it so we can store values we've seen before, fast duplicate checking, great whenver the problem asks have I seen this before 
        #The box_key identifies which 3 x 3 box im in, and boxes[box_key] stores the number I've already seen in that box. 
        #1.Main idea, make sure that we get our value at whatever the row/column is via val = board[r][c]
        #2. If val == '.': then continue of course
        #3. Our box_Key = (r // 3, c // 3)
        #4. Then we have our if statements, which is like the if theirs any same values so.
        #   something like if val in rows[r] or val in cols[c] or val in boxes[box_key]: return False 
        #5. Then if no return false, just add those values via rows[r].add(val), cols[c].add(val), and boxes[box_key].add(val)