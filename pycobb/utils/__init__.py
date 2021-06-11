TEAMS = {
  "ARI": {
    "stadium": {
      "id": "15",
      "name": " Chase Field"
    }
  },
  "ATL": {
    "stadium": {
      "id": "4705",
      "name": " Truist Park"
    }
  },
  "ATL-2016": {
    "stadium": {
      "id": "16",
      "name": " Turner Field"
    }
  },
  "BAL": {
    "stadium": {
      "id": "2",
      "name": " Oriole Park"
    }
  },
  "BOS": {
    "stadium": {
      "id": "3",
      "name": " Fenway Park"
    }
  },
  "CHC": {
    "stadium": {
      "id": "17",
      "name": " Wrigley Field"
    }
  },
  "CIN": {
    "stadium": {
      "id": "2602",
      "name": " GABP"
    }
  },
  "CLE": {
    "stadium": {
      "id": "5",
      "name": " Progressive Field"
    }
  },
  "COL": {
    "stadium": {
      "id": "19",
      "name": " Coors Field"
    }
  },
  "CWS": {
    "stadium": {
      "id": "4",
      "name": " Guaranteed Rate Fld"
    }
  },
  "DET": {
    "stadium": {
      "id": "2394",
      "name": " Comerica Park"
    }
  },
  "FLA-2011": {
    "stadium": {
      "id": "20",
      "name": " Hard Rock Stadium"
    }
  },
  "HOU": {
    "stadium": {
      "id": "2392",
      "name": " Minute Maid Park"
    }
  },
  "KC": {
    "stadium": {
      "id": "7",
      "name": " Kauffman Stadium"
    }
  },
  "LA": {
    "stadium": {
      "id": "22",
      "name": " Dodger Stadium"
    }
  },
  "LAA": {
    "stadium": {
      "id": "1",
      "name": " Angel Stadium"
    }
  },
  "LAD": {
    "stadium": {
      "id": "22",
      "name": " Dodger Stadium"
    }
  },
  "MIA": {
    "stadium": {
      "id": "4169",
      "name": " Marlins Park"
    }
  },
  "MIL": {
    "stadium": {
      "id": "32",
      "name": " Miller Park"
    }
  },
  "MIN": {
    "stadium": {
      "id": "3312",
      "name": " Target Field"
    }
  },
  "MIN-2009": {
    "stadium": {
      "id": "8",
      "name": " Metrodome"
    }
  },
  "NYM": {
    "stadium": {
      "id": "3289",
      "name": " Citi Field"
    }
  },
  "NYM-2008": {
    "stadium": {
      "id": "25",
      "name": " Shea Stadium"
    }
  },
  "NYY": {
    "stadium": {
      "id": "3313",
      "name": " Yankee Stadium"
    }
  },
  "NYY-2008": {
    "stadium": {
      "id": "9",
      "name": " Yankee Stadium"
    }
  },
  "OAK": {
    "stadium": {
      "id": "10",
      "name": " Oakland Coliseum"
    }
  },
  "PHI": {
    "stadium": {
      "id": "2681",
      "name": " Citizens Bank Park"
    }
  },
  "PIT": {
    "stadium": {
      "id": "31",
      "name": " PNC Park"
    }
  },
  "SD": {
    "stadium": {
      "id": "2680",
      "name": " Petco Park"
    }
  },
  "SEA": {
    "stadium": {
      "id": "680",
      "name": " T-Mobile Park"
    }
  },
  "SF": {
    "stadium": {
      "id": "2395",
      "name": " Oracle Park"
    }
  },
  "STL": {
    "stadium": {
      "id": "2889",
      "name": " Busch Stadium"
    }
  },
  "TB": {
    "stadium": {
      "id": "12",
      "name": " Tropicana Field"
    }
  },
  "TEX": {
    "stadium": {
      "id": "5325",
      "name": " Globe Life Field"
    }
  },
  "TEX-2019": {
    "stadium": {
      "id": "13",
      "name": " Globe Life Park"
    }
  },
  "TOR": {
    "stadium": {
      "id": "14",
      "name": " Rogers Centre"
    }
  },
  "WSH": {
    "stadium": {
      "id": "3309",
      "name": " Nationals Park"
    }
  }
}

