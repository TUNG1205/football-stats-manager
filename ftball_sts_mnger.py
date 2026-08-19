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
#list that will hold one dictionary (row) per team, storing their accumulated stats
stats = []
#looks up a team's existing row in stats, or creates a new one if this is their first match
def exstnce_check(stats,group,team):
    for row in stats:
        if row['Group'] == group and row['Team'] == team:
            return row
    new_stat = {'Group': group, 'Team': team, 'MP': 0, 'W': 0, 'D': 0,'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    stats.append(new_stat)
    return new_stat
#get (or create) each team's row so their stats can be updated below
home_row = exstnce_check(stats, grp_name, hme_tm_name)
away_row = exstnce_check(stats, grp_name, away_tm_name)
#updates a single team's row with the result of one match (MP, W/D/L, GF, GA, GD, Pts)
def update_stats(row,GF,GA):
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
#apply this match's result to both teams (goals are swapped so each team's GF/GA is correct from their own side)
update_stats(home_row, hme_tm_goal, away_tm_goal)
update_stats(away_row, away_tm_goal, hme_tm_goal)
#print the group table with fixed-width columns so the stats line up neatly
print(f"\nGroup: {grp_name}")
print(f"{'Team':<15}{'MP':>4}{'W':>4}{'D':>4}{'L':>4}{'GF':>4}{'GA':>4}{'GD':>5}{'Pts':>5}")
for row in stats:
    if row['Group'] == grp_name:
        print(f"{row['Team']:<15}{row['MP']:>4}{row['W']:>4}{row['D']:>4}"
              f"{row['L']:>4}{row['GF']:>4}{row['GA']:>4}{row['GD']:>5}{row['Pts']:>5}")