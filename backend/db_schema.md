Table name: USER
columns:    _id, name
types:      int, string
examples:   0,   Matti M.

Table name: STEPS
columns:    _id,    user_id,    steps,  date
types:      int,    int,        int,    date
examples    1,      0,          10_000, 11/10/2023

Table name: STRESS
columns:    _id,    user_id,    level,  level_min,  level_max,  date
types:      int,    int,        int,    int,        int,        date
examples:   1,      0,          54,     23,         73,         11/10/2023

Table name: SLEEP
columns:    _id,    user_id,    time,   date
types:      int,    int,        int,    date
examples:   1,      0,          510,    10/10/2023
