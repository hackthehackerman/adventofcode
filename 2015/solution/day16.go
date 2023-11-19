package solution

import (
	"strconv"
	"strings"
)

func (Solution) Day16Part1(fn string) int {
	lines := toLines(fn)
	items := []map[string]int{}

	for _, line := range lines {
		// Sue 1: children: 1, cars: 8, vizslas: 7
		parts := strings.Split(line, " ")
		name1 := parts[2][:len(parts[2])-1]
		name2 := parts[4][:len(parts[4])-1]
		name3 := parts[6][:len(parts[6])-1]

		number1_str := parts[3][:len(parts[3])-1]
		number2_str := parts[5][:len(parts[5])-1]
		number3_str := parts[7]

		number1, _ := strconv.Atoi(number1_str)
		number2, _ := strconv.Atoi(number2_str)
		number3, _ := strconv.Atoi(number3_str)

		items = append(items, map[string]int{name1: number1, name2: number2, name3: number3})
	}

	tape := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}

	for i, item := range items {
		match := true
		for k, v := range item {
			if tape[k] != v {
				match = false
				break
			}
		}
		if match {
			return i + 1
		}
	}

	return 0
}

func (Solution) Day16Part2(fn string) int {
	lines := toLines(fn)
	items := []map[string]int{}

	for _, line := range lines {
		// Sue 1: children: 1, cars: 8, vizslas: 7
		parts := strings.Split(line, " ")
		name1 := parts[2][:len(parts[2])-1]
		name2 := parts[4][:len(parts[4])-1]
		name3 := parts[6][:len(parts[6])-1]

		number1_str := parts[3][:len(parts[3])-1]
		number2_str := parts[5][:len(parts[5])-1]
		number3_str := parts[7]

		number1, _ := strconv.Atoi(number1_str)
		number2, _ := strconv.Atoi(number2_str)
		number3, _ := strconv.Atoi(number3_str)

		items = append(items, map[string]int{name1: number1, name2: number2, name3: number3})
	}

	tape := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}

	for i, item := range items {
		match := true
		for k, v := range item {
			if k == "cats" || k == "trees" {
				if tape[k] >= v {
					match = false
					break
				}
			} else if k == "pomeranians" || k == "goldfish" {
				if tape[k] <= v {
					match = false
					break
				}
			} else if tape[k] != v {
				match = false
				break
			}
		}
		if match {
			return i + 1
		}
	}

	return 0
}
