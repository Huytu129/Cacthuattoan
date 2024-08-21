def stable_marriage(men_preferences, women_preferences):
    n = len(men_preferences)

    free_men = list(men_preferences.keys())
    engaged = {}
    women_partner = {woman: None for woman in women_preferences}

    while free_men:
        man = free_men[0]
        man_preferences = men_preferences[man]

        for woman in man_preferences:
            if women_partner[woman] is None:
                engaged[man] = woman
                women_partner[woman] = man
                free_men.remove(man)
                break
            else:
                current_partner = women_partner[woman]
                woman_preferences_list = women_preferences[woman]
                if woman_preferences_list.index(man) < woman_preferences_list.index(current_partner):
                    free_men.append(current_partner)
                    engaged[man] = woman
                    women_partner[woman] = man
                    free_men.remove(man)
                    break

    return engaged


# Example usage:
men_preferences = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['X', 'Z', 'Y']
}

women_preferences = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['B', 'C', 'A']
}

engaged = stable_marriage(men_preferences, women_preferences)
print(f"Engaged pairs: {engaged}")
