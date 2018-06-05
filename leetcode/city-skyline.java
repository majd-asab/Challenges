/*
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
What is the maximum total sum that the height of the buildings can be increased?
*/
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[][] newGrid = new int[grid.length][grid[0].length];
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0;j < grid[0].length; j++){
               
               int maxRow = maxInRow(grid[i]);
               int maxColumn = maxInColumn(grid,j);
               // if(maxRow < maxColumn){
               //     newGrid[i][j] = maxRow;
               // }else{
               //     newGrid[i][j] = maxColumn;
               // }
               newGrid[i][j] = (maxRow < maxColumn)? maxRow : maxColumn;
               System.out.print(newGrid[i][j]);
            }
             System.out.println();
        }
        return 0;
    }
    
    // Return the max number in an array.
    public int maxInRow(int[] arr){
        int max = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max) max = arr[i];
        }
        return max;
    }
    
    // Return the max number out of a bunch of arrays at a specific index.
    public int maxInColumn(int[][] grid, int index){
        int max = grid[0][index];
        for(int i = 0; i < grid.length; i++){
            if(grid[i][index] > max) max = grid[i][index];
        }
        return max;
    }
}
