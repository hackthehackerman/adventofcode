package solution

import (
	"os"
	"strings"
)

type Solution struct {
}

type Point struct {
	X int
	Y int
}

func toLines(fn string) (r []string) {
	s := toString(fn)
	return strings.Split(s, "\n")
}

func toString(fn string) (r string) {
	bytes, _ := os.ReadFile(fn)
	return string(bytes)
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(x int) int {
	if x >= 0 {
		return x
	} else {
		return -x
	}
}
