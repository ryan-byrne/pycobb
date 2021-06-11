from .utils import *
import requests, io, time, datetime, os
import pandas as pd
import numpy as np

def get(  player_type="pitcher", min_results=0, group_by="name", columns=None,
            sort_col="pitches", player_event_sort="pitch_number_thisgame",
            sort_order="desc", min_pas=0, type="details", **kwargs):

    url = "https://baseballsavant.mlb.com/statcast_search/csv?all=true"

    for key, setting in {**locals(), **kwargs}.items():

        if not setting or key in ['url', 'kwargs']:
            continue

        elif key not in SEARCH_TERMS and key not in locals():
            raise ValueError(f"{key} is not a Valid Argument")

        elif key in locals():
            url+=f"&{key}={setting}"

        elif key in ['batters', 'pitchers']:
            if not setting:
                continue
            ids = get_player_ids(setting)
            if isinstance(ids, int):
                url+=f"&{SEARCH_TERMS[key]['id']}={ids}"
            else:
                url+="".join(f"&{SEARCH_TERMS[key]['id']}={id}" for id in ids)

        elif key == 'years':
            if not isinstance(setting, list):
                raise ValueError('Years must be declared as a list')
            url+="&hfSea="
            for year in setting:
                if "-" in year:
                    r0, r1 = year.split('-')
                    r_string = [str(y) for y in range(int(r0), int(r1))]
                    year="|".join(r_string)
                url+=f"{year}|"

        elif key == 'date_range':
            url+=f"&game_date_gt={setting[0]}&game_date_lt={setting[1]}"

        elif not SEARCH_TERMS[key]['list'] and setting not in SEARCH_TERMS[key]['options']:
            raise ValueError(f"{setting} is not a valid value for {key}")

        elif not SEARCH_TERMS[key]['list'] and isinstance(setting, list):
            raise TypeError(f"{key} must be a single value")

        elif SEARCH_TERMS[key]['list'] and not isinstance(setting, list):
            url+=f"&{SEARCH_TERMS[key]['id']}={setting}|"

        elif SEARCH_TERMS[key]['list']:
            url+=f"&{SEARCH_TERMS[key]['id']}="
            for value in setting:
                if value not in SEARCH_TERMS[key]['options']:
                    raise ValueError(f"{value} is not a valid value for {key}")
                else:
                    url+=f"{value}|"
        else:
            url+=f"&{key}={setting}"

    r = requests.get(url)
    dtype = {key:STATS[key]['type'] for key in STATS.keys()}
    ignore = ["umpire", "sv_id", "pitcher.1", "fielder_2.1"]
    df = pd.read_csv(io.StringIO(r.text), dtype=dtype)
    pd.to_datetime(df['game_date'])
    return df[columns] if columns else df

def _player_str_to_dict(search_str):

    search_dict = {}

    search_list = search_str.split(' ')
    if '.' in search_list[0] and '.' in search_list[1]:
        search_dict['name_first'] = f"{search_list[0]} {search_list[1]}"
        search_dict['name_last'] = search_list[2]
    elif '.' in search_list[0]:
        n = search_list[0].split('.')
        search_dict['name_first'] = f"{n[0]}. {n[1]}."
        search_dict['name_last'] = search_list[1]
    else:
        search_dict['name_first'] = search_list[0]
        search_dict['name_last'] = search_list[1]

    try:
        search_dict['index'] = int(search_list[-1])
    except ValueError:
        search_dict['index'] = None

    return search_dict

def _find_player(df, search):

    search_dict = _player_str_to_dict(search) if isinstance(search, str) else search

    for key, val in search_dict.items():
        # Filter DataFrame for specified values
        if key == 'index':
            continue
        df = df[df[key]==val]
    if df.empty:
        # Unable to find any entries
        traits = "".join([f"{k}={v}, " for k,v in search_dict.items()])
        raise ValueError(f"Unable to find player with {traits}")
    elif df.shape[0] > 1 and search_dict['index'] == None:
        # Too many entries and index not specified
        traits = "".join([f"{k}={v}, " for k,v in search_dict.items()])
        players = "\n ".join(f"{i} {p['name_first']} {p['name_last']}, {p['mlb_played_first']}-{p['mlb_played_last']}, {int(p['key_mlbam'])}" for i, (_, p) in enumerate(df.iterrows()))
        raise ValueError(f"Your player search ({traits}) was too vague.\
        \n Try adding an index (name_first=Pedro, name_last=Martinez, index=0) \
        \n Or using the player's id.\
        \n {players}")
    elif df.shape[0] > 1:
        # Index specifed with name
        return int(df.iloc[search_dict['index']]['key_mlbam'])
    else:
        # Only one name found, return ID
        return int(df['key_mlbam'])

def _player_search(df, player_info):

    if isinstance(player_info, list):
        return [_find_player(df, p) for p in player_info]
    else:
        return _find_player(df, player_info)

def get_player_ids(player_info):

    if isinstance(player_info, int):
        # Simply an MLB ID
        return player_info
    elif isinstance(player_info, list) and isinstance(player_info[0], int):
        # Simply a list of MLB IDs
        return [p for p in player_info]
    else:
        # List of strings
        df = pd.read_csv(f'{os.path.dirname(utils.__file__)}/players.csv')
        return _player_search(df, player_info)
