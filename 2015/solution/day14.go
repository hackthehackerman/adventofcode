package solution

import (
	"fmt"
)

func (Solution) Day14Part1(fn string) int {
	lines := toLines(fn)
	m := make(map[string][]int)

	for _, line := range lines {
		var name string
		var speed, fly, rest int
		fmt.Sscanf(line, "%s can fly %d km/s for %d seconds, but then must rest for %d seconds.", &name, &speed, &fly, &rest)
		m[name] = []int{speed, fly, rest}
	}

	seconds := 2503
	ret := 0
	for _, v := range m {
		dist := v[0] * (seconds / (v[1] + v[2]) * v[1])
		remain := seconds % (v[1] + v[2])
		if remain > v[1] {
			dist += v[0] * v[1]
		} else {
			dist += v[0] * remain
		}

		ret = max(ret, dist)
	}

	return ret
}

func (Solution) Day14Part2(fn string) int {
	lines := toLines(fn)
	m := make(map[string][]int)
	scores := make(map[string]int)

	for _, line := range lines {
		var name string
		var speed, fly, rest int
		fmt.Sscanf(line, "%s can fly %d km/s for %d seconds, but then must rest for %d seconds.", &name, &speed, &fly, &rest)
		m[name] = []int{speed, fly, rest}
		scores[name] = 0
	}

	dist := func(speed, fly, rest, seconds int) int {
		d := speed * (seconds / (fly + rest) * fly)
		remain := seconds % (fly + rest)
		if remain > fly {
			d += speed * fly
		} else {
			d += speed * remain
		}
		return d
	}

	seconds := 2503
	for i := 1; i <= seconds; i++ {
		maxDist := 0
		for _, v := range m {
			d := dist(v[0], v[1], v[2], i)
			if d > maxDist {
				maxDist = d
			}
		}
		for k, v := range m {
			if dist(v[0], v[1], v[2], i) == maxDist {
				scores[k]++
			}
		}
	}

	ret := 0
	for _, v := range scores {
		ret = max(ret, v)
	}

	return ret
}
