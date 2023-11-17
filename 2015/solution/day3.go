package solution

func (Solution) Day3Part1(fn string) int {
	s := toString(fn)
	c := 1
	cur := Point{}
	m := map[Point]bool{cur: true}

	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '^':
			cur.Y++
		case 'v':
			cur.Y--
		case '>':
			cur.X++
		case '<':
			cur.X--
		}
		if !m[cur] {
			c++
			m[cur] = true
		}
	}
	return c
}

func (Solution) Day3Part2(fn string) int {
	s := toString(fn)
	c := 1
	cur1 := Point{}
	cur2 := Point{}
	m := map[Point]bool{cur1: true}
	cur1_turn := true

	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '^':
			if cur1_turn {
				cur1.Y++
			} else {
				cur2.Y++
			}
		case 'v':
			if cur1_turn {
				cur1.Y--
			} else {
				cur2.Y--
			}
		case '>':
			if cur1_turn {
				cur1.X++
			} else {
				cur2.X++
			}
		case '<':
			if cur1_turn {
				cur1.X--
			} else {
				cur2.X--
			}
		}
		if cur1_turn {
			if !m[cur1] {
				c++
				m[cur1] = true
			}
		} else {
			if !m[cur2] {
				c++
				m[cur2] = true
			}
		}
		cur1_turn = !cur1_turn
	}
	return c
}
