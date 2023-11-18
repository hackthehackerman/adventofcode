package solution

import (
	"encoding/json"
	"regexp"
	"strconv"
)

func (Solution) Day12Part1(fn string) int {
	s := toString(fn)
	re := regexp.MustCompile(`-?\d+`)

	// Find all matches
	matches := re.FindAllString(s, -1)
	sum := 0
	for _, match := range matches {
		val, _ := strconv.Atoi(match)
		sum += val
	}

	// Count the matches
	return sum
}

func traverse(node interface{}) int {
	switch node.(type) {
	case []interface{}:
		sum := 0
		for _, v := range node.([]interface{}) {
			sum += traverse(v)
		}
		return sum
	case map[string]interface{}:
		sum := 0
		for _, v := range node.(map[string]interface{}) {
			sum += traverse(v)
		}
		for _, v := range node.(map[string]interface{}) {
			if v == "red" {
				return 0
			}
		}
		return sum
	case float64:
		return int(node.(float64))
	default:
		return 0
	}
}

func (Solution) Day12Part2(fn string) int {
	s := toString(fn)
	var result interface{}
	json.Unmarshal([]byte(s), &result)
	return traverse(result)
}
