#Part 1
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
def stats(row,GF,GA):
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

#print the group table with fixed-width columns so the stats line up neatly
print(f"\nGroup: {grp_name}")
print(f"{'Team':<15}{'MP':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>4}{'GA':>4}{'GD':>5}{'Pts':>5}")
print(f"{home_row['Team']:<15}{home_row['MP']:>4}{home_row['W']:>4}{home_row['D']:>4}"
      f"{home_row['L']:>4}{home_row['GF']:>4}{home_row['GA']:>4}{home_row['GD']:>5}{home_row['Pts']:>5}")
print(f"{away_row['Team']:<15}{away_row['MP']:>4}{away_row['W']:>4}{away_row['D']:>4}"
      f"{away_row['L']:>4}{away_row['GF']:>4}{away_row['GA']:>4}{away_row['GD']:>5}{away_row['Pts']:>5}")

#Part 2
