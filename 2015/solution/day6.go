package solution

import (
	"strconv"
	"strings"
)

func parsePoint(s string) Point {
	// "1,1" to x,y
	parts := strings.Split(s, ",")
	x, _ := strconv.Atoi(parts[0])
	y, _ := strconv.Atoi(parts[1])
	return Point{x, y}
}

func (Solution) Day6Part1(fn string) int {
	lines := toLines(fn)
	m := make(map[Point]bool)
	for _, line := range lines {
		parts := strings.Split(line, " ")
		if parts[0] == "toggle" {
			point1 := parsePoint(parts[1])
			point2 := parsePoint(parts[3])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = !m[Point{x, y}]
				}
			}
		} else if parts[1] == "on" {
			point1 := parsePoint(parts[2])
			point2 := parsePoint(parts[4])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = true
				}
			}

		} else {
			point1 := parsePoint(parts[2])
			point2 := parsePoint(parts[4])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = false
				}
			}
		}
	}

	c := 0
	for _, v := range m {
		if v {
			c++
		}
	}
	return c
}

func (Solution) Day6Part2(fn string) int {
	lines := toLines(fn)
	m := make(map[Point]int)
	for _, line := range lines {
		parts := strings.Split(line, " ")
		if parts[0] == "toggle" {
			point1 := parsePoint(parts[1])
			point2 := parsePoint(parts[3])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = m[Point{x, y}] + 2
				}
			}
		} else if parts[1] == "on" {
			point1 := parsePoint(parts[2])
			point2 := parsePoint(parts[4])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = m[Point{x, y}] + 1
				}
			}

		} else {
			point1 := parsePoint(parts[2])
			point2 := parsePoint(parts[4])
			for x := point1.X; x <= point2.X; x++ {
				for y := point1.Y; y <= point2.Y; y++ {
					m[Point{x, y}] = max(m[Point{x, y}]-1, 0)
				}
			}
		}
	}

	c := 0
	for _, v := range m {
		c += v
	}
	return c
}
