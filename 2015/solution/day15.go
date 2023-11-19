package solution

import (
	"regexp"
	"strconv"
	"strings"
)

func (Solution) Day15Part1(fn string) int {
	lines := toLines(fn)
	m := make(map[string][]int)
	n := []string{"Sprinkles", "PeanutButter", "Frosting", "Sugar"}

	for _, line := range lines {
		// Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
		name := strings.Split(line, ":")[0]
		re := regexp.MustCompile(`-?\d+`)
		numberStrings := re.FindAllString(line, -1)
		m[name] = []int{}
		for _, numberString := range numberStrings {
			val, _ := strconv.Atoi(numberString)
			m[name] = append(m[name], val)
		}
	}

	maxScore := 0

	var walk func(recipe []int, idx int, remains int)
	walk = func(recipe []int, idx int, remains int) {
		if idx == len(recipe) {
			var capacity, durability, flavor, texture int
			for i := 0; i < len(recipe); i++ {
				capacity += recipe[i] * m[n[i]][0]
				durability += recipe[i] * m[n[i]][1]
				flavor += recipe[i] * m[n[i]][2]
				texture += recipe[i] * m[n[i]][3]
			}
			capacity = max(0, capacity)
			durability = max(0, durability)
			flavor = max(0, flavor)
			texture = max(0, texture)

			maxScore = max(maxScore, capacity*durability*flavor*texture)
		} else if idx == len(recipe)-1 {
			recipe[idx] = remains
			walk(recipe, idx+1, 0)
		} else {
			for i := 0; i <= remains; i++ {
				recipe[idx] = i
				walk(recipe, idx+1, remains-i)
			}
		}
	}
	recipe := make([]int, len(n))
	walk(recipe, 0, 100)

	return maxScore
}

func (Solution) Day15Part2(fn string) int {
	lines := toLines(fn)
	m := make(map[string][]int)
	n := []string{"Sprinkles", "PeanutButter", "Frosting", "Sugar"}

	for _, line := range lines {
		// Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
		name := strings.Split(line, ":")[0]
		re := regexp.MustCompile(`-?\d+`)
		numberStrings := re.FindAllString(line, -1)
		m[name] = []int{}
		for _, numberString := range numberStrings {
			val, _ := strconv.Atoi(numberString)
			m[name] = append(m[name], val)
		}
	}

	maxScore := 0

	var walk func(recipe []int, idx int, remains int)
	walk = func(recipe []int, idx int, remains int) {
		if idx == len(recipe) {
			var capacity, durability, flavor, texture, calories int
			for i := 0; i < len(recipe); i++ {
				capacity += recipe[i] * m[n[i]][0]
				durability += recipe[i] * m[n[i]][1]
				flavor += recipe[i] * m[n[i]][2]
				texture += recipe[i] * m[n[i]][3]
				calories += recipe[i] * m[n[i]][4]
			}
			capacity = max(0, capacity)
			durability = max(0, durability)
			flavor = max(0, flavor)
			texture = max(0, texture)
			if calories == 500 {
				maxScore = max(maxScore, capacity*durability*flavor*texture)
			}

		} else if idx == len(recipe)-1 {
			recipe[idx] = remains
			walk(recipe, idx+1, 0)
		} else {
			for i := 0; i <= remains; i++ {
				recipe[idx] = i
				walk(recipe, idx+1, remains-i)
			}
		}
	}
	recipe := make([]int, len(n))
	walk(recipe, 0, 100)

	return maxScore
}
