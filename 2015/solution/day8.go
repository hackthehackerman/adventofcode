package solution

func (Solution) Day8Part1(fn string) int {
	lines := toLines(fn)
	c1 := 0
	c2 := 0

	for _, line := range lines {
		c1 += len(line)
		line = line[1 : len(line)-1]
		decoded := 0
		for i := 0; i < len(line); {
			if line[i] == '\\' {
				if line[i+1] == '\\' || line[i+1] == '"' {
					i += 2
				} else if line[i+1] == 'x' {
					i += 4
				}
			} else {
				i++
			}
			decoded++
		}
		c2 += decoded
	}

	return c1 - c2
}

func (Solution) Day8Part2(fn string) int {
	lines := toLines(fn)
	c1 := 0
	c2 := 0

	for _, line := range lines {
		c1 += len(line)
		encoded := 0
		for i := 0; i < len(line); {
			if line[i] == '\\' || line[i] == '"' {
				encoded += 2
			} else {
				encoded++
			}
			i++
		}
		c2 += (encoded + 2)
	}

	return c2 - c1
}
