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
    #Check for a valid whole number, then returns it as an int
    def check_whole_number(number):
        while True:
            value = input(number)
            if value.isdigit():
                return int(value)
            else:
                print('Please enter a whole, non-negative number.')
    #checks whether any character in the given text is a digit
    def contains_number(text):
        has_number = False
        for char in text:
            if char.isdigit():
                has_number = True
        return has_number
    #sort keys shared by view_group_tables and determine_winners
    def sort_items(team):
        return (team['Pts'], team['GD'], team['GF'])
    def create_group_tournaments():
        #Check if the total is a whole number but also must be a multiple of 4
        valid_total = False
        while valid_total == False:
            total_teams = check_whole_number('\nPlease enter the total number of teams participating in the tournament: ')
            if total_teams % 4 == 0:
                valid_total = True
            else:
                print('The total number of teams must be a multiple of 4.')
        total_groups = total_teams // 4
        print('Total number of groups:', total_groups)
        for i in range(total_groups):
            print(f'\n Group {i+1} of {total_groups}')
            group_name = input(f'\nPlease enter the name of group {i+1}: ')
            print(f'\nYou will now enter the names of the 4 teams in group {group_name}.')
            #empty list to hold the teams in this group
            teams = []
            for t in range(4):
                #check whether the team name contains no numbers
                valid_name = False
                while valid_name == False:
                    team_name = input(f'Please enter the name of team {t+1} in group {group_name}: ')
                    if contains_number(team_name):
                        print('Team names cannot contain numbers. Please try again.')
                    else:
                        valid_name = True
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
    #schedules round-robin matches for a chosen group
    def create_group_matches():
        creating = True
        while creating:
            group_name = input('\nPlease enter the name of the group to create matches for: ')
            #Ensure that the group actually exists before scheduling matches for it
            if group_records.get(group_name) is None:
                print('That group does not exist. Please create it first.')
            else:
                #check whether this group's matches have already been generated
                exist_matches = False
                for match in matches:
                    if match['Group'] == group_name:
                        exist_matches = True
                if exist_matches:
                    print(f'Matches for {group_name} have already been created.')
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
            again = input('\nCreate matches for another group? (yes/no): ')
            if again.lower() == 'no':
                creating = False
            elif again.lower() != 'yes':
                print('Invalid input. Please enter "yes" or "no".')
    #displays every scheduled match for one chosen group
    def view_group_matches():
        group = input('\nPlease enter the group name to view matches for: ')
        #Check if the group exists
        if group in group_records:
            group_matches = []
            #Filter the matches list to only include matches for the chosen group
            for match in matches:
                if match['Group'] == group:
                    group_matches.append(match)
            #Display the matches for the chosen group, or indicate that no matches were found
            if len(group_matches) > 0:
                print(f'\nMatches for {group}:')
                for match in group_matches:
                    print(f"Match {match['MatchID']}: {match['Home']} vs {match['Away']}")
            else:
                print(f'\nNo matches found for {group}.')
        else:
            print('That group does not exist.')
    #updates a single team's row with the result of one match 
    def calculate_points_and_stats(team_record, GF, GA):
        team_record['MP'] += 1
        team_record['GF'] += GF
        team_record['GA'] += GA
        team_record['GD'] = team_record['GF'] - team_record['GA']
        if GF > GA:
            team_record['W'] += 1
            team_record['Pts'] += 3
        elif GF < GA:
            team_record['L'] += 1
        else:
            team_record['D'] += 1
        team_record['Pts'] = team_record['W'] * 3 + team_record['D']
    def record_match_scores():
        #Stop here if no groups exist yet
        if group_records == {}:
            print('\nNo groups have been created yet. Please create a group first.')
            return
        #users can keep
        select_groups = True
        while select_groups:
            #looks for a group name until it exists and has at least one match to record
            ready_group = False
            while ready_group == False:
                group = input('\nPlease enter the group name to record match scores for: ')
                if group not in group_records:
                    print('That group does not exist, please enter a valid group name.')
                else:
                    #Filter the matches list down to just this group's matches
                    group_matches = []
                    for match in matches:
                        if match['Group'] == group:
                            group_matches.append(match)
                    if len(group_matches) == 0:
                        print(f'No matches have been created for {group} yet. Please choose a different group.')
                    else:
                        ready_group = True
            #Show the group's matches so the user knows which IDs are valid to pick from
            print(f'\nMatches for {group}:')
            for match in group_matches:
                print(f"Match {match['MatchID']}: {match['Home']} vs {match['Away']}")
            #Keep recording match scores for this group until the user decides to exist
            record = True
            while record:
                match_id = int(input('\nPlease enter the match ID to record scores for: '))
                #Find the chosen match, but only search within this group's matches
                match_found = False
                for match in group_matches:
                    if match['MatchID'] == match_id:
                        selected_match = match
                        match_found = True
                if match_found == False:
                    print('That match ID does not belong to this group. Please choose a valid match ID.')
                else:
                    #Prompt the user to enter the goals scored by each team in the selected match
                    home_goals = check_whole_number(f"Enter goals scored by {selected_match['Home']}: ")
                    away_goals = check_whole_number(f"Enter goals scored by {selected_match['Away']}: ")
                    #Update the stats for both teams in this group's table
                    for team_record in group_records[group]:
                        #Check if this team is the home or away team in the selected match and update its stats accordingly
                        if team_record['Team'] == selected_match['Home']:
                            calculate_points_and_stats(team_record, home_goals, away_goals)
                        elif team_record['Team'] == selected_match['Away']:
                            calculate_points_and_stats(team_record, away_goals, home_goals)
                    #print the match summary
                    print('\nGroup Name:', selected_match['Group'])
                    print('Match Number:', selected_match['MatchID'])
                    print('Home Team:', selected_match['Home'])
                    print('Away Team:', selected_match['Away'])
                    print('Home Team Goals:', home_goals)
                    print('Away Team Goals:', away_goals)
                    if home_goals > away_goals:
                        print('Winner of Match', selected_match['MatchID'], 'is:', selected_match['Home'])
                    elif away_goals > home_goals:
                        print('Winner of Match', selected_match['MatchID'], 'is:', selected_match['Away'])
                    else:
                        print('Match', selected_match['MatchID'], 'ended in a draw.')
                    #Ask the user if they want to record another match score for this group, and validate the input
                    again = input(f'\nRecord another match score for {group}? (yes/no): ')
                    if again.lower() == 'no':
                        record = False
                    elif again.lower() != 'yes':
                        print('Invalid input. Please enter "yes" or "no".')
            #Ask if the user wants to record match scores for a different group, or return to the menu
            another_group = input('\nRecord match scores for another group? (yes/no): ')
            if another_group.lower() == 'no':
                select_groups = False
            elif another_group.lower() != 'yes':
                print('Invalid input. Please enter "yes" or "no".')
    #displays a group's table, sorted in decending order to rank the teams
    def view_group_tables():
        #Stop here if no groups exist yet, so the group-name prompt below can't loop forever
        if group_records == {}:
            print('\nNo groups have been created yet. Please create a group first.')
            return
        #Keep asking for a group name until it exists
        valid_group = False
        while valid_group == False:
            group = input('\nPlease enter the group name to view the table for: ')
            if group in group_records:
                valid_group = True
            else:
                print('That group does not exist, please enter a valid group name.')
        
        #Python's built-in sorted(): Investigated through Val
        #group_records[group]:list of team dicts for the chosen group(the data being sorted)
        #key=sort_items: Keys used to compare teams(Pts, GD, GF) 
        #reverse=True: sorts that tuple highest to lowest
        sorted_teams = sorted(group_records[group], key=sort_items, reverse=True)
        #print the sorted group table with fixed-width columns
        print(f'\nGroup: {group}')
        print(f"{'Team':<15}{'MP':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>4}{'GA':>4}{'GD':>5}{'Pts':>5}")
        for team in sorted_teams:
            print(f"{team['Team']:<15}{team['MP']:>4}{team['W']:>4}{team['D']:>4}"
                  f"{team['L']:>4}{team['GF']:>4}{team['GA']:>4}{team['GD']:>5}{team['Pts']:>5}")
    #determines the top 2 teams from each completed group and lists them all as knockout-stage qualifiers
    def determine_winners():
        #Check if there's any groups already first.
        if group_records == {}:
            print('\nNo groups have been created yet.')
            return
        #collects every qualifying team's name across all groups, for the final combined list
        qualified_teams = []
        #pick each key value from the dictionary group_records 
        for group_name, teams in group_records.items():
            #a group is only complete once every team has played all 3 of its round-robin matches
            complete = True
            for team in teams:
                if team['MP'] < 3:
                    complete = False
            if complete:
                #rank this group's teams (Pts, then GD, then GF, highest first) so the top 2 can be picked out
                ranked = sorted(teams, key=sort_items, reverse=True)
                #the top 2 ranked teams advance to the knockout stage
                top_two = ranked[0:2]
                print(f'\n{group_name} winners (advancing to the knockout stage):')
                for team in top_two:
                    print(f" - {team['Team']} (Pts: {team['Pts']}, GD: {team['GD']}, GF: {team['GF']})")
                    qualified_teams.append(team['Team'])
            else:
                print(f'\n{group_name}: matches are still in progress, cannot determine winners yet.')
        #Show the combined list
        if len(qualified_teams) > 0:
            print('\nAll teams qualifying for the knockout stage:')
            for team_name in qualified_teams:
                print('-', team_name)
    #keep showing the menu and running the chosen action until the user exits
    running = True
    while running:
        print('\nWelcome to the Football Tournament Group Stage Manager!')
        print('\nMenu')
        print('1. Create group tournaments')
        print('2. View group tournament')
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
            record_match_scores()
        elif choice == '6':
            view_group_tables()
        elif choice == '7':
            determine_winners()
        elif choice == '8':
            print('Goodbye!')
            running = False
        else:
            print('Invalid choice. Please enter a number from 1 to 8.')
if __name__ == "__main__":
    part1()
    part2()
#Reference: github: 