package solution

func next(b []byte) {
	for i := len(b) - 1; i >= 0; i-- {
		if b[i] == 'z' {
			b[i] = 'a'
		} else {
			b[i]++
			break
		}
	}
	return
}

func valid(b []byte) bool {
	r1 := false
	r3idx := -1
	r3 := false

	for i := 0; i < len(b); i++ {
		if i < len(b)-2 && !r1 {
			if b[i]+1 == b[i+1] && b[i+1]+1 == b[i+2] {
				r1 = true
			}
		}

		if b[i] == 'i' || b[i] == 'o' || b[i] == 'l' {
			return false
		}

		if i < len(b)-1 && r3idx == -1 {
			if b[i] == b[i+1] {
				r3idx = i
			}
		} else if i < len(b)-1 && r3idx != -1 {
			if b[i] == b[i+1] && i != r3idx && b[i] != b[r3idx] {
				r3 = true
			}
		}

	}
	return r1 && r3
}

func (Solution) Day11Part1(fn string) string {
	s := toString(fn)
	b := []byte(s)
	for {
		next(b)
		if valid(b) {
			return string(b)
		}
	}
}

func (Solution) Day11Part2(fn string) string {
	s := toString(fn)
	b := []byte(s)
	found := false
	for {
		next(b)
		if valid(b) {
			if found {
				return string(b)
			} else {
				found = true
				continue
			}
		}
	}
}
