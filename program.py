import sys
from functions import *
from database_functions import *

if __name__ == '__main__':
    db = []
    try:
        with open(sys.argv[1]) as f:  # 1 is the script path
            file = f.readlines()
            for line in file:
                line = line.strip()
                if line == 'load':  # we have a load operator
                    db = load_creature_text_file("cscreatures.txt")
                    print(f'Loaded {len(db)} entries')
                else:
                    try:
                        line = line.split(":")
                        if line[0] == 'report-creatures':
                            for creature in db:
                                report_creature(creature)
                        elif line[0] == 'report-count':
                            print(f'{len(db)} entries')
                        elif line[0] == 'report-percent-kind':
                            print(f'{percent_by_kind(db, line[1])}% {line[1]}')
                        elif line[0] == 'report-avg-attr':
                            print(f'{line[1]} Average: {avg_attr(db, line[1])}')
                        elif line[0] == 'filter-legendary':
                            db = filter_legendary(db)
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == 'filter-by-kind':
                            db = filter_by_kind(db, line[1])
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == 'filter-out-kind':
                            db = filter_out_kind(db, line[1])
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == 'filter-by-attr-gt':
                            db = filter_by_attr_gt(db, line[1], int(line[2]))
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == 'filter-by-attr-lt':
                            db = filter_by_attr_lt(db, line[1], int(line[2]))
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == "report-avg-weight":
                            average = avg_weight(db)
                            print(f'Average Weight: {average}')
                        elif line[0] == 'filter-by-weight-gt':
                            db = filter_by_weight_gt(db, int(line[1]))
                            print(f'Filtered to {len(db)} entries')
                        elif line[0] == 'filter-by-weight-lt':
                            db = filter_by_weight_lt(db, int(line[1]))
                            print(f'Filtered to {len(db)} entries')
                    except ValueError:
                        continue
    except FileNotFoundError:
        print('file not found')
    except IndexError:
        print('invalid argument(s)')