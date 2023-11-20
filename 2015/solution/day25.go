package solution

func (Solution) Day25Part1(fn string) int {
	// To continue, please consult the code grid in the manual. Enter the code at row 2981, column 3075.

	row, col := 2981, 3075
	steps := 0
	for i := 1; i <= col; i++ {
		steps += i
	}

	for i := 1; i < row; i++ {
		steps += col + i - 1
	}

	start := 20151125
	for i := 1; i < steps; i++ {
		start = (start * 252533) % 33554393
	}
	return start
}
