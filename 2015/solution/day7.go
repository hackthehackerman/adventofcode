package solution

import (
	"strconv"
	"strings"
)

func (Solution) Day7Part1(fn string) int {
	lines := toLines(fn)
	m := make(map[string]string)
	for _, line := range lines {
		parts := strings.Split(line, " -> ")
		m[parts[1]] = parts[0]
	}

	var dfs func(reg string, m map[string]string, memo map[string]uint16) uint16
	dfs = func(reg string, m map[string]string, memo map[string]uint16) uint16 {
		if val, ok := memo[reg]; ok {
			return val
		}
		var ret uint16
		if val, err := strconv.Atoi(reg); err == nil {
			ret = uint16(val)
		} else {

			parts := strings.Split(m[reg], " ")
			if parts[0] == "NOT" {
				val := dfs(parts[1], m, memo)
				ret = ^val
			} else if len(parts) == 1 {
				ret = dfs(parts[0], m, memo)
			} else if parts[1] == "AND" {
				val1 := dfs(parts[0], m, memo)
				val2 := dfs(parts[2], m, memo)
				ret = val1 & val2
			} else if parts[1] == "OR" {
				val1 := dfs(parts[0], m, memo)
				val2 := dfs(parts[2], m, memo)
				ret = val1 | val2
			} else if parts[1] == "LSHIFT" {
				val1 := dfs(parts[0], m, memo)
				val2, _ := strconv.Atoi(parts[2])
				ret = val1 << val2
			} else if parts[1] == "RSHIFT" {
				val1 := dfs(parts[0], m, memo)
				val2, _ := strconv.Atoi(parts[2])
				ret = val1 >> val2
			} else {
				panic("Unknown instruction")
			}
		}

		memo[reg] = ret
		return ret
	}

	memo := make(map[string]uint16)
	val := dfs("a", m, memo)

	return int(val)
}

func (Solution) Day7Part2(fn string) int {
	lines := toLines(fn)
	m := make(map[string]string)
	for _, line := range lines {
		parts := strings.Split(line, " -> ")
		m[parts[1]] = parts[0]
	}

	var dfs func(reg string, m map[string]string, memo map[string]uint16) uint16
	dfs = func(reg string, m map[string]string, memo map[string]uint16) uint16 {
		if val, ok := memo[reg]; ok {
			return val
		}
		var ret uint16
		if val, err := strconv.Atoi(reg); err == nil {
			ret = uint16(val)
		} else {

			parts := strings.Split(m[reg], " ")
			if parts[0] == "NOT" {
				val := dfs(parts[1], m, memo)
				ret = ^val
			} else if len(parts) == 1 {
				ret = dfs(parts[0], m, memo)
			} else if parts[1] == "AND" {
				val1 := dfs(parts[0], m, memo)
				val2 := dfs(parts[2], m, memo)
				ret = val1 & val2
			} else if parts[1] == "OR" {
				val1 := dfs(parts[0], m, memo)
				val2 := dfs(parts[2], m, memo)
				ret = val1 | val2
			} else if parts[1] == "LSHIFT" {
				val1 := dfs(parts[0], m, memo)
				val2, _ := strconv.Atoi(parts[2])
				ret = val1 << val2
			} else if parts[1] == "RSHIFT" {
				val1 := dfs(parts[0], m, memo)
				val2, _ := strconv.Atoi(parts[2])
				ret = val1 >> val2
			} else {
				panic("Unknown instruction")
			}
		}

		memo[reg] = ret
		return ret
	}

	memo := make(map[string]uint16)
	val := dfs("a", m, memo)
	m["b"] = strconv.Itoa(int(val))
	memo = make(map[string]uint16)
	val = dfs("a", m, memo)

	return int(val)
}
