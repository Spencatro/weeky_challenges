package main

import (
	"fmt"
	"strings"
)

func ladybug(board string) bool {
	if strings.Contains(board, "_") {
		// build count map
		counts := map[uint8]int{};
		for idx := 0; idx < len(board); idx += 1 {
			ch := board[idx]
			if ch != '_' {
				_, charExists := counts[ch]
				if !charExists {
					counts[ch] = 0
				}
				counts[ch] += 1
			}
		}
		// check count map
		success := true
		for _, value := range counts {
			if value < 2 {
				success = false
			}
		}
		return success
	} else {
		// board must start happy else it is sad
		if len(board) < 2 {
			return false
		}
		lastIdx := len(board) - 1
		allHappy := board[0] == board[1] && board[lastIdx] == board[lastIdx-1]
		for idx := 1; idx < len(board) - 1; idx += 1 {
			allHappy = allHappy && (board[idx] == board[idx + 1] || board[idx] == board[idx-1])
		}
		return allHappy
	}
}

func wrap(board string) string {
	if ladybug(board) {
		return "YES"
	} else {
		return "NO"
	}
}

func main() {
	var numGames int;
	fmt.Scan(&numGames)
	for idx := 0; idx < numGames; idx++ {
		var boardLen int;
		var board string;
		fmt.Scan(&boardLen)
		fmt.Scan(&board)
		fmt.Println(wrap(board))
	}
}