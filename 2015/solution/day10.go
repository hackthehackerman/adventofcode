package solution

import (
	"fmt"
	"strconv"
)

func transform(s string) string {
	if len(s) == 0 {
		return ""
	}
	n := 1
	for i := 1; i < len(s); {
		if s[i] == s[0] {
			n++
			i++
		} else {
			break
		}
	}

	return fmt.Sprintf("%d%s%s", n, string(s[0]), transform(s[n:]))
}

func (Solution) Day10Part1(fn string) int {
	s := toString(fn)
	for i := 0; i < 40; i++ {
		fmt.Println(i)
		s = transform(s)
	}
	return len(s)
}

func transform_memo(s string, m map[string]string) string {
	if val, ok := m[s]; ok {
		return val
	}
	if len(s) == 0 {
		return ""
	}
	n := 1
	for i := 1; i < len(s); {
		if s[i] == s[0] {
			n++
			i++
		} else {
			break
		}
	}

	result := fmt.Sprintf("%d%s%s", n, string(s[0]), transform_memo(s[n:], m))
	m[s] = result
	return result
}

func transform_bytes(b []byte) (ret []byte) {
	for i := 0; i < len(b); {
		n := 1
		for j := i + 1; j < len(b); j++ {
			if b[j] == b[i] {
				n++
			} else {
				break
			}
		}
		ret = append(ret, byte(strconv.Itoa(n)[0]), b[i])
		i += n
	}
	return
}

func (Solution) Day10Part2(fn string) int {
	s := toString(fn)
	bytes := []byte(s)
	for i := 0; i < 50; i++ {
		bytes = transform_bytes(bytes)
	}
	return len(string(bytes))
}
