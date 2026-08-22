def part1():
    grp_name = input('Please enter a group name: ')
    match_nber = input('Please enter match number: ')
    hme_tm_name = input('Please enter the name of the home team: ')
    away_tm_name = input('Please enter the name of the away team: ')
    hme_tm_goal = int(input('Please enter the goals by the home team: '))
    away_tm_goal = int(input('Please enter the goals by the away team: '))

    print('Group Name:', grp_name)
    print('Match Number:', match_nber)
    print('Home Team:', hme_tm_name)
    print('Away Team:', away_tm_name)
    print('Home Team Goals:', hme_tm_goal)
    print('Away Team Goals:', away_tm_goal)
    #instead of user input, the program will automatically generate the winner of the match based on the goals scored by each team and compare the goals scored by the home team and the away team and determine the winner accordingly.
    if hme_tm_goal > away_tm_goal:
        print('Winner of Match', match_nber, 'is:', hme_tm_name)
    elif away_tm_goal > hme_tm_goal:
        print('Winner of Match', match_nber, 'is:', away_tm_name)
    else:
        print('Match', match_nber, 'ended in a draw.')

    #dictionaries holding each team's stats
    home_row = {'Group': grp_name, 'Team': hme_tm_name, 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    away_row = {'Group': grp_name, 'Team': away_tm_name, 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}

    #updates a single team's row with the result of one match (MP, W/D/L, GF, GA, GD, Pts)
    def stats(row, GF, GA):
        row['MP'] += 1
        row['GF'] += GF
        row['GA'] += GA
        row['GD'] = row['GF'] - row['GA']
        if GF > GA:
            row['W'] += 1
            row['Pts'] += 3
        elif GF < GA:
            row['L'] += 1
        else:
            row['D'] += 1
        row['Pts'] = row['W'] * 3 + row['D']

    #apply this match's result to both teams
    stats(home_row, hme_tm_goal, away_tm_goal)
    stats(away_row, away_tm_goal, hme_tm_goal)

    #print the group table with fixed-width columns
    print(f"\nGroup: {grp_name}")
    print(f"{'Team':<15}{'MP':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>4}{'GA':>4}{'GD':>5}{'Pts':>5}")
    print(f"{home_row['Team']:<15}{home_row['MP']:>4}{home_row['W']:>4}{home_row['D']:>4}"
          f"{home_row['L']:>4}{home_row['GF']:>4}{home_row['GA']:>4}{home_row['GD']:>5}{home_row['Pts']:>5}")
    print(f"{away_row['Team']:<15}{away_row['MP']:>4}{away_row['W']:>4}{away_row['D']:>4}"
          f"{away_row['L']:>4}{away_row['GF']:>4}{away_row['GA']:>4}{away_row['GD']:>5}{away_row['Pts']:>5}")

def part2():
    #holds every group's teams so it can be read by other menu options later
    group_records = {}
    #holds every scheduled match across all groups
    matches = []
    def create_group_tournaments():
        total_teams = int(input('\nPlease enter the total number of teams participating in the tournament: '))
        #Validation for number of teams: divisible by 4
        if total_teams % 4 != 0:
            print('The total number of teams must be a multiple of 4.')
            return
        total_groups = total_teams // 4
        print('Total number of groups:', total_groups)
        for i in range(total_groups):
            print(f'\n Group {i+1} of {total_groups}')
            group_name = input(f'\nPlease enter the name of group {i+1}: ')
            print(f'\nYou will now enter the names of the 4 teams in group {group_name}.')
            #empty list to hold the teams in this group
            teams = []
            for t in range(4):
                team_name = input(f'Please enter the name of team {t+1} in group {group_name}: ')
                #creates the team record dictionary and appends it to the teams list
                team_record = {'Group': group_name, 'Team': team_name, 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
                teams.append(team_record)
            #add the group and its teams to the group records dictionary
            group_records[group_name] = teams
    #displays every group with its 4 teams, plus totals for groups and teams
    def view_group_tournament():
        #Check if any groups have been created yet
        if group_records == {}:
            print('\nNo groups have been created yet.')
            return
        print('\nTournament Overview:')
        #Print each group and its teams, and count the total number of teams
        total_teams = 0
        for group_name, teams in group_records.items():
            print(f'\n{group_name}:')
            #list every team in this group
            for team in teams:
                print(' -', team['Team'])
            #add this group's team count to the running total
            total_teams += len(teams)
        print(f'\nTotal number of groups: {len(group_records)}')
        print(f'Total number of teams: {total_teams}')
        
    #schedules round-robin matches (every team plays every other team once) for a chosen group
    def create_group_matches():
        while True:
            group_name = input('\nPlease enter the name of the group to create matches for: ')
            #Ensure that the group actually exists before scheduling matches for it
            if group_records.get(group_name) is None:
                print('That group does not exist. Please create it first.')
            else:
                print(f'\nGenerating matches for {group_name}:')
                for i in range(4):
                    #pair team i with every team that comes after it in the list so that each pair only appears once
                    for j in range(i + 1, 4):
                        match_id = len(matches) + 1
                        home_team = group_records[group_name][i]['Team']
                        away_team = group_records[group_name][j]['Team']
                        match_record = {'MatchID': match_id, 'Group': group_name, 'Home': home_team, 'Away': away_team}
                        matches.append(match_record)
                        print(f"Match {match_id}: {home_team} vs {away_team}")
            #Ask the user if they want to create matches for another group
            again = input('\nCreate matches for another group? (yes/no): ')
            if again.lower() == 'no':
                break
            if again.lower() != 'yes' and again.lower() != 'no':
                print('Invalid input. Please enter "yes" or "no".')
                continue

    #displays every scheduled match (ID, home team, away team) for one chosen group
    def view_group_matches():
        chosen_group = input('\nPlease enter the group name to view matches for: ')
        #Check if the group exists
        if chosen_group in group_records:
            group_matches = []
            #Filter the matches list to only include matches for the chosen group
            for match in matches:
                if match['Group'] == chosen_group:
                    group_matches.append(match)
            #Display the matches for the chosen group, or indicate that no matches were found
            if len(group_matches) > 0:
                print(f'\nMatches for {chosen_group}:')
                for match in group_matches:
                    print(f"Match {match['MatchID']}: {match['Home']} vs {match['Away']}")
            else:
                print(f'\nNo matches found for {chosen_group}.')
        else:
            print('That group does not exist.')

    #While True: keep showing the menu and running the chosen action until the user picks 8 (Exit)
    while True:
        print('\nWelcome to the Football Tournament Group Stage Manager!')
        print('\nMenu')
        print('1. Create group tournaments')
        print('2. View a group tournament')
        print('3. Create group matches')
        print('4. View group matches')
        print('5. Record match scores')
        print('6. View group tables')
        print('7. Determine winners')
        print('8. Exit')
        #Get the user's choice and call the appropriate function
        choice = input('\nEnter your choice: ')
        if choice == '1':
            create_group_tournaments()
        elif choice == '2':
            view_group_tournament()
        elif choice == '3':
            create_group_matches()
        elif choice == '4':
            view_group_matches()
        elif choice == '5':
            print('Not implemented yet.')
        elif choice == '6':
            print('Not implemented yet.')
        elif choice == '7':
            print('Not implemented yet.')
        elif choice == '8':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number from 1 to 8.')
        #prompt the user to press Enter to return to the menu, and print a separator line for clarity
        print('\n' + '=' * 40)
        input('Press Enter to return to the menu...')
#menu to choose which part to run
choice = input('Which part do you want to run? (1 or 2): ')
if choice == '1':
    part1()
elif choice == '2':
    part2()
else:
    print('Invalid choice.')