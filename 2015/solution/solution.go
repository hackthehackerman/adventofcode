package solution

import (
	"os"
	"reflect"
	"strings"
)

type Solution struct {
}

type Point struct {
	X int
	Y int
}

func toLines(fn string) (r []string) {
	s := toString(fn)
	return strings.Split(s, "\n")
}

func toString(fn string) (r string) {
	bytes, _ := os.ReadFile(fn)
	return string(bytes)
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func abs(x int) int {
	if x >= 0 {
		return x
	} else {
		return -x
	}
}

func permutationsInt(arr []int) [][]int {
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int) {
		if n == 1 {
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

func permutationsString(arr []string) [][]string {
	var helper func([]string, int)
	res := [][]string{}

	helper = func(arr []string, n int) {
		if n == 1 {
			tmp := make([]string, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

func deepCopySlice[T any](original []T) []T {
	copied := make([]T, len(original))
	for i, v := range original {
		// Use reflect to check if element is a struct and contains reference types
		if reflect.ValueOf(v).Kind() == reflect.Struct {
			// Handle struct with a custom deep copy logic specific to your structs
			// This part is tricky and depends on your struct's structure
		} else {
			copied[i] = v
		}
	}
	return copied
}

func deepCopyMap[K comparable, V any](original map[K]V) map[K]V {
	copied := make(map[K]V)
	for key, value := range original {
		copied[key] = value
	}
	return copied
}
