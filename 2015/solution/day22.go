package solution

import (
	"math"
	"strconv"
	"strings"
)

type spell struct {
	name   string
	cost   int
	damage int
	heal   int
	effect string
}

type battleState struct {
	player     character
	boss       character
	mana       int
	mana_spent int
	turn       int
	shield     int
	poison     int
	recharge   int
}

func (Solution) Day22Part1(fn string) int {
	lines := toLines(fn)
	hp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	damage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])

	boss := character{hp, damage, 0}

	spells := []spell{
		{"Magic Missile", 53, 4, 0, ""},
		{"Drain", 73, 2, 2, ""},
		{"Shield", 113, 0, 0, "Shield"},
		{"Poison", 173, 0, 0, "Poison"},
		{"Recharge", 229, 0, 0, "Recharge"},
	}

	fight := func(state battleState, spell spell) (newState battleState, player_won bool, boss_won bool, invalid_move bool) {
		// fmt.Println("-- player turn -- ", state.turn)
		// fmt.Println("- Player has", state.player.hp, "hp,", state.player.armor, "armor,", state.mana, "mana")
		// fmt.Println("- Boss has", state.boss.hp, "hp")
		// fmt.Println("timer: ", state.shield, state.poison, state.recharge)

		newState = state
		newState.turn++
		newState.player.armor = 0
		// spell tick
		if newState.shield > 0 {
			newState.player.armor = 7
			newState.shield--
		}
		if newState.poison > 0 {
			newState.boss.hp -= 3
			newState.poison--
		}
		if newState.recharge > 0 {
			newState.mana += 101
			newState.recharge--
		}

		// boss died from poison
		if newState.boss.hp <= 0 {
			return newState, true, false, false
		}

		if state.turn%2 == 0 {
			// player
			// check for invalid spells
			if spell.name == "Shield" && newState.shield > 0 {
				return newState, false, false, true
			} else if spell.name == "Poison" && newState.poison > 0 {
				return newState, false, false, true
			} else if spell.name == "Recharge" && newState.recharge > 0 {
				return newState, false, false, true
			}
			if spell.cost > newState.mana {
				return newState, false, false, true
			}

			// cast spell
			newState.mana_spent += spell.cost
			newState.mana -= spell.cost
			newState.boss.hp -= spell.damage
			newState.player.hp += spell.heal
			if spell.effect == "Poison" {
				newState.poison = 6
			} else if spell.effect == "Recharge" {
				newState.recharge = 5
			} else if spell.effect == "Shield" {
				newState.shield = 6
			}
			// check if boss is dead
			if newState.boss.hp <= 0 {
				return newState, true, false, false
			} else {
				return newState, false, false, false
			}

		} else {
			// boss
			newState.player.hp -= max(1, newState.boss.dmg-newState.player.armor)
			if newState.player.hp <= 0 {
				return newState, false, true, false
			} else {
				return newState, false, false, false
			}
		}

	}

	var least_mana_spent func(state battleState) int
	min_mana := math.MaxInt
	least_mana_spent = func(state battleState) int {
		if state.mana_spent >= min_mana {
			return math.MaxInt
		}
		if state.turn%2 == 0 {
			// player turn
			for _, spell := range spells {
				newState, player_won, boss_won, invalid_move := fight(state, spell)
				if invalid_move {
					continue
				}
				if player_won {
					min_mana = min(min_mana, newState.mana_spent)
				} else if boss_won {
					// no-op
				} else {
					min_mana = min(min_mana, least_mana_spent(newState))
				}
			}
		} else {
			// boss turn
			newState, player_won, boss_won, _ := fight(state, spell{})
			if boss_won {
				return math.MaxInt
			} else if player_won {
				min_mana = min(min_mana, newState.mana_spent)
			} else {
				min_mana = min(min_mana, least_mana_spent(newState))
			}
		}
		return min_mana
	}

	state := battleState{character{50, 0, 0}, boss, 500, 0, 0, 0, 0, 0}
	return least_mana_spent(state)
}

