import time, argparse, sys, os, datetime, requests
from pycobb import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def _get_arguments():
    parser = argparse.ArgumentParser(description="Get Pitch Data from Baseball Savant")
    parser.add_argument('command', type=str, help="Command to be Run")
    parser.add_argument('-s', '--save',dest='save',nargs=1, help="save data to a specified file path")
    parser.add_argument('-d',dest='date_range', nargs=2, help="range of dates to be searched i.e. 2021-05-03 2021-05-08")
    parser.add_argument(
        '-p', dest='pitchers', nargs="+",
        help="list of pitchers to search (MLB ID or name). ex: -p 124692 506433 \
        or -p Cy+Young Yu+Darvish"
    )
    parser.add_argument(
        '-b', dest='batters', nargs="+",
        help="list of batters to search (MLB ID or name): ex: -b 112431 116539 \
        or -b Ty+Cobb Derek+Jeter"
    )
    parser.add_argument(
        '-t', dest='pitch_types', nargs='+',
        help="list of pitch types. e.g. -t FT CU"
    )
    parser.add_argument(
        '-y', dest='years', nargs='+',
        help="values or range of years"
    )
    parser.add_argument(
        '-c', dest='columns', nargs="+", help="Columns to return"
    )
    parser.add_argument('--print', dest='print', action='store_true', default=False, help="Print the dataframe when complete")
    parser.add_argument('--plot', nargs='+')
    return parser.parse_args(), parser

def _plot(pitches=None, x_col=None, y_col=None, title="", groupby=None):

    fig, ax = plt.subplots()

    if groupby:
        for group, pitches in pitches.groupby([groupby]):

            ax.scatter(group, pitches[y_col].mean(), color='gray')
    else:
        ax.scatter(pitches[x_col], pitches[y_col])

    ax.set_title(title)
    ax.set_ylabel(y_col)
    ax.set_xlabel(x_col)

    plt.show()

def main():

    args, parser = _get_arguments()

    if args.command == 'get':
        params = vars(args).copy()
        [params.pop(key) for key in ['command', 'save', 'print', 'plot']]
        if all(x is None for x in params.values()):
            raise ValueError('Search cannot be empty')
        pitches = get(**params)
        _ = print(pitches) if args.print else None
        _ = pitches.to_csv(args.save[0]) if args.save else None
        _ = _plot(pitches, *args.plot) if args.plot else None
        if pitches.shape[0] == 40000:
            print("\nWARNING: Baseball Savant limits queries to 40000 pitches. Try narrowing your search...\n")

    elif args.command == 'test':
        pass

    elif args.command == 'update':
        url = 'https://raw.githubusercontent.com/chadwickbureau/register/master/data/people.csv'
        r = requests.get(url)
        df = pd.read_csv(io.StringIO(r.text), dtype=PLAYER_TYPES)
        ignore = [  'mlb_managed_first', 'mlb_managed_last',  'col_managed_first',
                    'col_managed_last', 'pro_umpired_first', 'pro_umpired_last',
                    'mlb_umpired_first', 'mlb_umpired_last', 'pro_managed_first',
                    'pro_managed_last', 'col_played_first', 'col_played_last',
                    'pro_played_first', 'pro_played_last', 'key_npb','key_sr_nfl',
                    'key_sr_nba','key_sr_nhl',
        ]
        df = df[df['mlb_played_first'].notna()].drop(ignore, axis='columns')
        df.to_csv(f"{os.path.dirname(utils.__file__)}/players.csv")

    else:
        raise parser.error(f"Invalid command: '{args.command}'")
