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

def _find_player(df, search_dict):
    for key, val in search_dict.items():
        if key == 'index':
            continue
        df = df[df[key]==val]
    if df.empty:
        traits = "".join([f"{k}={v}, " for k,v in search_dict.items()])
        raise ValueError(f"Unable to find player with {traits}")
    elif df.shape[0] > 1 and search_dict['index'] == None:
        traits = "".join([f"{k}={v}, " for k,v in search_dict.items()])
        ids = ", ".join(str(id) for id in df['key_mlbam'].to_list())
        raise ValueError(f"Your player search ({traits}) was too vague. Found too many players. \
        \n To specify which player, try adding an index (name_first=Mariano, index=0) \
        \n Or you could try using the player's id: {ids}")
    elif df.shape[0] > 1:
        return int(df.iloc[search_dict['index']]['key_mlbam'])
    else:
        return int(df['key_mlbam'])

def _player_search(df, player_info):

    if isinstance(player_info, list):
        return [_find_player(df, p) for p in player_info]
    else:
        return _find_player(df, player_info)

def get_player_ids(player_info=None):

    if isinstance(player_info, int):
        return player_info
    elif isinstance(player_info, list) and isinstance(player_info[0], int):
        return [p for p in player_info]
    elif isinstance(player_info, list) and isinstance(player_info[0], str):
        players = []
        for player in player_info:
            name = player.split(' ') if " " in player else player.split('+')
            index = int(name[2]) if len(name) > 2 else None
            players.append({'name_first':name[0],'name_last':name[1],'index':index})
        df = pd.read_csv(f'{os.path.dirname(utils.__file__)}/players.csv')
        return _player_search(df, players)
    else:
        df = pd.read_csv(f'{os.path.dirname(utils.__file__)}/players.csv')
        return _player_search(df, player_info)
