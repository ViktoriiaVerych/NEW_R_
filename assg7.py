import argparse
import sys
parser = argparse.ArgumentParser(description="our example parser.")
args = parser.parse_args()



#task3
def overall(overall_dict):
    with open(args.filename, "r") as file:
        next_line = file.readline()
        while next_line != '\t':
            next_line = file.readline()
            olympic_info = next_line.split('\t')
            for i in overall_dict:
                if next_line != '\t':
                    if i == olympic_info[6] and olympic_info[14] != 'NA':
                        overall_dict[i] = overall_dict[i] + olympic_info[9] + ';'
        for i in overall_dict:
            year_max = 0
            medals_count = 0
            years = overall_dict[i].split(';')
            for j in range(1910,2023):
                if years.count(str(j)) > medals_count:
                    medals_count = years.count(str(j))
                    year_max = j
            print(i,year_max, medals_count)
    return overall_dict

def interactive():
    country = input('Enter country or code: ')
    first_game = {}
    other_games = {}
    with open(args.filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            split_line = line.split('\t')
            team = split_line[6]
            noc = split_line[7]
            games = split_line[8]
            year = split_line[9]
            city = split_line[11]
            medal = split_line[14]

            if country == team or country == noc:
                first_game[city] = year
                if games not in other_games:
                    other_games[games] = [0, 0, 0, 0]
                else:
                    if medal != 'NA':
                        if medal == 'Gold':
                            other_games[games][1] +=1
                        if medal == 'Silver':
                            other_games[games][2] +=1
                        if medal == 'Bronze':
                            other_games[games][3] +=1
                        other_games[games][0] = other_games[games][1] + other_games[games][2] + other_games[games][3]

        gold = 0
        silver = 0
        bronze = 0
        sum_games = 0

        for i in other_games:
            gold += other_games[i][1]
            silver += other_games[i][2]
            bronze += other_games[i][3]
            sum_games +=1
        first = min(first_game, key=first_game.get)
        best = max(other_games, key=other_games.get)
        worst = min(other_games, key=other_games.get)
        print(f'First game in {first} in {first_game[first]} year')
        print(f'Best game in {best}, and got {other_games[best][0]} medals')
        print(f'Worst game in {worst}, and got {other_games[worst][0]} medals')
        print(f'An average: gold {gold//sum_games}, silver {silver//sum_games}, bronze {bronze//sum_games} ')



print(f'{args.overall=}')
if args.overall:
    overall()
    
if args.interactive:
    interactive()
print(args)
