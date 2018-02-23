# Week 2: Happy Ladybugs

Challenge proposed 2/20, due 2/23

-----------------------------------------------------------

> Happy Ladybugs is a board game having the following properties.
> - The board is represented by a string, ``b``, of length ``n``. The ``i``th character of the string, ``bi``, denotes the ``i``th cell of the board.
>  - If ``bi`` is an underscore (i.e., _), it means the  cell of the board is empty.
>  - If ``bi`` is an uppercase English alphabetic letter (i.e., A through Z), it means the  cell contains a ladybug of color ``bi``.
>  - String ``b`` will not contain any other characters.
> - A ladybug is happy only when its left or right adjacent cell (i.e., ``bi+/-1``) is occupied by another ladybug having the same color.
> - In a single move, you can move a ladybug from its current position to any empty cell.
> 
> Given the values of ``n`` and ``b`` for ``g`` games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, print YES on a new line if all the ladybugs can be made happy through some number of moves; otherwise, print NO to indicate that no number of moves will result in all the ladybugs being happy.

source: https://www.hackerrank.com/challenges/happy-ladybugs/problem
