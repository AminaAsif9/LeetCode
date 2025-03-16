class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the original color is the same as the target color, no changes are needed
        if original_color == color:
            return image
        
        # Define the 4-directional movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Get the dimensions of the image
        rows, cols = len(image), len(image[0])
        
        # Use a stack for DFS (you can also use a queue for BFS)
        stack = [(sr, sc)]
        
        # Perform DFS
        while stack:
            x, y = stack.pop()  # Get the current pixel
            
            # Change the color of the current pixel
            image[x][y] = color
            
            # Explore all 4-directional neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the neighbor is within bounds and has the original color
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color:
                    stack.append((nx, ny))  # Add to stack for further processing
        
        return image