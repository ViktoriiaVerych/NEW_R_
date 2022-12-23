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


print(f'{args.overall=}')
if args.overall:
    overall()