package solution

import (
	"strconv"
)

func (Solution) Day20Part1(fn string) int {
	s := toString(fn)
	target, _ := strconv.Atoi(s)

	m := map[int]int{}
	for i := 1; i <= target/10; i++ {
		j := i
		for j <= target {
			m[j] += i * 10
			j += i
		}
		if m[i] >= target {
			return i
		}
	}

	return -1
}

func (Solution) Day20Part2(fn string) int {
	s := toString(fn)
	target, _ := strconv.Atoi(s)

	m := map[int]int{}
	for i := 1; i <= target/10; i++ {
		j := i
		for k := 0; k < 50; k++ {
			m[j] += i * 11
			j += i
		}
		if m[i] >= target {
			return i
		}
	}

	return -1
}
