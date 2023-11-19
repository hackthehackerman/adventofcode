package solution

import (
	"math"
	"strconv"
	"strings"
)

type item struct {
	name   string
	cost   int
	damage int
	armor  int
}

type character struct {
	hp    int
	dmg   int
	armor int
}

func (Solution) Day21Part1(fn string) int {
	lines := toLines(fn)
	hp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	damage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])
	armor, _ := strconv.Atoi(strings.Split(lines[2], ": ")[1])

	boss := character{hp, damage, armor}

	weapons := []item{
		{"Dagger", 8, 4, 0},
		{"Shortsword", 10, 5, 0},
		{"Warhammer", 25, 6, 0},
		{"Longsword", 40, 7, 0},
		{"Greataxe", 74, 8, 0},
	}

	armors := []item{
		{"Leather", 13, 0, 1},
		{"Chainmail", 31, 0, 2},
		{"Splintmail", 53, 0, 3},
		{"Bandedmail", 75, 0, 4},
		{"Platemail", 102, 0, 5},
	}

	rings := []item{
		{"Damage +1", 25, 1, 0},
		{"Damage +2", 50, 2, 0},
		{"Damage +3", 100, 3, 0},
		{"Defense +1", 20, 0, 1},
		{"Defense +2", 40, 0, 2},
		{"Defense +3", 80, 0, 3},
	}

	fight := func(player, boss character) bool {
		for {
			boss.hp -= max(player.dmg-boss.armor, 1)
			if boss.hp <= 0 {
				return true
			}
			player.hp -= max(boss.dmg-player.armor, 1)
			if player.hp <= 0 {
				return false
			}
		}
	}

	minCost := math.MaxInt
	for w := 0; w < len(weapons); w++ {
		for a := -1; a < len(armors); a++ {
			for r1 := -1; r1 < len(rings); r1++ {
				for r2 := -1; r2 < len(rings); r2++ {
					if r1 == r2 && r1 >= 0 {
						continue
					}
					var price, damage, armor int
					price += weapons[w].cost
					damage += weapons[w].damage
					if a >= 0 {
						price += armors[a].cost
						armor += armors[a].armor
					}
					if r1 >= 0 {
						price += rings[r1].cost
						damage += rings[r1].damage
						armor += rings[r1].armor
					}
					if r2 >= 0 {
						price += rings[r2].cost
						damage += rings[r2].damage
						armor += rings[r2].armor
					}
					player := character{100, damage, armor}
					if fight(player, boss) {
						minCost = min(minCost, price)
					}
				}
			}
		}
	}

	return minCost
}

func (Solution) Day21Part2(fn string) int {
	lines := toLines(fn)
	hp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	damage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])
	armor, _ := strconv.Atoi(strings.Split(lines[2], ": ")[1])

	boss := character{hp, damage, armor}

	weapons := []item{
		{"Dagger", 8, 4, 0},
		{"Shortsword", 10, 5, 0},
		{"Warhammer", 25, 6, 0},
		{"Longsword", 40, 7, 0},
		{"Greataxe", 74, 8, 0},
	}

	armors := []item{
		{"Leather", 13, 0, 1},
		{"Chainmail", 31, 0, 2},
		{"Splintmail", 53, 0, 3},
		{"Bandedmail", 75, 0, 4},
		{"Platemail", 102, 0, 5},
	}

	rings := []item{
		{"Damage +1", 25, 1, 0},
		{"Damage +2", 50, 2, 0},
		{"Damage +3", 100, 3, 0},
		{"Defense +1", 20, 0, 1},
		{"Defense +2", 40, 0, 2},
		{"Defense +3", 80, 0, 3},
	}

	fight := func(player, boss character) bool {
		for {
			boss.hp -= max(player.dmg-boss.armor, 1)
			if boss.hp <= 0 {
				return true
			}
			player.hp -= max(boss.dmg-player.armor, 1)
			if player.hp <= 0 {
				return false
			}
		}
	}

	maxCost := 0
	for w := 0; w < len(weapons); w++ {
		for a := -1; a < len(armors); a++ {
			for r1 := -1; r1 < len(rings); r1++ {
				for r2 := -1; r2 < len(rings); r2++ {
					if r1 == r2 && r1 >= 0 {
						continue
					}
					var price, damage, armor int
					price += weapons[w].cost
					damage += weapons[w].damage
					if a >= 0 {
						price += armors[a].cost
						armor += armors[a].armor
					}
					if r1 >= 0 {
						price += rings[r1].cost
						damage += rings[r1].damage
						armor += rings[r1].armor
					}
					if r2 >= 0 {
						price += rings[r2].cost
						damage += rings[r2].damage
						armor += rings[r2].armor
					}
					player := character{100, damage, armor}
					if !fight(player, boss) {
						maxCost = max(maxCost, price)
					}

				}
			}
		}
	}

	return maxCost
}
