def count_ordered_checkpoints(n, m, checkpoints):
    def is_reachable(start, end):
        return start[1] <= end[1]  # Can only move right
    
    def count_between_ordered_points(points):
        if not points:
            return 1
            
        total = 0
        curr = points[0]
        rest = points[1:]
        
        # Try each checkpoint as next point
        for i, next_point in enumerate(rest):
            if is_reachable(curr, next_point):
                paths = count_between_points(curr, next_point)
                if paths > 0:
                    total += paths * count_between_ordered_points(rest[:i] + rest[i+1:])
        
        return total
    
    return count_between_ordered_points([(0,0)] + checkpoints + [(n-1,m-1)])
