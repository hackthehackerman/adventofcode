package solution

import (
	"fmt"
	"math"
)

func (Solution) Day9Part1(fn string) int {
	lines := toLines(fn)
	m := make(map[string]int)
	c := 0
	for _, line := range lines {
		var a, b string
		var d int
		fmt.Sscanf(line, "%s to %s = %d", &a, &b, &d)
		if _, ok := m[a]; !ok {
			m[a] = c
			c++
		}
		if _, ok := m[b]; !ok {
			m[b] = c
			c++
		}
	}
	d := make([][]int, c)
	for i := 0; i < c; i++ {
		d[i] = make([]int, c)
	}
	for _, line := range lines {
		var a, b string
		var dd int
		fmt.Sscanf(line, "%s to %s = %d", &a, &b, &dd)
		d[m[a]][m[b]] = dd
		d[m[b]][m[a]] = dd
	}

	path := make([]int, c)
	for i := 0; i < c; i++ {
		path[i] = i
	}

	p := permutations(path)

	min_dist := math.MaxInt
	for _, path := range p {
		dist := 0
		for i := 0; i < len(path)-1; i++ {
			dist += d[path[i]][path[i+1]]
		}
		if dist < min_dist {
			min_dist = dist
		}
	}

	return min_dist
}

func (Solution) Day9Part2(fn string) int {
	lines := toLines(fn)
	m := make(map[string]int)
	c := 0
	for _, line := range lines {
		var a, b string
		var d int
		fmt.Sscanf(line, "%s to %s = %d", &a, &b, &d)
		if _, ok := m[a]; !ok {
			m[a] = c
			c++
		}
		if _, ok := m[b]; !ok {
			m[b] = c
			c++
		}
	}
	d := make([][]int, c)
	for i := 0; i < c; i++ {
		d[i] = make([]int, c)
	}
	for _, line := range lines {
		var a, b string
		var dd int
		fmt.Sscanf(line, "%s to %s = %d", &a, &b, &dd)
		d[m[a]][m[b]] = dd
		d[m[b]][m[a]] = dd
	}

	path := make([]int, c)
	for i := 0; i < c; i++ {
		path[i] = i
	}

	p := permutations(path)

	max_dist := math.MinInt
	for _, path := range p {
		dist := 0
		for i := 0; i < len(path)-1; i++ {
			dist += d[path[i]][path[i+1]]
		}
		if dist > max_dist {
			max_dist = dist
		}
	}

	return max_dist
}
