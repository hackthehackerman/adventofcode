package solution

func (Solution) Day1Part1(fn string) int {
	s := toString(fn)
	c := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			c++
		} else {
			c--
		}
	}
	return c
}

func (Solution) Day1Part2(fn string) int {
	s := toString(fn)
	c := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			c++
		} else {
			c--
		}
		if c == -1 {
			return i + 1
		}
	}
	return -1
}
