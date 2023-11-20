package solution

import (
	"strings"
)

func (Solution) Day19Part1(fn string) int {
	lines := toLines(fn)
	molecule := lines[len(lines)-1]
	replacements := map[string][]string{}

	for idx, line := range lines {
		if idx <= len(lines)-3 {
			parts := strings.Split(line, " => ")
			l := parts[0]
			r := parts[1]
			if _, ok := replacements[l]; !ok {
				replacements[l] = []string{}
			}
			replacements[l] = append(replacements[l], r)
		}
	}

	cnt := map[string]int{}
	for k, v := range replacements {
		for _, r := range v {
			for i := 0; i < len(molecule); i++ {
				if i+len(k) > len(molecule) {
					continue
				}
				if molecule[i:i+len(k)] == k {
					cnt[molecule[:i]+r+molecule[i+len(k):]]++
				}
			}
		}
	}

	return len(cnt)
}

func (Solution) Day19Part2(fn string) int {
	lines := toLines(fn)
	molecule := lines[len(lines)-1]
	replacements := map[string]string{}

	for idx, line := range lines {
		if idx <= len(lines)-3 {
			parts := strings.Split(line, " => ")
			l := parts[0]
			r := parts[1]
			replacements[r] = l
		}
	}
	memo := map[string]int{}

	var walk func(m string, steps int) int
	walk = func(m string, steps int) int {
		if v, ok := memo[m]; ok {
			return v
		}
		if m == "e" {
			return steps
		}
		for k, v := range replacements {
			nm := m
			count := strings.Count(nm, k)
			if count == 0 {
				continue
			}
			nm = strings.ReplaceAll(nm, k, v)
			walkcnt := walk(nm, steps+count)

			if walkcnt > 0 {
				return walkcnt
			} else {
				memo[nm] = walkcnt
			}
		}
		memo[m] = -1
		return -1
	}
	return walk(molecule, 0)
}
