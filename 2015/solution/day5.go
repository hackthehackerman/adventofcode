package solution

import (
	"strings"
)

func isNice(s string) bool {
	vowels := 0
	double := 0

	for i := 0; i < len(s); i++ {
		if strings.Contains("aeiou", string(s[i])) {
			vowels++
		}

		if i > 0 && s[i] == s[i-1] {
			double++
		}

		if i > 0 && strings.Contains("ab cd pq xy", s[i-1:i+1]) {
			return false
		}
	}
	return vowels >= 3 && double >= 1
}

func (Solution) Day5Part1(fn string) int {
	lines := toLines(fn)
	nice := 0
	for _, line := range lines {
		if isNice(line) {
			nice++
		}
	}
	return nice
}

func isNice2(s string) bool {
	pair := false
	l := false

	m := make(map[string]int)
	for i := 0; i < len(s); i++ {
		if i+1 < len(s) {
			if val, ok := m[s[i:i+2]]; ok && val != i-1 {
				pair = true
				break
			}

			if _, ok := m[s[i:i+2]]; !ok {
				m[s[i:i+2]] = i
			}
		}
	}

	for i := 0; i < len(s); i++ {
		if i+2 < len(s) {
			if s[i] == s[i+2] {
				l = true
				break
			}
		}
	}

	return pair && l
}

func (Solution) Day5Part2(fn string) int {
	lines := toLines(fn)
	nice := 0
	for _, line := range lines {
		if isNice2(line) {
			nice++
		}
	}
	return nice
}
