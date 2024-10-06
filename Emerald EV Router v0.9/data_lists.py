
import pandas as pd
import numpy as np

file_path = 'Data.xlsx'

#Get data from sheets in excel
pokemon_data = pd.read_excel(file_path, sheet_name = 'Pokemon')
trainer_data = pd.read_excel(file_path, sheet_name = 'Trainers')
exp_group = pd.read_excel(file_path, sheet_name = 'EXP_Group')

#EXP Group Data: Indexes = 0->Fast; 1->Medium Fast; 2->Medium Slow; 3->Slow; 4->Fluctuating; 5->Erratic
exp_group_list = []
exp_group_names = exp_group.keys()
num_exp_groups = len(exp_group_names)
for x in range(num_exp_groups):
    exp_group_list.append(exp_group[exp_group_names[x]].tolist())

#Pokemon Data
pk_list = pokemon_data['Name'].tolist()
hp_list = pokemon_data['HP'].tolist()
att_list = pokemon_data['Attack'].tolist()
def_list = pokemon_data['Defense'].tolist()
spa_list = pokemon_data['Sp. Attack'].tolist()
spd_list = pokemon_data['Sp. Defense'].tolist()
spe_list = pokemon_data['Speed'].tolist()

hp_EV_list = pokemon_data['HP_EV'].tolist()
att_EV_list = pokemon_data['Att_EV'].tolist()
def_EV_list = pokemon_data['Def_EV'].tolist()
spa_EV_list = pokemon_data['SpA_EV'].tolist()
spd_EV_list = pokemon_data['SpD_EV'].tolist()
spe_EV_list = pokemon_data['Spe_EV'].tolist()

#Trainer Data
tindex_list = trainer_data['Index'].tolist()
gymleader_list = trainer_data['Tab'].tolist()

tname_list = trainer_data['Name'].tolist()
tmny_list_str = trainer_data['Money'].tolist()
tmny_list = list(map(int, tmny_list_str))
troute_list = trainer_data['Route'].tolist()

tpk1_list = trainer_data['Pokémon_1'].tolist()
tlvl1_list_str = trainer_data['Level_1'].tolist()
tlvl1_list = list(map(int, tlvl1_list_str))
texp1_list_str = trainer_data['EXP_1'].tolist()
texp1_list = list(map(int, texp1_list_str))

tpk2_list = trainer_data['Pokémon_2'].tolist()
tlvl2_list_str = trainer_data['Level_2'].tolist()
tlvl2_list = list(map(int, tlvl2_list_str))
texp2_list_str = trainer_data['EXP_2'].tolist()
texp2_list = list(map(int, texp2_list_str))

tpk3_list = trainer_data['Pokémon_3'].tolist()
tlvl3_list_str = trainer_data['Level_3'].tolist()
tlvl3_list = list(map(int, tlvl3_list_str))
texp3_list_str = trainer_data['EXP_3'].tolist()
texp3_list = list(map(int, texp3_list_str))

tpk4_list = trainer_data['Pokémon_4'].tolist()
tlvl4_list_str = trainer_data['Level_4'].tolist()
tlvl4_list = list(map(int, tlvl4_list_str))
texp4_list_str = trainer_data['EXP_4'].tolist()
texp4_list = list(map(int, texp4_list_str))

tpk5_list = trainer_data['Pokémon_5'].tolist()
tlvl5_list_str = trainer_data['Level_5'].tolist()
tlvl5_list = list(map(int, tlvl5_list_str))
texp5_list_str = trainer_data['EXP_5'].tolist()
texp5_list = list(map(int, texp5_list_str))

tpk6_list = trainer_data['Pokémon_6'].tolist()
tlvl6_list_str = trainer_data['Level_6'].tolist()
tlvl6_list = list(map(int, tlvl6_list_str))
texp6_list_str = trainer_data['EXP_6'].tolist()
texp6_list = list(map(int, texp6_list_str))

ttot_exp_list_str = trainer_data['Tot_EXP'].tolist()
ttot_exp_list = list(map(int, ttot_exp_list_str))

tman_list = trainer_data['Mandatory'].tolist()
tstart_list = trainer_data['Rival_Starter'].tolist()
thm_list = trainer_data['HM'].tolist()

