package solution

import (
	"math"
	"slices"
	"sort"
	"strconv"
)

func (Solution) Day24Part1(fn string) int {
	lines := toLines(fn)
	weights := []int{}
	sum := 0
	for _, line := range lines {
		val, _ := strconv.Atoi(line)
		weights = append(weights, val)
		sum += val
	}
	sort.Sort(sort.Reverse(sort.IntSlice(weights)))

	var findGroup func(target, length int, cur []int, weights []int, result *[][]int)
	findGroup = func(target, length int, cur []int, weights []int, result *[][]int) {
		if target == 0 && length == 0 {
			new_cur := make([]int, len(cur))
			copy(new_cur, cur)
			*result = append(*result, new_cur)
			return
		}
		if target < 0 || length == 0 || len(weights) == 0 {
			return
		}
		for i, weight := range weights {
			findGroup(target-weight, length-1, append(cur, weight), weights[i+1:], result)
		}
	}

	var findGroupAnyLength func(target int, cur []int, weights []int, result *[][]int)
	findGroupAnyLength = func(target int, cur []int, weights []int, result *[][]int) {
		if target == 0 {
			new_cur := make([]int, len(cur))
			copy(new_cur, cur)
			*result = append(*result, new_cur)
			return
		}
		if target < 0 || len(weights) == 0 {
			return
		}
		for i, weight := range weights {
			findGroupAnyLength(target-weight, append(cur, weight), weights[i+1:], result)
		}
	}

	remove := func(weights []int, group []int) []int {
		ret := []int{}
		for _, weight := range weights {
			if !slices.Contains(group, weight) {
				ret = append(ret, weight)
			}
		}
		return ret
	}
	// sum = 1524, sum/3 = 508
	for i := 1; i < 100; i++ {
		group1 := [][]int{}
		findGroup(sum/3, i, []int{}, weights, &group1)
		if len(group1) > 0 {
			minQE := math.MaxInt
			for _, g1 := range group1 {
				remains := remove(weights, g1)
				group2 := [][]int{}
				findGroupAnyLength(sum/3, []int{}, remains, &group2)

				if len(group2) > 0 {

					for _, g2 := range group2 {
						remains := remove(remains, g2)

						group3 := [][]int{}
						findGroupAnyLength(sum/3, []int{}, remains, &group3)
						if len(group3) > 0 {

							qe := 1
							for _, w := range g1 {
								qe *= w
							}
							minQE = min(minQE, qe)
							break
						}
					}
				}
			}
			if minQE != math.MaxInt {
				return minQE
			}
		}
	}

	return 0
}

func (Solution) Day24Part2(fn string) int {
	lines := toLines(fn)
	weights := []int{}
	sum := 0
	for _, line := range lines {
		val, _ := strconv.Atoi(line)
		weights = append(weights, val)
		sum += val
	}
	sort.Sort(sort.Reverse(sort.IntSlice(weights)))

	var findGroup func(target, length int, cur []int, weights []int, result *[][]int)
	findGroup = func(target, length int, cur []int, weights []int, result *[][]int) {
		if target == 0 && length == 0 {
			new_cur := make([]int, len(cur))
			copy(new_cur, cur)
			*result = append(*result, new_cur)
			return
		}
		if target < 0 || length == 0 || len(weights) == 0 {
			return
		}
		for i, weight := range weights {
			findGroup(target-weight, length-1, append(cur, weight), weights[i+1:], result)
		}
	}

	var findGroupAnyLength func(target int, cur []int, weights []int, result *[][]int)
	findGroupAnyLength = func(target int, cur []int, weights []int, result *[][]int) {
		if target == 0 {
			new_cur := make([]int, len(cur))
			copy(new_cur, cur)
			*result = append(*result, new_cur)
			return
		}
		if target < 0 || len(weights) == 0 {
			return
		}
		for i, weight := range weights {
			findGroupAnyLength(target-weight, append(cur, weight), weights[i+1:], result)
		}
	}

	remove := func(weights []int, group []int) []int {
		ret := []int{}
		for _, weight := range weights {
			if !slices.Contains(group, weight) {
				ret = append(ret, weight)
			}
		}
		return ret
	}

	for i := 1; i < 100; i++ {
		group1 := [][]int{}
		findGroup(sum/4, i, []int{}, weights, &group1)
		if len(group1) > 0 {
			minQE := math.MaxInt
			for _, g1 := range group1 {
				remains := remove(weights, g1)
				group2 := [][]int{}
				findGroupAnyLength(sum/4, []int{}, remains, &group2)
				if len(group2) > 0 {
					for _, g2 := range group2 {
						remains := remove(remains, g2)
						group3 := [][]int{}
						findGroupAnyLength(sum/4, []int{}, remains, &group3)
						if len(group3) > 0 {
							for _, g3 := range group3 {
								remains := remove(remains, g3)
								group4 := [][]int{}
								findGroupAnyLength(sum/4, []int{}, remains, &group4)
								if len(group4) > 0 {
									qe := 1
									for _, w := range g1 {
										qe *= w
									}
									minQE = min(minQE, qe)
									break
								}
							}
						}
					}
				}
			}
			if minQE != math.MaxInt {
				return minQE
			}
		}
	}

	return 0
}
