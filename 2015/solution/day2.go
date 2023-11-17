package solution

import (
	"sort"
	"strconv"
	"strings"
)

func (Solution) Day2Part1(fn string) int {
	lines := toLines(fn)
	var c int
	for _, l := range lines {
		dimensions := strings.Split(l, "x")
		d := make([]int, 3)
		d[0], _ = strconv.Atoi(dimensions[0])
		d[1], _ = strconv.Atoi(dimensions[1])
		d[2], _ = strconv.Atoi(dimensions[2])

		sort.Ints(d)

		c += 2*(d[0]*d[1]+d[1]*d[2]+d[0]*d[2]) + d[0]*d[1]
	}
	return c
}

func (Solution) Day2Part2(fn string) int {
	lines := toLines(fn)
	var c int
	for _, l := range lines {
		dimensions := strings.Split(l, "x")
		d := make([]int, 3)
		d[0], _ = strconv.Atoi(dimensions[0])
		d[1], _ = strconv.Atoi(dimensions[1])
		d[2], _ = strconv.Atoi(dimensions[2])

		sort.Ints(d)

		c += 2*(d[0]+d[1]) + d[0]*d[1]*d[2]
	}
	return c
}
