package solution

import (
	"strconv"
	"strings"
)

func (Solution) Day23Part1(fn string) int {
	lines := toLines(fn)

	ptr := 0
	reg := map[string]int{
		"a": 0,
		"b": 0,
	}

	for {
		if ptr >= len(lines) {
			break
		}
		l := lines[ptr]

		if strings.Contains(l, "hlf") {
			reg[strings.Split(l, " ")[1]] /= 2
			ptr++
		} else if strings.Contains(l, "tpl") {
			reg[strings.Split(l, " ")[1]] *= 3
			ptr++
		} else if strings.Contains(l, "inc") {
			reg[strings.Split(l, " ")[1]]++
			ptr++
		} else if strings.Contains(l, "jmp") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[1])
			ptr += val
		} else if strings.Contains(l, "jie") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[2])
			if reg[strings.Split(strings.Split(l, " ")[1], ",")[0]]%2 == 0 {
				ptr += val
			} else {
				ptr++
			}
		} else if strings.Contains(l, "jio") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[2])
			if reg[strings.Split(strings.Split(l, " ")[1], ",")[0]] == 1 {
				ptr += val
			} else {
				ptr++
			}
		} else {
			panic("unknown instruction")
		}

	}

	return reg["b"]
}

func (Solution) Day23Part2(fn string) int {
	lines := toLines(fn)

	ptr := 0
	reg := map[string]int{
		"a": 1,
		"b": 0,
	}

	for {
		if ptr >= len(lines) {
			break
		}
		l := lines[ptr]

		if strings.Contains(l, "hlf") {
			reg[strings.Split(l, " ")[1]] /= 2
			ptr++
		} else if strings.Contains(l, "tpl") {
			reg[strings.Split(l, " ")[1]] *= 3
			ptr++
		} else if strings.Contains(l, "inc") {
			reg[strings.Split(l, " ")[1]]++
			ptr++
		} else if strings.Contains(l, "jmp") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[1])
			ptr += val
		} else if strings.Contains(l, "jie") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[2])
			if reg[strings.Split(strings.Split(l, " ")[1], ",")[0]]%2 == 0 {
				ptr += val
			} else {
				ptr++
			}
		} else if strings.Contains(l, "jio") {
			val, _ := strconv.Atoi(strings.Split(l, " ")[2])
			if reg[strings.Split(strings.Split(l, " ")[1], ",")[0]] == 1 {
				ptr += val
			} else {
				ptr++
			}
		} else {
			panic("unknown instruction")
		}

	}

	return reg["b"]
}
