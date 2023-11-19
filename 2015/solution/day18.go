package solution

func step(m [][]bool) (ret [][]bool) {
	ret = make([][]bool, len(m))
	for i := 0; i < len(m); i++ {
		ret[i] = make([]bool, len(m[i]))
	}

	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			on := 0
			for x := i - 1; x <= i+1; x++ {
				for y := j - 1; y <= j+1; y++ {
					if x == i && y == j {
						continue
					}
					if x < 0 || x >= len(m) || y < 0 || y >= len(m[i]) {
						continue
					}
					if m[x][y] {
						on++
					}
				}
			}

			if m[i][j] {
				ret[i][j] = (on == 2 || on == 3)
			} else {
				ret[i][j] = (on == 3)
			}

		}
	}
	return
}

func (Solution) Day18Part1(fn string) int {
	lines := toLines(fn)
	matrix := [][]bool{}
	for _, line := range lines {
		row := []bool{}
		for _, c := range line {
			row = append(row, c == '#')
		}
		matrix = append(matrix, row)
	}
	for i := 0; i < 100; i++ {
		matrix = step(matrix)
		// fmt.Println("After", i+1, "steps")
		// for _, row := range matrix {
		// 	fmt.Println(row)
		// }
	}

	count := 0
	for _, row := range matrix {
		for _, c := range row {
			if c {
				count++
			}
		}
	}

	return count
}

func step2(m [][]bool) (ret [][]bool) {
	ret = make([][]bool, len(m))
	for i := 0; i < len(m); i++ {
		ret[i] = make([]bool, len(m[i]))
	}

	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			on := 0
			for x := i - 1; x <= i+1; x++ {
				for y := j - 1; y <= j+1; y++ {
					if x == i && y == j {
						continue
					}
					if x < 0 || x >= len(m) || y < 0 || y >= len(m[i]) {
						continue
					}
					if m[x][y] {
						on++
					}
				}
			}

			if m[i][j] {
				ret[i][j] = (on == 2 || on == 3)
			} else {
				ret[i][j] = (on == 3)
			}

		}
	}
	ret[0][0] = true
	ret[0][len(ret[0])-1] = true
	ret[len(ret)-1][0] = true
	ret[len(ret)-1][len(ret[0])-1] = true

	return
}

func (Solution) Day18Part2(fn string) int {
	lines := toLines(fn)
	matrix := [][]bool{}
	for _, line := range lines {
		row := []bool{}
		for _, c := range line {
			row = append(row, c == '#')
		}
		matrix = append(matrix, row)
	}
	for i := 0; i < 100; i++ {
		matrix = step2(matrix)
		// fmt.Println("After", i+1, "steps")
		// for _, row := range matrix {
		// 	fmt.Println(row)
		// }
	}

	count := 0
	for _, row := range matrix {
		for _, c := range row {
			if c {
				count++
			}
		}
	}

	return count
}
