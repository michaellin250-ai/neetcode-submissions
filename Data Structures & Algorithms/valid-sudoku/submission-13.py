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
        


        #1.We set up the rows, cols, and boxes with our defaultdict(set) because it allows for fast lookup without having to worry about duplicates. 
        #2.Then we go into it with two for loops, for r in range(9) representing the rows and for c in range(9) representing the columns.
        #3.Then we get the value we're at in our soduku by just doing val = board[r][c]. 
        #4.If our space is like empty like '.' we'll just continue 
        #5.Then, we'll have to get our box_key to satisfy the 3 x 3 sub-boxes requriement. So we'll do that by box_key = (r // 3, c // 3) 
        #5.Then we do our testing to see if like our value is a duplicate, via if statement. So if val in rows[r] or val in cols[c] or val in boxes[box_key]
        #6.If its there then we return False. Otherwise we'll just do rows[r].add(val), cols[c].add(val) asnd boxes[box_key].add(val) 
        #7.When everything is done just do return True. 

        #O(N^2) solution.
        #O(N^2) memory. 