SEARCH_TERMS = {
    'pitch_types':{
        'id':'hfPT',
        'list':True,
        'options':"FF|FT|FC|SI|FS|SL|CH|CU|KC|CS|KN|FO|EP|SC|IN|PO|AB|UN".split("|")
    },
    'pa_result':{
        'id':'hfAB',
        'list':True,
        "options":"single|double|triple|home_run|field_out|strikeout|strikeout_double_play|walk|double_play|field_error|grounded_into_double_play|fielders_choice|fielders_choice_out|batter_interference|catcher_interf|caught_stealing_2b|caught_stealing_3b|caught_stealing_home|force_out|hit_by_pitch|intent_walk|sac_bunt|sac_bunt_double_play|sac_fly|sac_fly_double_play|triple_play".split("|")
        },
    'game_type':{
        'id':'hfGT',
        'list':True,
        'options':"R|PO|F|D|L|W|S".split('|')
    },
    'pitch_result':{
        'id':'hfPR',
        'list':True,
        'options':"automatic\.\.ball|ball|blocked\.\.ball|called\.\.strike|foul|foul\.\.bunt|foul\.\.pitchout|pitchout|hit\.\.by\.\.pitch|intent\.\.ball|hit\.\.into\.\.play|hit\.\.into\.\.play\.\.no\.\.out|hit\.\.into\.\.play\.\.score|pitchout\.\.hit\.\.into\.\.play\.\.score|missed\.\.bunt|foul\.\.tip|swinging\.\.pitchout|swinging\.\.strike|swinging\.\.strike\.\.blocked".replace("\.\.", "_").split("|")
    },
    'gameday_zone':{
        'id':'hfZ',
        'list':True,
        'options':[int(v) for v in range(1,15)]
    },
    'stadium':{
        'id':'stadium',
        'list':False,
        'options':["15","4705","16","2","3","17","2602","5","19","4","2394","20","2392","7","22",
        "1","4169","32","3312","8","3289","25","3313","9","10","2681","31","2680","680",
        "2395","2889","12","5325","13","3309","14"]
    },
    'batted_ball_location':{
        'id':'hfBBL',
        'list':True,
        'options':[int(v) for v in range(1,10)]
    },
    'attack_zone':{
        'id':'hfNewZones',
        'list':True,
        'options':[int(v) for v in range(1, 40)]
    },
    'batted_ball_direction':{
        'id':'hfPull',
        'list':True,
        'options':"Pull|Straightaway|Opposite".split('|')
    },
    'count':{
        'id':'hfC',
        'list':True,
        'options':"00|01|02|10|11|12|20|21|22|30|31|32|ahead|even|behind|2strikes|3balls".split("|")
    },
    'years':{
        'id':'hfSea',
        'list':True,
        'options':[int(year) for year in range(1999, 2022)]
    },
    'situation':{
        'id':'hfSit',
        'list':True,
        'options':"Go\.\.Ahead\.run\.at\.plate|Go\.\.Ahead\.run\.on\.base|Tying\.run\.at\.plate|Tying\.run\.on\.base|Tying\.run\.on\.deck".replace("\.","_").split("|")
    },
    'player_type':{
        'id':'player_type',
        'list':False,
        'options':['Batter',"Pitcher"]+[f'fielder_{i}' for i in range(2, 10)]

    },
    'outs':{
        'id':'hfOuts',
        'list':True,
        'options':[int(i) for i in range(1,3)]
    },
    'opponent':{
        'id':'opponent',
        'list':False,
        'options':["American+League","National+League"]+list(TEAMS.keys())
    },
    'pitcher_throws':{
        'id':'pitcher_throws',
        'list':False,
        'options':["R","L"]
    },
    'batter_stands':{
        'id':'batter_stands',
        'list':False,
        'options':["R","L"]
    },
    'quality_of_contact':{
        'id':'hfSA',
        'list':True,
        'options':[int(v) for v in range(1,7)]
    },
    'date_range':{
        'list':True
    },
    'if_alignment':{
        'id':'hfInfield',
        'list':True,
        'options':['1','2','3']
    },
    'team':{
        'id':'team',
        'list':False,
        'options':["American+League","National+League"]+list(TEAMS.keys())
    },
    'position':{
        'id':'position',
        'list':False,
        'options':['IF','OF','SP',"RP"]+[int(i) for i in range(1,11)]
    },
    'of_alignment':{
        'id':'hfOutfield',
        'list':True,
        'options':[int(v) for v in range(1,5)]
    },
    'runners_on':{
        'id':'hfRO',
        'list':True,
        'options':[int(v) for v in range(1, 9)]
    },
    'home_or_away':{
        'id':'home_road',
        'list':False,
        'options':["Home","Away"]
    },
    'flags':{
        'id':'hfFlag',
        'list':True,
        'options':"touch1\.\.is\.\.putout|touch1\.\.is\.\.assist|touch1\.\.is\.\.deflection|touch1\.\.is\.\.error|is\.\.hit\.\.into\.\.play\.\.basehit|is\.\.hit\.\.into\.\.play\.\.hardhit|is\.\.bunt|is\.\.last\.\.pitch|is\.\.launch\.\.angle\.\.sweetspot|is\.\.nonpitcher\.\.pitcher|is\.\.remove\.\.bunts|is\.\.starter\.\.batter|is\.\.non\.\.starter\.\.batter".replace("\.\.","_").split("|")
    },
    'batted_ball_type':{
        'id':'hfBBT',
        'list':True,
        'options':"fly\.\.ball|popup|line\.\.drive|ground\.\.ball".replace("\.\.","_").split("|")
    },
    'metric_range':{
        'id':'metric_1',
        'list':False,
        'options':["api_p_release_speed","api_h_launch_speed","api_h_launch_angle",
        "delta_run_exp","api_h_launch_direction","api_h_launch_direction_pullopp",
        "api_h_distance_projected","api_p_release_spin_rate","lineup_cd","api_p_effective_speed",
        "api_release_pos_x","api_release_pos_z","api_plate_x","api_plate_z","estimated_ba_using_speedangle",
        "estimated_slg_using_speedangle","estimated_iso_using_speedangle","estimated_woba_using_speedangle",
        "home_score","away_score","home_score_diff","bat_score","fld_score","bat_score_diff",
        "home_win_exp","bat_win_exp","n_thruorder_pitcher","n_priorpa_thisgame_player_at_bat"
        ]
    },
    "metric_low":{
        "id":"metric_1_gt"
    },
    "metric_high":{
        'id':"metric_1_lt"
    },
    'inning':{
        'id':'hfInn',
        'list':True,
        'options':[int(v) for v in range(1,11)]
    },
    "pitchers":{
        'id':'pitchers_lookup[]',
        'list':True,
        'options':[int(v) for v in range(1,1000000)]
    },
    "batters":{
        'id':'batters_lookup[]',
        'list':True,
        'options':[int(v) for v in range(1,1000000)]
    }
}

