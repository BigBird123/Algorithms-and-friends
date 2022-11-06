# Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from _**1**_ to _**n**_. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API _**int guess(int num)**_, which returns three possible results:
  - _**-1**_: Your guess is higher than the number I picked (i.e. _**num > pick**_).
  - _**1**_: Your guess is lower than the number I picked (i.e. _**num < pick**_).
  - _**0**_: your guess is equal to the number I picked (i.e. _**num == pick**_).

Return _the number_ that I picked.
### Related Topics
     Array     Binary_Search
### Example:
Example 1:
    
    Input: n = 10, pick = 6
    Output: 6
Example 2:

    Input: n = 1, pick = 1
    Output: 1
Example 3:

    Input: n = 2, pick = 1
    Output: 1
### Constraints

>- 1 <= n <= 231 - 1
>- 1 <= pick <= n