#Natures
natures = [
    "Hardy (±0, ±0)",
    "Lonely (+Att, -Def)",
    "Brave (+Att, -Speed)",
    "Adamant (+Att, -Sp.Atk)",
    "Naughty (+Att, -Sp.Def)",
    
    "Bold (+Def, -Att)",
    "Docile (±0, ±0)",
    "Relaxed (+Def, -Speed)",
    "Impish (+Def, -Sp.Atk)",
    "Lax (+Def, -Sp.Def)",
    
    "Timid (+Speed, -Att)",
    "Hasty (+Speed, -Def)",
    "Serious (±0, ±0)",
    "Jolly (+Speed, -Sp.Atk)",
    "Naive (+Speed, -Sp.Def)",
    
    "Modest (+Sp.Atk, -Att)",
    "Mild (+Sp.Atk, -Def)",
    "Quiet (+Sp.Atk, -Speed)",
    "Bashful (±0, ±0)",
    "Rash (+Sp.Atk, -Sp.Def)",
    
    "Calm (+Sp.Def, -Att)",
    "Gentle (+Sp.Def, -Def)",
    "Sassy (+Sp.Def, -Speed)",
    "Careful (+Sp.Def, -Sp.Atk)",
    "Quirky (±0, ±0)"
]
patt_nat = [
    "Lonely (+Att, -Def)",
    "Brave (+Att, -Speed)",
    "Adamant (+Att, -Sp.Atk)",
    "Naughty (+Att, -Sp.Def)",
]
pdef_nat = [
    "Bold (+Def, -Att)",
    "Relaxed (+Def, -Speed)",
    "Impish (+Def, -Sp.Atk)",
    "Lax (+Def, -Sp.Def)",
]
pspe_nat = [
    "Timid (+Speed, -Att)",
    "Hasty (+Speed, -Def)",
    "Jolly (+Speed, -Sp.Atk)",
    "Naive (+Speed, -Sp.Def)",
]
pspa_nat = [
    "Modest (+Sp.Atk, -Att)",
    "Mild (+Sp.Atk, -Def)",
    "Quiet (+Sp.Atk, -Speed)",
    "Rash (+Sp.Atk, -Sp.Def)",
]
pspd_nat = [
    "Calm (+Sp.Def, -Att)",
    "Gentle (+Sp.Def, -Def)",
    "Sassy (+Sp.Def, -Speed)",
    "Careful (+Sp.Def, -Sp.Atk)",
]
natt_nat = [
    "Bold (+Def, -Att)",  
    "Timid (+Speed, -Att)",
    "Modest (+Sp.Atk, -Att)",
    "Calm (+Sp.Def, -Att)",
]
ndef_nat = [
    "Lonely (+Att, -Def)",
    "Hasty (+Speed, -Def)",
    "Mild (+Sp.Atk, -Def)",
    "Gentle (+Sp.Def, -Def)",
]
nspe_nat = [
    "Brave (+Att, -Speed)",
    "Relaxed (+Def, -Speed)",
    "Quiet (+Sp.Atk, -Speed)",
    "Sassy (+Sp.Def, -Speed)",
]
nspa_nat = [
    "Adamant (+Att, -Sp.Atk)",
    "Impish (+Def, -Sp.Atk)",
    "Jolly (+Speed, -Sp.Atk)",
    "Careful (+Sp.Def, -Sp.Atk)",
]
nspd_nat = [
    "Naughty (+Att, -Sp.Def)",
    "Lax (+Def, -Sp.Def)",
    "Naive (+Speed, -Sp.Def)",
    "Rash (+Sp.Atk, -Sp.Def)",
]
pos_natures_array = [patt_nat, 
                    pdef_nat, 
                    pspa_nat, 
                    pspd_nat, 
                    pspe_nat]
neg_natures_array = [natt_nat, 
                    ndef_nat, 
                    nspa_nat, 
                    nspd_nat, 
                    nspe_nat]

#Nested list of base stats
base_stat_list = [hp_list,
                att_list,
                def_list,
                spa_list,
                spd_list,
                spe_list,]
        
#Nested list of EVs       
pk_EV_array = [hp_EV_list, 
                att_EV_list, 
                def_EV_list, 
                spa_EV_list, 
                spd_EV_list, 
                spe_EV_list]

#Hidden power types in order
hidden_power_type = ['Fighting', 
                    'Flying', 
                    'Poison',
                    'Ground', 
                    'Rock', 
                    'Bug', 
                    'Ghost', 
                    'Steel', 
                    'Fire', 
                    'Water', 
                    'Grass', 
                    'Electric', 
                    'Psychic', 
                    'Ice', 
                    'Dragon', 
                    'Dark']