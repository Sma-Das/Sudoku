# Sudoku Solver

### This solver will be based on the backtracking algorihm
##### It will also have import refinements, those being:
- Active generation of valid options
  - In typical solutions every number (1-9) is tested
  - Only valid options for that cell be used
- Simple elimination
  - In cases where there is only one valid option, it will fill that value in
- Modular elimination techniques
  - Dirty cell finding techniques to reduce possible options can easily be worked into the cell options generator


#### Board Look (terminal)
![Board Preview](https://user-images.githubusercontent.com/20164942/105075244-ed74f900-5aa2-11eb-88a0-45f0360af994.png)
![Board Look](https://user-images.githubusercontent.com/20164942/105075104-c1597800-5aa2-11eb-92cf-38734b95e947.png)