STATS = {
  "umpire":{"type":str},
  "sv_id":{"type":str},
  "pitcher.1":{"type":str},
  "fielder_2.1":{"type":str},
  "pitch_type": {
    "description": "The type of pitch derived from Statcast.",
    "type": str
  },
  "game_date": {
    "description": "Date of the Game.",
    "type": str
  },
  "release_speed": {
    "description": "Pitch velocities from 2008-16 are via Pitch F/X, and adjusted to roughly out-of-hand release point. All velocities from 2017 and beyond are Statcast, which are reported out-of-hand.",
    "type": float
  },
  "release_pos_x": {
    "description": "Horizontal Release Position of the ball measured in feet from the catcher's perspective.",
    "type": float
  },
  "release_pos_z": {
    "description": "Vertical Release Position of the ball measured in feet from the catcher's perspective.",
    "type": float
  },
  "player_name": {
    "description": "Player's name tied to the event of the search.",
    "type": str
  },
  "batter": {
    "description": "MLB Player Id tied to the play event.",
    "type": float
  },
  "pitcher": {
    "description": "MLB Player Id tied to the play event.",
    "type": float
  },
  "events": {
    "description": "Event of the resulting Plate Appearance.",
    "type": str
  },
  "description": {
    "description": "Description of the resulting pitch.",
    "type": str
  },
  "spin_dir": {
    "description": "* Deprecated field from the old tracking system.",
    "type": float
  },
  "spin_rate_deprecated": {
    "description": "* Deprecated field from the old tracking system. Replaced by release_spin",
    "type": float
  },
  "break_angle_deprecated": {
    "description": "* Deprecated field from the old tracking system.",
    "type": float
  },
  "break_length_deprecated": {
    "description": "* Deprecated field from the old tracking system.",
    "type": float
  },
  "zone": {
    "description": "Zone location of the ball when it crosses the plate from the catcher's perspective.",
    "type": "Int64"
  },
  "des": {
    "description": "Plate appearance description from game day.",
    "type": str
  },
  "game_type": {
    "description": "Type of Game. E = Exhibition, S = Spring Training, R = Regular Season, F = Wild Card, D = Divisional Series, L = League Championship Series, W = World Series",
    "type": str
  },
  "stand": {
    "description": "Side of the plate batter is standing.",
    "type": str
  },
  "p_throws": {
    "description": "Hand pitcher throws with.",
    "type": str
  },
  "home_team": {
    "description": "Abbreviation of home team.",
    "type": str
  },
  "away_team": {
    "description": "Abbreviation of away team.",
    "type": str
  },
  "type": {
    "description": "Short hand of pitch result. B = ball, S = strike, X = in play.",
    "type": str
  },
  "hit_location": {
    "description": "Position of first fielder to touch the ball.",
    "type": "Int64"
  },
  "bb_type": {
    "description": "Batted ball type, ground_ball, line_drive, fly_ball, popup.",
    "type": str
  },
  "balls": {
    "description": "Pre-pitch number of balls in count.",
    "type": "Int64"
  },
  "strikes": {
    "description": "Pre-pitch number of strikes in count.",
    "type": "Int64"
  },
  "game_year": {
    "description": "Year game took place.",
    "type": "Int64"
  },
  "pfx_x": {
    "description": "Horizontal movement in feet from the catcher's perspective.",
    "type": float
  },
  "pfx_z": {
    "description": "Vertical movement in feet from the catcher's perpsective.",
    "type": float
  },
  "plate_x": {
    "description": "Horizontal position of the ball when it crosses home plate from the catcher's perspective.",
    "type": float
  },
  "plate_z": {
    "description": "Vertical position of the ball when it crosses home plate from the catcher's perspective.",
    "type": float
  },
  "on_3b": {
    "description": "Pre-pitch MLB Player Id of Runner on 3B.",
    "type": "Int64"
  },
  "on_2b": {
    "description": "Pre-pitch MLB Player Id of Runner on 2B.",
    "type": "Int64"
  },
  "on_1b": {
    "description": "Pre-pitch MLB Player Id of Runner on 1B.",
    "type": "Int64"
  },
  "outs_when_up": {
    "description": "Pre-pitch number of outs.",
    "type": "Int64"
  },
  "inning": {
    "description": "Pre-pitch inning number.",
    "type": "Int64"
  },
  "inning_topbot": {
    "description": "Pre-pitch top or bottom of inning.",
    "type": str
  },
  "hc_x": {
    "description": "Hit coordinate X of batted ball.",
    "type": float
  },
  "hc_y": {
    "description": "Hit coordinate Y of batted ball.",
    "type": float
  },
  "tfs_deprecated": {
    "description": "* Deprecated field from old tracking system.",
    "type": float
  },
  "tfs_zulu_deprecated": {
    "description": "* Deprecated field from old tracking system.",
    "type": float
  },
  "fielder_2": {
    "description": "MLB Player Id for catcher.",
    "type": "Int64"
  },
  "vx0": {
    "description": "The velocity of the pitch, in feet per second, in x-dimension, determined at y=50 feet.",
    "type": float
  },
  "vy0": {
    "description": "The velocity of the pitch, in feet per second, in y-dimension, determined at y=50 feet.",
    "type": float
  },
  "vz0": {
    "description": "The velocity of the pitch, in feet per second, in z-dimension, determined at y=50 feet.",
    "type": float
  },
  "ax": {
    "description": "The acceleration of the pitch, in feet per second per second, in x-dimension, determined at y=50 feet.",
    "type": float
  },
  "ay": {
    "description": "The acceleration of the pitch, in feet per second per second, in y-dimension, determined at y=50 feet.",
    "type": float
  },
  "az": {
    "description": "The acceleration of the pitch, in feet per second per second, in z-dimension, determined at y=50 feet.",
    "type": float
  },
  "sz_top": {
    "description": "Top of the batter's strike zone set by the operator when the ball is halfway to the plate.",
    "type": float
  },
  "sz_bot": {
    "description": "Bottom of the batter's strike zone set by the operator when the ball is halfway to the plate.",
    "type": float
  },
  "hit_distance": {
    "description": "Projected hit distance of the batted ball.",
    "type": float
  },
  "hit_distance_sc": {
    "description": "Projected hit distance of the batted ball.",
    "type": float
  },
  "launch_speed": {
    "description": "Exit velocity of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.",
    "type": float
  },
  "launch_angle": {
    "description": "Launch angle of the batted ball as tracked by Statcast. For the limited subset of batted balls not tracked directly, estimates are included based on the process described here.",
    "type": float
  },
  "effective_speed": {
    "description": "Derived speed based on the the extension of the pitcher's release.",
    "type": float
  },
  "release_spin": {
    "description": "Spin rate of pitch tracked by Statcast.",
    "type":float
  },
  "release_spin_rate": {
    "description": "Spin rate of pitch tracked by Statcast.",
    "type": float
  },
  "release_extension": {
    "description": "Release extension of pitch in feet as tracked by Statcast.",
    "type": float
  },
  "game_pk": {
    "description": "Unique Id for Game.",
    "type": "Int64"
  },
  "fielder_3": {
    "description": "MLB Player Id for 1B.",
    "type": "Int64"
  },
  "fielder_4": {
    "description": "MLB Player Id for 2B.",
    "type": "Int64"
  },
  "fielder_5": {
    "description": "MLB Player Id for 3B.",
    "type": "Int64"
  },
  "fielder_6": {
    "description": "MLB Player Id for SS.",
    "type": "Int64"
  },
  "fielder_7": {
    "description": "MLB Player Id for LF.",
    "type": "Int64"
  },
  "fielder_8": {
    "description": "MLB Player Id for CF.",
    "type": "Int64"
  },
  "fielder_9": {
    "description": "MLB Player Id for RF.",
    "type": "Int64"
  },
  "release_pos_y": {
    "description": "Release position of pitch measured in feet from the catcher's perspective.",
    "type": float
  },
  "estimated_ba_using_speedangle": {
    "description": "Estimated Batting Avg based on launch angle and exit velocity.",
    "type": float
  },
  "estimated_woba_using_speedangle": {
    "description": "Estimated wOBA based on launch angle and exit velocity.",
    "type": float
  },
  "woba_value": {
    "description": "wOBA value based on result of play.",
    "type": float
  },
  "woba_denom": {
    "description": "wOBA denominator based on result of play.",
    "type": float
  },
  "babip_value": {
    "description": "BABIP value based on result of play.",
    "type": float
  },
  "iso_value": {
    "description": "ISO value based on result of play.",
    "type": float
  },
  "launch_speed_angle": {
    "description": "Launch speed/angle zone based on launch angle and exit velocity. 1: Weak, 2: Topped, 3: Under, 4: Flare/Burner, 5: Solid Contact, 6: Barrel",
    "type": float
  },
  "at_bat_number": {
    "description": "Plate appearance number of the game.",
    "type": "Int64"
  },
  "pitch_number": {
    "description": "Total pitch number of the plate appearance.",
    "type": "Int64"
  },
  "pitch_name": {
    "description": "The name of the pitch derived from the Statcast Data.",
    "type": str
  },
  "home_score": {
    "description": "Pre-pitch home score",
    "type": "Int64"
  },
  "away_score": {
    "description": "Pre-pitch away score",
    "type": "Int64"
  },
  "bat_score": {
    "description": "Pre-pitch bat team score",
    "type": "Int64"
  },
  "fld_score": {
    "description": "Pre-pitch field team score",
    "type": "Int64"
  },
  "post_home_score": {
    "description": "Post-pitch home score",
    "type": "Int64"
  },
  "post_away_score": {
    "description": "Post-pitch away score",
    "type": "Int64"
  },
  "post_bat_score": {
    "description": "Post-pitch bat team score",
    "type": "Int64"
  },
  "post_fld_score": {
    "description": "Post-pitch fielding team score",
    "type": "Int64"
  },
  "if_fielding_alignment": {
    "description": "Infield fielding alignment at the time of the pitch.",
    "type": str
  },
  "of_fielding_alignment": {
    "description": "Outfield fielding alignment at the time of the pitch.",
    "type": str
  },
  "spin_axis": {
    "description": "The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball",
    "type": "Int64"
  },
  "delta_home_win_exp": {
    "description": "The change in Win Expectancy before the Plate Appearance and after the Plate Appearance",
    "type": float
  },
  "delta_run_exp": {
    "description": "The change in Run Expectancy before the Pitch and after the Pitch",
    "type": float
  }
}

