package solution

import (
	"math"
	"strconv"
)

func (Solution) Day17Part1(fn string) int {
	lines := toLines(fn)
	containers := []int{}
	for _, line := range lines {
		n, _ := strconv.Atoi(line)
		containers = append(containers, n)
	}

	var walk func(idx int, remains int)
	var count int
	walk = func(idx int, remains int) {
		if remains == 0 {
			count++
			return
		}
		if idx >= len(containers) {
			return
		}
		walk(idx+1, remains)
		if remains >= containers[idx] {
			walk(idx+1, remains-containers[idx])
		}
	}
	walk(0, 150)
	return count
}

func (Solution) Day17Part2(fn string) int {
	lines := toLines(fn)
	containers := []int{}
	for _, line := range lines {
		n, _ := strconv.Atoi(line)
		containers = append(containers, n)
	}

	used := make([]bool, len(containers))

	var walk func(idx int, remains int)
	count := make(map[int]int)
	walk = func(idx int, remains int) {
		if remains == 0 {
			cnt := 0
			for _, u := range used {
				if u {
					cnt++
				}
			}
			count[cnt] = count[cnt] + 1
			return
		}
		if idx >= len(containers) {
			return
		}
		used[idx] = false
		walk(idx+1, remains)

		if remains >= containers[idx] {
			used[idx] = true
			walk(idx+1, remains-containers[idx])
			used[idx] = false
		}
	}
	walk(0, 150)

	min := math.MaxInt
	for k := range count {
		if k < min {
			min = k
		}
	}
	return count[min]
}