func (Solution) Day22Part2(fn string) int {
	lines := toLines(fn)
	hp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	damage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])

	boss := character{hp, damage, 0}

	spells := []spell{
		{"Magic Missile", 53, 4, 0, ""},
		{"Drain", 73, 2, 2, ""},
		{"Shield", 113, 0, 0, "Shield"},
		{"Poison", 173, 0, 0, "Poison"},
		{"Recharge", 229, 0, 0, "Recharge"},
	}

	fight := func(state battleState, spell spell) (newState battleState, player_won bool, boss_won bool, invalid_move bool) {
		// fmt.Println("-- player turn -- ", state.turn)
		// fmt.Println("- Player has", state.player.hp, "hp,", state.player.armor, "armor,", state.mana, "mana")
		// fmt.Println("- Boss has", state.boss.hp, "hp")
		// fmt.Println("timer: ", state.shield, state.poison, state.recharge)

		newState = state
		newState.turn++
		newState.player.armor = 0

		if state.turn%2 == 0 {
			// hard mode
			newState.player.hp--
			if newState.player.hp <= 0 {
				return newState, false, true, false
			}
		}

		// spell tick
		if newState.shield > 0 {
			newState.player.armor = 7
			newState.shield--
		}
		if newState.poison > 0 {
			newState.boss.hp -= 3
			newState.poison--
		}
		if newState.recharge > 0 {
			newState.mana += 101
			newState.recharge--
		}

		// boss died from poison
		if newState.boss.hp <= 0 {
			return newState, true, false, false
		}

		if state.turn%2 == 0 {
			// player
			// check for invalid spells
			if spell.name == "Shield" && newState.shield > 0 {
				return newState, false, false, true
			} else if spell.name == "Poison" && newState.poison > 0 {
				return newState, false, false, true
			} else if spell.name == "Recharge" && newState.recharge > 0 {
				return newState, false, false, true
			}
			if spell.cost > newState.mana {
				return newState, false, false, true
			}

			// cast spell
			newState.mana_spent += spell.cost
			newState.mana -= spell.cost
			newState.boss.hp -= spell.damage
			newState.player.hp += spell.heal
			if spell.effect == "Poison" {
				newState.poison = 6
			} else if spell.effect == "Recharge" {
				newState.recharge = 5
			} else if spell.effect == "Shield" {
				newState.shield = 6
			}
			// check if boss is dead
			if newState.boss.hp <= 0 {
				return newState, true, false, false
			} else {
				return newState, false, false, false
			}

		} else {
			// boss
			newState.player.hp -= max(1, newState.boss.dmg-newState.player.armor)
			if newState.player.hp <= 0 {
				return newState, false, true, false
			} else {
				return newState, false, false, false
			}
		}

	}

	var least_mana_spent func(state battleState) int
	min_mana := math.MaxInt
	least_mana_spent = func(state battleState) int {
		if state.mana_spent >= min_mana {
			return math.MaxInt
		}
		if state.turn%2 == 0 {
			// player turn
			for _, spell := range spells {
				newState, player_won, boss_won, invalid_move := fight(state, spell)
				if invalid_move {
					continue
				}
				if player_won {
					min_mana = min(min_mana, newState.mana_spent)
				} else if boss_won {
					// no-op
				} else {
					min_mana = min(min_mana, least_mana_spent(newState))
				}
			}
		} else {
			// boss turn
			newState, player_won, boss_won, _ := fight(state, spell{})
			if boss_won {
				return math.MaxInt
			} else if player_won {
				min_mana = min(min_mana, newState.mana_spent)
			} else {
				min_mana = min(min_mana, least_mana_spent(newState))
			}
		}
		return min_mana
	}

	state := battleState{character{50, 0, 0}, boss, 500, 0, 0, 0, 0, 0}
	return least_mana_spent(state)
}