PLAYER_TYPES = {
    "key_person":str,
    "key_uuid":str,
    "key_mlbam":"Int64",
    "key_retro":str,
    "key_bbref":str,
    "key_bbref_minors":str,
    "key_fangraphs":"Int64",
    "key_npb":str,
    "key_sr_nfl":str,
    "key_sr_nba":str,
    "key_sr_nhl":str,
    "key_findagrave":str,
    "name_last":str,
    "name_first":str,
    "name_given":str,
    "name_suffix":str,
    "name_matrilineal":str,
    "name_nick":str,
    "birth_year":'Int64',
    "birth_month":'Int64',
    "birth_day":'Int64',
    "death_year":'Int64',
    "death_month":'Int64',
    "death_day":'Int64',
    "pro_played_first":float,
    "pro_played_last":float,
    "mlb_played_first":'Int64',
    "mlb_played_last":'Int64',
    "col_played_first":float,
    "col_played_last":float,
    "pro_managed_first":float,
    "pro_managed_last":float,
    "mlb_managed_first":float,
    "mlb_managed_last":float,
    "col_managed_first":float,
    "col_managed_last":float,
    "pro_umpired_first":float,
    "pro_umpired_last":float,
    "mlb_umpired_first":float,
    "mlb_umpired_last":float
}

PITCH_NAMES = {
    "FF":"Fastball (4-seam)",
    "FT":"Fastball (2-seam)",
    "FC":"Fastball (Cut)",
    "SI":"Sinker",
    "FS":"Split-finger",
    "SL":"Slider",
    "CH":"Changeup",
    "CU":"Curveball",
    "KC":"Knuckle Curve",
    "CS":"Slow Curve",
    "KN":"Knuckleball",
    "FO":"Forkball",
    "EP":"Eephus",
    "SC":"Screwball",
    "IN":"Intentional Ball",
    "PO":"Pitchout",
    "AB":"Automatic Ball",
    "UN":"Unknown"
}
