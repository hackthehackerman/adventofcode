package solution

import "fmt"

func (Solution) Day13Part1(fn string) int {
	lines := toLines(fn)

	happiness := make(map[string]map[string]int)
	for _, line := range lines {
		var name1, name2, gainlose string
		var amount int
		fmt.Sscanf(line, "%s would %s %d happiness units by sitting next to %s.", &name1, &gainlose, &amount, &name2)
		name2 = name2[:len(name2)-1]
		if gainlose == "lose" {
			amount = -amount
		}
		if happiness[name1] == nil {
			happiness[name1] = make(map[string]int)
		}
		happiness[name1][name2] = amount
	}

	names := make([]string, 0)
	for name := range happiness {
		names = append(names, name)
	}

	// Find all permutations
	perms := permutationsString(names)
	max := 0
	for _, perm := range perms {
		sum := 0
		for i := 0; i < len(perm); i++ {
			sum += happiness[perm[i]][perm[(i+1)%len(perm)]] + happiness[perm[(i+1)%len(perm)]][perm[i]]
		}
		if sum > max {
			max = sum
		}
	}
	return max
}

func (Solution) Day13Part2(fn string) int {
	lines := toLines(fn)

	happiness := make(map[string]map[string]int)
	for _, line := range lines {
		var name1, name2, gainlose string
		var amount int
		fmt.Sscanf(line, "%s would %s %d happiness units by sitting next to %s.", &name1, &gainlose, &amount, &name2)
		name2 = name2[:len(name2)-1]
		if gainlose == "lose" {
			amount = -amount
		}
		if happiness[name1] == nil {
			happiness[name1] = make(map[string]int)
		}
		happiness[name1][name2] = amount
	}

	names := make([]string, 0)
	for name := range happiness {
		names = append(names, name)
	}
	happiness["Me"] = make(map[string]int)
	for _, name := range names {
		happiness[name]["Me"] = 0
		happiness["Me"][name] = 0
	}
	names = append(names, "Me")

	// Find all permutations
	perms := permutationsString(names)
	max := 0
	for _, perm := range perms {
		sum := 0
		for i := 0; i < len(perm); i++ {
			sum += happiness[perm[i]][perm[(i+1)%len(perm)]] + happiness[perm[(i+1)%len(perm)]][perm[i]]
		}
		if sum > max {
			max = sum
		}
	}
	return max
}
