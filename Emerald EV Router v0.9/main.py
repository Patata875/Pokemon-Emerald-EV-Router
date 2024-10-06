# Version 0.9

import math
import tkinter as tk
from tkinter import ttk
import data_lists
import threading

Title = "Emerald EV Router v0.9"

use_custom_titlebar = 'True' # If false, uses standard titlebar for OS

theme_all = 'dark' # "dark" makes it dark theme, anything else makes it light theme



#Imported Lists
if True:
    pk_EV_array = data_lists.pk_EV_array
    pk_list = data_lists.pk_list
    base_stat_list = data_lists.base_stat_list

    tpk1_list = data_lists.tpk1_list
    tpk2_list = data_lists.tpk2_list
    tpk3_list = data_lists.tpk3_list
    tpk4_list = data_lists.tpk4_list
    tpk5_list = data_lists.tpk5_list
    tpk6_list = data_lists.tpk6_list
    tpk_all_list = [tpk1_list,
                    tpk2_list,
                    tpk3_list,
                    tpk4_list,
                    tpk5_list,
                    tpk6_list,]

    pos_natures_array = data_lists.pos_natures_array
    neg_natures_array = data_lists.neg_natures_array

    ttot_exp_list = data_lists.ttot_exp_list
    exp_group_names = data_lists.exp_group_names
    exp_group_list = data_lists.exp_group_list
    exp_groups = data_lists.exp_group_names

    hidden_power_type_all = data_lists.hidden_power_type

    tindex_list = data_lists.tindex_list
    tname_list = data_lists.tname_list

    tab_list = data_lists.gymleader_list
    troute_list = data_lists.troute_list
    tman_list = data_lists.tman_list
    tstart_list = data_lists.tstart_list


#Variables
if True:
    init_lvl = 5 #Initial Level
    init_iv = 31 #Initial IVs
    init_ev = 0 #Initial EVs

    init_starter = 'Treecko' #Rival Starter

    pad_x = (10,10) #Horizontal space between widgets
    pad_y = (10,10) #Vertical space between widgets

    tot_columns = 12 #Max number of columns for each tab (mulitple of 2)
    columns_per_route = 2 #Number of columns used for each route


#Colors and Fonts
font_family = "Segoe UI"
font_size=10

if theme_all == 'dark':#Dark theme - Checkbuttons are difficult to see
    font_weight = 'bold'
    
    background_color = "#2b2b2b"
    secondary_background_color = "#494949"

    text_color = '#cecece'
    text_color_mandatory = '#82cddc'
    text_color_secondary = '#8b8b8b'

    button_color = '#14363d'
    button_hover_color = '#36535a'

    tab_color = "#2d6672"
    tab_select_color = "#36535a"

    progressbar_color = '#82cddc'
    checkbutton_color = 'black'
    
    border_color = 'black'
else: #Light theme
    font_weight = 'normal'
    
    background_color = "#dbdbdb"
    secondary_background_color = "#bfbfbf"

    text_color = 'black'
    text_color_mandatory = 'black'
    text_color_secondary = '#525252'

    button_color = '#0e88a1'
    button_hover_color = '#145d6b'

    tab_color = "#4eb2c7"
    tab_select_color = "#1f8ea6"

    progressbar_color = '#82cddc'
    checkbutton_color = 'black'
    
    border_color = 'black'


#Initializing lists
if True:
    total_number_trainers = len(data_lists.tname_list) #Total number of trainers

    checkbox_index = 0 #Initialize index of checkboxes
    checkboxes_all = [] #List of all checkboxes
    checkbox_vars = [] #Indicates checkbox variables with index corresponding to (trainer_index)
    trainer_checkbox_index_pairs = [] #List of trainer indexes and corresponding checkbox indexes (check_vars)

    ordered_tr_ind_list = [] #Indexes of trainers selected in order of selection
    prev_pk_battled_index = [] #Indexes of selected pokemon prior to latest selection - Used to update EVs only for changes in pokemon
    theoretical_new_EVs = [0,0,0,0,0,0] #List of theoretical EVs if no max 510/255 rule - Used for properly udating EVs when deselcting trainers
    pk_battled = [] #List of pokemon for each trainer in order of trainers selected

    non_selected_rivals = []#Indexes of rivals not for selected rival starter

    init_IV_list = [] #List of initial IVs
    for x in range(6):
        init_IV_list.append(init_iv)




#---------------------------------------------------Theme----------------------------------------------------

def set_custom_theme():
    style = ttk.Style()
    style.theme_use("clam")

    #Frame
    style.configure("TFrame",   
                            background=background_color,
                    )
    
    #Title Bar
    style.configure("TitleBar.TFrame",   
                            background=secondary_background_color,
                    )
    
    #Label
    style.configure("TLabel",   
                            background=background_color, 

                            foreground=text_color,
                            font= (font_family, font_size, font_weight), 
                    )
    
    #Title Bar - Label
    style.configure("TitleBar.TLabel",   
                            background=secondary_background_color, 

                            foreground=text_color,
                            font= (font_family, font_size, 'bold'), 
                    )
    
    #Combobox
    style.configure("TCombobox",  
                            background = background_color,
                            foreground = text_color,
                            fieldbackground = secondary_background_color,
                            
                            bordercolor=border_color,
                            lightcolor=border_color,
                            darkcolor=border_color,

                            arrowcolor = text_color,
                    )
    root.option_add("*TCombobox*Listbox.background", secondary_background_color)
    root.option_add("*TCombobox*Listbox.foreground", text_color)
    root.option_add('*TCombobox*editbox.font', (font_family, font_size, font_weight))
    root.option_add('*TCombobox*Listbox.font', (font_family, font_size, font_weight))

    #Button
    style.configure("TButton",  
                            background=button_color, 

                            foreground=text_color,
                            font= (font_family, font_size, 'bold'),  

                            bordercolor=border_color,
                            lightcolor=border_color,
                            darkcolor=border_color,

                            relief="raised", 
                            borderwidth=5,
                    )
    style.map("TButton",    
                            background=[("active", button_hover_color)],
                            bordercolor=[("focus", border_color), ("active", border_color)]
                )
    
    #Title Bar - Button
    style.configure("TitleBar.TButton",  
                            background=secondary_background_color, 

                            foreground=text_color,
                            font= (font_family, font_size, font_weight), 

                            bordercolor=secondary_background_color,
                            lightcolor=secondary_background_color,
                            darkcolor=secondary_background_color,

                            relief="raised", 
                            borderwidth=0,
                    )
    style.map("TitleBar.TButton",    
                            background=[("active", 'red')], 
                            bordercolor=[("focus", secondary_background_color), ("active", secondary_background_color)]
                )
    
    #Entry
    style.configure("TEntry",   
                            background = background_color,
                            fieldbackground=secondary_background_color,

                            foreground=text_color,
                            font= (font_family, font_size, 'bold'), 
                            insertcolor = text_color,

                            bordercolor=border_color,
                            lightcolor=border_color,
                            darkcolor=border_color,

                            borderwidth = 0,
                            highlightbackground = background_color,
                            highlightthickness = 0
                    )
    style.map("TEntry",   
                            background = background_color,
                )


    #Progressbar
    style.configure("TProgressbar",    
                            troughcolor=secondary_background_color, 
                            bordercolor=border_color, 
                            pbarrelief="sunken", 
                            borderwidth=0,

                            background=progressbar_color,
                            lightcolor = progressbar_color,
                            darkcolor = progressbar_color,
                    )

    #Checkbutton
    style.configure("TCheckbutton", 
                            background= background_color,
                    )
    style.map("TCheckbutton",   
                            background=[("active", background_color)],
                            indicatorcolor=[("active", background_color)]
               )
    
    #Notebook
    style.configure("TNotebook", 
                            background=background_color, 
                            foreground=text_color,
                            
                            bordercolor = background_color,
                            lightcolor=background_color,
                            darkcolor=background_color,
                    )
    
    #Notebook Tabs
    style.configure("TNotebook.Tab", 
                            background=tab_color, 
                            foreground=text_color,
                            bordercolor = border_color,
                            lightcolor = border_color,
                            font= (font_family, font_size, 'bold'), 
                    )
    style.map("TNotebook.Tab", 
                            background=[("active", tab_select_color), ("selected", tab_select_color)],
                            lightcolor=[("disabled", border_color)],
                    )




#------------------------------------Initialize experience required per level at start------------------------------------------------------------

def get_exp(lvl, exp_group): #Exp required for a level and exp group
    """
    Calculates experience needed for a particular level in the selected experience group
    Equations from https://bulbapedia.bulbagarden.net/wiki/Experience

    Parameters
    ----------
    lvl : int between 1 and 100
        Level
    exp_group : str - Fast, Medium Fast, Medium Slow, Slow, Fluctuating, Erratic
        Experience group

    Returns
    -------
    exp_req : int
        Experience required
    """

    exp_req = 0
    if lvl == 1:
        exp_req = 0
    else:
        if exp_group == "Fast":
            exp_req = (4*(lvl**3))/5
        if exp_group == "Medium Fast":
            exp_req = lvl**3        
        if exp_group == "Medium Slow":
            exp_req = (6*(lvl**3))/5 - 15*(lvl**2) + 100*lvl - 140
        if exp_group == "Slow":
            exp_req = (5*(lvl**3))/4
        if exp_group == "Fluctuating":
            if lvl < 15:
                exp_req = ((lvl**3)*(((lvl+1)/3)+24))/50
            if lvl >= 15 and lvl < 36:
                exp_req = ((lvl**3)*(lvl+14))/50
            if lvl > 36:
                exp_req = ((lvl**3)*(((lvl)/2)+32))/50
        if exp_group == "Erratic":
            if lvl < 50:
                exp_req = ((lvl**3)*(100 - lvl))/50
            if lvl >= 50 and lvl < 68:
                exp_req = ((lvl**3)*(150 - lvl))/100
            if lvl >= 68 and lvl < 98:
                exp_req = ((lvl**3)*((1911 - (10*lvl))/3))/500
            if lvl >= 98:
                exp_req = ((lvl**3)*(160 - lvl))/100

    exp_req = math.trunc(exp_req)
    return exp_req

exp_per_lvl_per_expgroup = [0,0,0,0,0,0] #Nested list of exp requirements per level per exp group [exp group][level]
exp_groups = exp_group_names
for x in range(len(exp_groups)): #For each exp group
    lvl=[]
    exp=[]
    for lvl_minus_1 in range (100): #For each level between 1 and 100
        lvl = lvl_minus_1 + 1
        exp_num = get_exp(lvl, exp_groups[x])
        exp.append(exp_num)
    exp_per_lvl_per_expgroup[x] = exp




#---------------------------------------Functions for updating EXP and Level-----------------------------------------------------------------------

def find_exp_group():#Finds and displays EXP group 
    """
    Finds experience group for the selected pokemon and displays it on the [exp_group_show] tkinter label

    Returns
    -------
    sel_exp_group : str
        Exp Group
    """
    pk_selected = pk_combobox.get()
    len_exp_group_list = len(exp_group_list)
    for x in range(len_exp_group_list):
        if pk_selected in exp_group_list[x]:
            sel_exp_group = exp_groups[x]
            exp_group_show.config(text=f'EXP Group:  {sel_exp_group}')
    return sel_exp_group

def get_exp(lvl): #Calcualte exp at input level
    """
    Calculates experience at a specific level

    Parameters
    ----------
    lvl : int between 1 and 100

    Returns
    -------
    curr_exp : int
        Experience at that level
    """
    exp_groups = exp_group_names
    whole_group_sel = exp_group_show.cget("text")
    group_sel = whole_group_sel[12:]
    for x in range(6):
        if exp_groups[x] == group_sel:
            curr_exp = exp_per_lvl_per_expgroup[x][lvl-1]
            break
    return curr_exp

def find_exp_gain(trainer_indexes):#Find list of exp gains
    """
    Finds list of all experience gained

    Parameters
    ----------
    trainer_indexes : list of int
        List of trainers selected
    
    Returns
    -------
    exp_gain : list of int
        List of experience gains corresponding to each trainer
    """

    exp_gain = []
    l = len(trainer_indexes)
    for i in range(l):
        j = trainer_indexes[i]
        exp_gain.append(ttot_exp_list[j])

    return exp_gain

def update_lvl(trainer_indexes): #Calculates and updates level and % to next level
    """
    Calculates the level and percent to next level based on trainers selected.

    Updates [Lvl_label_show] tkinter label with new level

    Updates [lvl_progress] tkinter label with percent to next level

    Parameters
    ----------
    trainer_indexes : list of int
        List of trainers selected

    """

    tot_exp = get_exp(init_lvl) #Initial EXP at starting level (init_lvl)
    tot_exp_list = find_exp_gain(trainer_indexes)

    if tot_exp_list != []: #If at least one trainer battled
        tot_exp = tot_exp + sum(tot_exp_list)
        for x in range(6): #Check each EXP group
            if exp_groups[x] in exp_group_show.cget("text"): #If pokemon in that EXP group
                if tot_exp > exp_per_lvl_per_expgroup[x][99]: #If at max EXP, set level to 100
                    new_lvl = 100
                    percent_to_next_lvl = 0
                else: #If not at max EXP, find level from pre-calculated 2D list (exp_per_lvl_per_expgroup)
                    for lvl_minus_1 in range(100): #
                        if tot_exp >= exp_per_lvl_per_expgroup[x][lvl_minus_1] and tot_exp< exp_per_lvl_per_expgroup[x][lvl_minus_1+1]:
                            new_lvl = lvl_minus_1 + 1
                            exp_over_lvl = tot_exp - exp_per_lvl_per_expgroup[x][lvl_minus_1]
                            exp_to_next_lvl = exp_per_lvl_per_expgroup[x][lvl_minus_1+1]-exp_per_lvl_per_expgroup[x][lvl_minus_1]
                            percent_to_next_lvl = 100*(exp_over_lvl/exp_to_next_lvl)
                            break
                break
    else: #If no trainers battled, level is initial level
        new_lvl = init_lvl
        percent_to_next_lvl = 0

    #Update label for level and level progress bar
    Lvl_label_show.config(text=new_lvl)
    lvl_progress.set(percent_to_next_lvl)
 



#-------------------------------------Functions for updating Stats, EVs and Hidden power----------------------------------------------------------------

def hidden_power_find(): #Calculate hidden power type and power based on IVs
    """
    Calculates hidden power type and power by searching IV boxes.

    Returns
    -------
    hidden_power_type : str
        Type of hidden power
    hidden_power_power : int
        Power of hidden power
    """

    #Get IVs from IV boxes
    iv_value_list = []
    for x in range(6):
        if int(iv_boxes[x].get()) >= 0 and int(iv_boxes[x].get()) <= 31:
            iv_value_list.append(int(iv_boxes[x].get()))
        elif int(iv_boxes[x].get()) > 31:
            iv_boxes[x].delete(0,tk.END)
            iv_boxes[x].insert(0,'31')
            iv_value_list.append(31)
        else:
            iv_boxes[x].delete(0,tk.END)
            iv_boxes[x].insert(0,'0')
            iv_value_list.append(0)

    #Find least significant bits of each IV
    lsb_hp = [] 
    for x in range(6): 
        if iv_value_list[x] % 2 == 0: # 
            lsb_hp.append(0)
        else: 
            lsb_hp.append(1)

    #Calculate type based on least significant bits
    hidden_power_index = math.trunc(((lsb_hp[0]+ 2*lsb_hp[1] + 4*lsb_hp[2] + 8*lsb_hp[3] + 16*lsb_hp[4] + 32*lsb_hp[5])*15)/63)
    hidden_power_type = hidden_power_type_all[hidden_power_index]

    #Find second least significant bits of each IV
    slsb_hp = [] 
    for x in range(6): #Find second least significant bits
        if iv_value_list[x] % 4 == 2 or iv_value_list[x] % 4 == 3: 
            slsb_hp.append(1)
        else:
            slsb_hp.append(0)
    
    #Calculate power based on least significant bits
    hidden_power_power = math.trunc(((slsb_hp[0]+ 2*slsb_hp[1] + 4*slsb_hp[2] + 8*slsb_hp[3] + 16*slsb_hp[4] + 32*slsb_hp[5])*40)/63)+30

    return hidden_power_type, hidden_power_power

def pk_batt_list(trainer_sel_indexes): #Creates list of all pokemon battled and their indexes
    """
    Creates list listof all pokemon battled and their indexes.

    Parameters
    ----------
    trainer_sel_indexes:
        List of all trainers selected

    Returns
    -------
    pk_battled: 
        List of pokemon selected
    pk_battled_index:
        List of pokemon indexes selected
    """

    pk_battled = []#List of all pokemon battled
    pk_battled_index = []#List of individual indexes for all pokemon battled -- Index is 6x index of trainer index + number of slot (0 - 5)
    num_trainers = len(trainer_sel_indexes)
    for i in range(num_trainers):#For each trainer
        trainer_index = trainer_sel_indexes[i]
        for x in range(6):#For each of six potential pokemon
             if tpk_all_list[x][trainer_index] != 0:#If pokemon in that slot
                pk_battled.append(tpk_all_list[x][trainer_index])
                pk_battled_index.append(6*trainer_sel_indexes[i]+x)

    return pk_battled, pk_battled_index
                     
def update_EVs(trainer_sel_indexes, prev_pk_battled_index, theoretical_new_EVs): #Update EVs 
    """
    Calcualtes EVs for new trainers and updates values in EV boxes

    Parameters
    ----------
    trainer_sel_indexes:
        List of all trainer indexes selected after latest selection
    prev_pk_battled_index:           
        List of pokemon indexes selected prior to latest selection
    theoretical_new_EVs:
        6-long list of theoretical EVs prior to latest selection (i.e., ignoring 510 total max or 255 indivudal max)

    Returns
    -------
    prev_pk_battled_index: 
        Updates list of pokemon indexes selected prior to latest selection
    theoretical_new_EVs:
        Updates list of theoretical EVs prior to latest selection
    """

    pk_battled, pk_battled_index = pk_batt_list(trainer_sel_indexes)

    #EVs before latest battle
    prev_EVs = []
    for x in range(6):
        prev_EV_value = int(EV_boxes[x].get())
        prev_EVs.append(prev_EV_value)
    tot_prev_EV = sum(prev_EVs)

    # If total of previous EVs is more than 510, keep previous EVs. Otherwise, calc new EVs
    if True:

        #When adding new trainers
        if len(pk_battled_index) > len(prev_pk_battled_index):
            new_EVs = prev_EVs
            tot_new_EV = tot_prev_EV
            new_pk_battled = []
            for index, value in enumerate(pk_battled_index):
                if value not in prev_pk_battled_index:
                    new_pk_battled.append(pk_battled[index])

            #Find updated total EVs from all pokemon ever battled
            for pok in range(len(new_pk_battled)): #For each pokemon battled
                pok_id = new_pk_battled[pok] #Identify a pokemon

                # Loops for HP->ATT->DEF->SPA->SPD->SPE
                for x in range(6):
                    y = pk_list.index(pok_id) #index of pokemon in Pokemon sheet
                    new_EVs[x] = new_EVs[x] + pk_EV_array[x][y] #Updates EV
                    tot_new_EV = tot_new_EV + pk_EV_array[x][y] # Updates total EV
                    theoretical_new_EVs[x] = theoretical_new_EVs[x] + pk_EV_array[x][y]
                    while new_EVs[x] > 255: #Checks updated EV is not > 255. If so, reduces EV by 1 and loops
                        new_EVs[x] -=  1
                        tot_new_EV -=  1 # Updates total EV
                    while tot_new_EV > 510: #Checks total EVs are not 510 after updating EV. If so, reduces EV by 1 and loops 
                        new_EVs[x] -= 1
                        tot_new_EV -=  1 # Updates total EV

        #When removing trainers
        else:
            new_EVs = [0,0,0,0,0,0]
            for x in range(6):
                new_EVs[x] = theoretical_new_EVs[x]
            tot_new_EV = sum(theoretical_new_EVs)
            no_pk_battled = []
            for index, value in enumerate(prev_pk_battled_index):
                if value not in pk_battled_index:
                    position_pk = 0
                    while value % 6 != 0:
                        value = value -1
                        position_pk = position_pk+1
                    i = int(value/6)
                    no_pk_battled.append(tpk_all_list[position_pk][i])
            

            #Find updated total EVs from all pokemon ever battled
            for pok in range(len(no_pk_battled)): #For each pokemon battled
                pok_id = no_pk_battled[pok] #Identify a pokemon
                y = pk_list.index(pok_id) #index of pokemon in Pokemon sheet

                for x in range(6): # Loops for HP->ATT->DEF->SPA->SPD->SPE
                    tot_new_EV = tot_new_EV - pk_EV_array[x][y] # Updates total EV
                    theoretical_new_EVs[x] = theoretical_new_EVs[x] - pk_EV_array[x][y]

                if sum(theoretical_new_EVs) > 510:#Updates EVs
                    for x in range (6):
                        new_EVs[x] = prev_EVs[x]
                else:
                    for x in range (6):
                        if new_EVs[x] <= 255:
                            new_EVs[x] = theoretical_new_EVs[x]
                        else:
                            new_EVs[x] = 255
            
            tot_new_EV = sum(new_EVs)

        #Update values in EV boxes
        for box in range(6):
            EV_boxes[box].config(state='normal')
            EV_boxes[box].delete(0,tk.END)
            EV_boxes[box].insert(tk.END,new_EVs[box])
            EV_boxes[box].config(state='readonly')
        tot_EV_box.config(text = f'Total EVs:   {tot_new_EV}')

    prev_pk_battled_index = pk_battled_index.copy()

    return prev_pk_battled_index, theoretical_new_EVs

    #Note - Unsure what happens when you have 509 EVs and you battle a pokemon that gives 2+ different EVs (random allocation?).
    #Here, the order is HP->ATT->DEF->SPA->SPD->SPE

def display_stats(trainer_sel_indexes): #Calculates and Updates stats
    """
    Calcualtes stats based on level, base stats for selected pokemon, EVs, IVs and nature.

    Formulas from https://bulbapedia.bulbagarden.net/wiki/Stat
    """

    #Get Nature
    nat_pk = nat_combobox.get()
    
    #Get Level
    lvl_pk_str = Lvl_label_show.cget("text")
    lvl_pk = int(lvl_pk_str)
    
    #Get selected pokemon
    selected_pk = pk_combobox.current()

    #Get IVs
    iv_num_list = []
    for x in range(6):
        if int(iv_boxes[x].get()) >= 0 and int(iv_boxes[x].get()) <= 31:
            iv_num_list.append(int(iv_boxes[x].get()))
        elif int(iv_boxes[x].get()) > 31:
            iv_boxes[x].delete(0,tk.END)
            iv_boxes[x].insert(0,'31')
            iv_num_list.append(31)
        else:
            iv_boxes[x].delete(0,tk.END)
            iv_boxes[x].insert(0,'0')
            iv_num_list.append(0)

    #Get EVs
    ev_num_list = []
    for x in range(6):
        ev_num_list.append(int(EV_boxes[x].get()))

    #Update stats
    if '\n' not in ev_num_list:
        div_trunc_EVs = []

        #Calcualte Stats
        for x in range(6):
            div_trunc_EVs.append(math.trunc(int(ev_num_list[x])/4))
        stat_values = []
        stat_values.append(math.trunc((2*base_stat_list[0][selected_pk] + iv_num_list[0] + div_trunc_EVs[0])*(lvl_pk/100)) + lvl_pk + 10)
        for x in range(5):
            if nat_pk in pos_natures_array[x]:
                stat_values.append(math.trunc((math.trunc((2*base_stat_list[x+1][selected_pk] + iv_num_list[x+1] + div_trunc_EVs[x+1])*(lvl_pk/100)) + 5)*1.1))
            elif nat_pk in neg_natures_array[x]:
                stat_values.append(math.trunc((math.trunc((2*base_stat_list[x+1][selected_pk] + iv_num_list[x+1] + div_trunc_EVs[x+1])*(lvl_pk/100)) + 5)*0.9))
            else:
                stat_values.append(math.trunc((2*base_stat_list[x+1][selected_pk] + iv_num_list[x+1] + div_trunc_EVs[x+1])*(lvl_pk/100)) + 5)
        
        #Badge Boosts
        trainer_names = []
        for index in trainer_sel_indexes:
            trainer_names.append(tname_list[index])

        badge_boost_leaders = ['Roxanne', 'Norman', 'Tate&Liza', 'Wattson']
        for badge_boost_name in badge_boost_leaders:
            for name in trainer_names:
                if badge_boost_name in name:
                    if badge_boost_name == 'Roxanne':
                        stat_values[1] = math.trunc(stat_values[1]*1.1)
                    elif badge_boost_name == 'Norman':
                        stat_values[2] = math.trunc(stat_values[2]*1.1)
                    elif badge_boost_name == 'Tate&Liza':
                        stat_values[3] = math.trunc(stat_values[3]*1.1)
                        stat_values[4] = math.trunc(stat_values[4]*1.1)
                    elif badge_boost_name == 'Wattson':
                        stat_values[5] = math.trunc(stat_values[5]*1.1)

        #Update stat boxes
        for x in range(6):
            stat_boxes[x].config(state='normal')
            stat_boxes[x].delete(0,tk.END)
            stat_boxes[x].insert(0, stat_values[x])
            stat_boxes[x].config(state='readonly')




#------------------------------------Functions for displaying trainers in tabs -----------------------------------------------------------------------

def display_trainer(tab, route, trainer_index_list, mandatory_list, row_start, column_start, max_row, prev_tr): #Displays trainer names for a route
    """
    Displays trainer names with checkboxes for a route. 
    
    Also displays heading with the route name.

    Parameters
    ---------
    tab : Tkinter Frame
        Tab on which to display route
    route : str
        Route for which to display trainers
    trainer_index_list : list of int
        List of trainer indexes for this route
    mandatory_list : list of int
        List of mandatory trainer indexes in this tab
    row_start : int
        Starting row
    column_start : int
        Starting Column
    max_row : int
        Number of rows in the longest route of the tab
    prev_tr: int
        Number of trainers displayed prior to current route

    Returns
    -------
    row_start : int
        Updates starting row for next route in the tab
    column_start : int
        Updates starting column for next route in the tab
    max_row : int
        Updates longest row for next route in the tab
    prev_tr : int
        Updates number of trainers displayed
    """
    
    global checkbox_index

    heading = ttk.Label(tab, text=route)
    heading.grid(row=row_start, column = column_start, columnspan=2, sticky="w", pady = (20,5), padx = (0,10))
    heading.config(font= (font_family, font_size+3, 'bold')) 

    r_r = row_start + 1
    for index, value in enumerate(trainer_index_list): #For each trainer index (value) and each (index) of the list (trainer_index_list)

        #Generate and display checkbox for each trainer and append to (check_vars)
        var=tk.BooleanVar()
        checkbox = tk.Checkbutton(tab, variable= var, command=lambda i = value: checkbox_clicked(i), 
                                    background= background_color, 
                                    activebackground= background_color,
                                    )
        checkbox.grid(row=r_r + index, column = column_start, rowspan=2, padx = 0, sticky = "n")
        checkbox_vars.append(var) #Updates list of checkbox variables
        checkboxes_all.append(checkbox) #Updates list of checkboxes
        trainer_checkbox_index_pairs.append([value, checkbox_index]) #Updates list of tuples trainer-checkbox indexes    
        checkbox_index += 1 #Update checkbox index for next checkbox

        #Generate and display labels for each trainer
        name = tname_list[value]
        if trainer_index_list[index] in mandatory_list:#If mandatory trainer, display text in bold and in mandatory text color
            label = ttk.Label(tab, text=name)
            label.grid(row=r_r + index, column = column_start + 1, sticky="w", padx = (0,10))
            label.config(font= (font_family, font_size, 'bold'), foreground = text_color_mandatory) 
        else:
            label = ttk.Label(tab, text=name)
            label.grid(row=r_r + index, column = column_start + 1, sticky="w", padx = (0,10))  

        #Generate and display EXP for each trainer       
        exp = ttot_exp_list[value]
        label = ttk.Label(tab, text= f"Exp:  {exp}" )
        label.grid(row=r_r + index+1, column = column_start + 1, sticky="nw", padx = (0,10))
        label.config(foreground=text_color_secondary)

        r_r = r_r+1 #Update starting row for next trainer


    #Update maximum row length of the routes for the (tab) based on the current number of rows (curr_row) for this (route)
    curr_row = 2*len(trainer_index_list)
    if max_row > curr_row:
        max_row = max_row
    else:
        max_row = curr_row

    #Set the starting row and column (row_start, column_start) for next route
    if column_start != tot_columns-columns_per_route:        
        column_off = columns_per_route
        row_off = 0
    else:
        column_off = -(tot_columns-columns_per_route)
        row_off = max_row+4
    prev_tr = prev_tr + index+1
    row_start = row_start+row_off
    column_start = column_start + column_off

    return [row_start, column_start, max_row, prev_tr]

def display_routes(tab_name, routes, prev_tr): #Generate new tab and call display_trainer() for all routes
    """
    Generates a tab and calls display_trainer() to display the traines in all routes for that tab.

    Parameters
    ---------
    tab_name : str
        Name of the new tab
    routes : list of str
        Routes to display on new tab
    prev_tr: int
        Number of trainers displayed on prior tabs

    Returns
    -------
    prev_tr : int
        Updates number of trainers displayed
    """
    global checkbox_index

    row_start = 2 #Starting row for a tab
    column_start = 0 #Starting column for a tab

    r_tr_list = [] #Initialize indexes of trainers for a particular route
    mandatory_trainer_tab = [] #Initialize indexes of mandatory trainers for a particular tab
    max_row = 0 #Initialize longest row at 0

    #Initialize new tab (tab)
    tab = ttk.Frame(tabControl)
    tabControl.add(tab, text=tab_name)

    #Display all routes (routes) in the new tab
    trainer_sub_tab = ttk.Frame(tab)
    trainer_sub_tab.grid(row=1)
    num_train_tab = 0
    for x in range(len(routes)):
        route = routes[x]

        #List all trainer indexes (r_tr_list) in a route (route) and update list of displayed trainer indexes (dis_trainer_index)
        for i in range(total_number_trainers): 
            if troute_list[i] == route and tab_list[i] == tab_name:
                trainer_ind = tindex_list[i]
                r_tr_list.append(trainer_ind)
                if tman_list[i] == True:
                    mandatory_trainer_tab.append(trainer_ind)

        #Display all trainers for the route (routes[x]) and return inputs for next route (routes[x+1])
        row_start, column_start, max_row, prev_tr = display_trainer(trainer_sub_tab, route, r_tr_list, mandatory_trainer_tab, row_start, column_start, max_row, prev_tr)

        num_train_tab = num_train_tab + len(r_tr_list)
        r_tr_list = []

    #Buttons to [de]select checkboxes
    button_sub_tab = ttk.Frame(tab)
    button_sub_tab.grid(row=0, sticky="w")

    select_all_button = ttk.Button(button_sub_tab, text="Select All")
    select_all_button.grid(row=0, column = 0, sticky="w")
    select_all_button.bind("<Button>", lambda event: select_all(prev_tr - num_train_tab, prev_tr))

    deselect_all_button = ttk.Button(button_sub_tab, text="Deselect All")
    deselect_all_button.grid(row=0, column = 1, sticky="w")
    deselect_all_button.bind("<Button>", lambda event: deselect_all(prev_tr - num_train_tab, prev_tr))

    select_man_button = ttk.Button(button_sub_tab, text="Select Mandatory")
    select_man_button.grid(row=0, column = 2, sticky="w")
    select_man_button.bind("<Button>", lambda event: select_mandatory(mandatory_trainer_tab))

    return prev_tr

def route_select(tab_name): #Finds all routes for a tab
    """
    Finds all routes for a tab

    Parameters
    ---------
    tab_name : str
        Name of the new tab

    Returns
    -------
    routes_tab : list of str 
        List of routes
    tr_tab : list of int
        List of trainer indexes
    """

    tr_tab = []
    routes_tab = []
    tab_select = data_lists.gymleader_list

    #Find indexes of trainers for that tab
    for x in range(len(tab_select)):
        if tab_select[x] == tab_name:
            tr_tab.append(data_lists.tindex_list.index(x))

    #Find routes for that tab
    for x in range(len(tr_tab)):
        tr_index = tr_tab[x]
        route_name_gym = data_lists.troute_list[tr_index]
        if route_name_gym not in routes_tab:
            routes_tab.append(route_name_gym)

    return routes_tab, tr_tab




#---------------------------------------Aggregated functions for binding to widgets-------------------------------------------------------------------

def checkbox_clicked(input_index): #Functions bound to trainer checkboxes
    """
    When a checkbox is [de]selected, it updates the ordered list of trainers battled (ordered_tr_ind_list[])

    Calls update_EVs(), update_lvl() and display_stats() based on the updated list

    Paramteres
    ----------
    index : int,
        Index of checkbox in checkbox_vars[]

    Returns
    -------
    prev_pk_battled_index : list of int
        List of trainer pokemon indexes selected prior to checkbox being [de]selected
    """
    global prev_pk_battled_index
    global theoretical_new_EVs

    #Gets the checkbox variable for a checkbox based on the trainer index
    for pair in trainer_checkbox_index_pairs:
        if pair[0] == input_index:
            trainer_index = pair[0]
            checkbox_index_test = pair[1]
            is_checked = checkbox_vars[pair[1]]
            break

    #Adds/Removes trainer from the ordered list of trainer indexes which have been selected (ordered_tr_ind_list)
    if is_checked and trainer_index not in ordered_tr_ind_list:
        ordered_tr_ind_list.append(trainer_index)
    elif trainer_index in ordered_tr_ind_list:
        ordered_tr_ind_list.remove(trainer_index)
    else:
        print(f'{tname_list[trainer_index]} not checked.             Trainer Index = {trainer_index}       Checkbox Index = {checkbox_index_test}')#Error message

    prev_pk_battled_index, theoretical_new_EVs = update_EVs(ordered_tr_ind_list, prev_pk_battled_index, theoretical_new_EVs) #Update EVs based on new list
    update_lvl(ordered_tr_ind_list) #Update Level based on new list and new EVs
    display_stats(ordered_tr_ind_list) #Update stats based on new list, new EVs and new level

    return prev_pk_battled_index

def pk_combobox_update(): #Functions bound to pokemon selection combobox
    display_stats(ordered_tr_ind_list)
    find_exp_group()
    update_lvl(ordered_tr_ind_list)

def IV_box_update(): #Functions bound to IV changes
    for x in range(6):
        if iv_boxes[x].get().isdigit():
            continue
        else:
            iv_boxes[x].delete(0,tk.END)
            iv_boxes[x].insert(0,'0')

    display_stats(ordered_tr_ind_list)
    type, power = hidden_power_find()
    hidden_power_box.config(text = f'Hidden Power:   {type}  -  {power}')




#-----------------------------------------------------Select Buttons------------------------------------------------------------------------------------

def select_all(start_index,end_index): #"Select All" Button
    """
    Selects all checkboxes between the start index and the end index

    Parameters
    ----------
    start_index : int
        Index of first checkbox to be selected
    end_index : int
        Index of last checkbox to be selected
    """
    def update_checkboxes_sa_button(start_index,end_index, progress_label, progress_var, close_event): #Set all checkboxes in range to True
        global window_width
        global window_height
        global center_x
        global center_y

        #Adds checkbutton indexes to a list (trainer_index_in_tab_list_test)
        check_box_index_list = []
        trainer_index_in_tab_list_test = []
        for pair in trainer_checkbox_index_pairs:
            if pair[1] >= start_index and pair[1] < end_index:
                check_box_index_list.append(pair[1]) 
                trainer_index_in_tab_list_test.append(pair[0])

        #Variable for loading screen progressbar
        i = 0

        #Checks all checkboxes
        for var in check_box_index_list:
            if checkboxes_all[var].cget('state') != 'disabled':
                if checkbox_vars[var].get() == False:
                    checkboxes_all[var].configure(state= 'normal')
                    checkbox_vars[var].set(True)
                    checkbox_clicked(var)
            i = i+1

            progress_var.set(i)  #Update the progress
            progress_label.config(text=f"Simulating Battles: {math.trunc(100*i/(len(check_box_index_list)))}%")
            if close_event.is_set():  #Check if the window close event has been triggered
                break
        close_event.set()  #Signal that the task is complete

    def loading_screen(start_index, end_index, close_event): #Create loading screen
        loading_popup = tk.Toplevel(main_window)
        window_width, window_height, center_x, center_y = set_window_size_percentage(loading_popup, 0.15, 0.1) 
        loading_popup.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        loading_popup.title("Loading")

        # Progress label and variable
        progress_var = tk.IntVar(value=0)
        progress_label = tk.Label(loading_popup, text="Simulating Battles: 0%")
        progress_label.pack(pady=20)

        # Run the task on a new thread
        threading.Thread(target=update_checkboxes_sa_button, args=(start_index, end_index, progress_label, progress_var, close_event)).start()

        # Continuously check if the task is complete and close the window if so
        def check_completion():
            if close_event.is_set():
                loading_popup.destroy()  # Close the Toplevel window when task is complete
            else:
                loading_popup.after(100, check_completion)  # Check again after 100ms

        check_completion()

    close_event = threading.Event()  # Event to signal task completion or window close
    loading_screen(start_index, end_index, close_event)  # Start the Toplevel window on a thread
    starter_select() #Updates numbers based on the rival started selected

def deselect_all(start_index,end_index): #"Deselect All" Button
    """
    Deselects all checkboxes between the start index and the end index

    Parameters
    ----------
    start_index : int
        Index of first checkbox to be deselected
    end_index : int
        Index of last checkbox to be deselected
    """

    def update_checkboxes_sa_button(start_index,end_index, progress_label, progress_var, close_event): #Set all checkboxes in range to False
        trainer_in_tab_list = []
        trainer_index_in_tab_list_test = []
        for pair in trainer_checkbox_index_pairs:
            if pair[1] >= start_index and pair[1] < end_index:
                trainer_in_tab_list.append(pair[1]) #Adds corresponding checkbutton indexes to a list
                trainer_index_in_tab_list_test.append(pair[0])

        i = 0
        for var in trainer_in_tab_list:
            if checkbox_vars[var].get() == True:
                checkboxes_all[var].configure(state= 'normal')
                checkbox_vars[var].set(False)
                checkbox_clicked(var)
            i = i+1

            progress_var.set(i)  # Update the progress
            progress_label.config(text=f"Simulating Battles: {math.trunc(100*i/(len(trainer_in_tab_list)))}%")
            if close_event.is_set():  # Check if the window close event has been triggered
                break
        close_event.set()  # Signal that the task is complete

    def loading_screen(start_index, end_index, close_event): #Create loading screen
        loading_popup = tk.Toplevel(main_window)
        window_width, window_height, center_x, center_y = set_window_size_percentage(loading_popup, 0.15, 0.1) 
        loading_popup.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        loading_popup.title("Loading")

        # Progress label and variable
        progress_var = tk.IntVar(value=0)
        progress_label = tk.Label(loading_popup, text="Simulating Battles: 0%")
        progress_label.pack(pady=20)

        # Run the task on a new thread
        threading.Thread(target=update_checkboxes_sa_button, args=(start_index, end_index, progress_label, progress_var, close_event)).start()

        # Continuously check if the task is complete and close the window if so
        def check_completion():
            if close_event.is_set():
                loading_popup.destroy()  # Close the Toplevel window when task is complete
            else:
                loading_popup.after(100, check_completion)  # Check again after 100ms

        check_completion()

    close_event = threading.Event()  # Event to signal task completion or window close
    loading_screen(start_index, end_index, close_event)  # Start the Toplevel window on a thread
    starter_select()

def select_mandatory(mandatory_indexes):# Selects mandatory checkboxes
    """
    Selects checkboxes for mandatory trainers

    Parameters
    ----------
    mandatory_indexes : list of int
        Indexes of mandatory trainers to select
    """

    def update_checkboxes_sa_button(mandatory_indexes, progress_label, progress_var, close_event):#Selects all checkboxes for mandatory trainers
        trainer_in_tab_list = []
        trainer_index_in_tab_list_test = []
        for pair in trainer_checkbox_index_pairs:
            if pair[0] in mandatory_indexes:
                trainer_in_tab_list.append(pair[1]) #Adds corresponding checkbutton indexes to a list
                trainer_index_in_tab_list_test.append(pair[0])

        i = 0
        for var in trainer_in_tab_list:
            if checkboxes_all[var].cget('state') != 'disabled':
                if checkbox_vars[var].get() == False:
                    checkboxes_all[var].configure(state= 'normal')
                    checkbox_vars[var].set(True)
                    checkbox_clicked(var)
            i = i+1

            progress_var.set(i)  # Update the progress
            progress_label.config(text=f"Simulating Battles: {math.trunc(100*i/len(mandatory_indexes))}%")
            if close_event.is_set():  # Check if the window close event has been triggered
                break
        close_event.set()  # Signal that the task is complete

    def loading_screen(mandatory_indexes, close_event): #Creates loading screen
        loading_popup = tk.Toplevel(main_window)
        window_width, window_height, center_x, center_y = set_window_size_percentage(loading_popup, 0.15, 0.1) 
        loading_popup.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        loading_popup.title("Loading")

        # Progress label and variable
        progress_var = tk.IntVar(value=0)
        progress_label = tk.Label(loading_popup, text="Simulating Battles: 0%")
        progress_label.pack(pady=20)

        # Run the task on a new thread
        threading.Thread(target=update_checkboxes_sa_button, args=(mandatory_indexes, progress_label, progress_var, close_event)).start()

        # Continuously check if the task is complete and close the window if so
        def check_completion():
            if close_event.is_set():
                loading_popup.destroy()  # Close the Toplevel window when task is complete
            else:
                loading_popup.after(100, check_completion)  # Check again after 100ms

        check_completion()

    close_event = threading.Event()  # Event to signal task completion or window close
    loading_screen(mandatory_indexes, close_event)  # Start the Toplevel window on a thread
    starter_select()

def reset_all():#Resets Level, IVs and EVs to Initial values. Resets all global lists
    global ordered_tr_ind_list, prev_pk_battled_index, theoretical_new_EVs, pk_battled
    
    #Checkbox Reset
    for pair in trainer_checkbox_index_pairs:
        checkboxes_all[pair[1]].configure(state= 'normal')
        checkbox_vars[pair[1]].set(False)

    ordered_tr_ind_list = [] #Indexes of trainers selected in order of selection
    prev_pk_battled_index = [] #Indexes of selected pokemon prior to latest selection - Used to update EVs only for changes in pokemon
    theoretical_new_EVs = [0,0,0,0,0,0] #List of theoretical EVs if no max 510/255 rule - Used for properly udating EVs when deselcting trainers
    pk_battled = [] #List of pokemon for each trainer in order of trainers selected

    #Lvl Reset
    Lvl_label_show.config(text=init_lvl)
    lvl_progress.set(0)

    #IVs Reset
    for x in range(6):
        iv_boxes[x].delete(0,tk.END)
        iv_boxes[x].insert(0,init_iv)

    #EVs Reset
    for x in range(6):
        EV_boxes[x].config(state='normal')
        EV_boxes[x].delete(0,tk.END)
        EV_boxes[x].insert(0,init_ev)
        
    update_EVs(ordered_tr_ind_list,prev_pk_battled_index,theoretical_new_EVs)
    IV_box_update()
    display_stats(ordered_tr_ind_list)
    starter_select()
    
def select_all_mandatory(): #Select all mandatory indexes
    all_mandatory_indexes = []

    for i in range(total_number_trainers): 
        if tman_list[i] == True:
            all_mandatory_indexes.append(tindex_list[i])

    select_mandatory(all_mandatory_indexes)
    
           



#--------------------------------------------------------Root config------------------------------------------------------------------------------------
root = tk.Tk()
root.title(Title)
def set_window_size_percentage(root, width_percent, height_percent):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate the new window size
    window_width = int(screen_width * width_percent)
    window_height = int(screen_height * height_percent)

    center_x = int((screen_width / 2) - (window_width / 2))
    center_y = int((screen_height / 2) - (window_height / 2))

    return window_width, window_height, center_x, center_y
    
window_width, window_height, center_x, center_y = set_window_size_percentage(root, 0.85, 0.7) 
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
set_custom_theme()




#--------------------------------------------------------Resizing Window Border------------------------------------------------------------------------------------
# These definitely weren't worth it for the amount of effort it took, but here now so I'm using it as default


resizing = False
resize_direction = ""
dx = 0
dy = 0

border_width = 3
titlebar_width = 30

border_color = 'black'
corner_color = border_color


#Resizable Border Edges
def bottom_border():#Bottom Resizable Edge
    global window_height, window_width, bottom_resize_frame

    bottom_resize_frame = tk.Frame(root, background=border_color, cursor="sb_v_double_arrow", height=border_width)
    bottom_resize_frame.place(x=border_width, y=window_height - border_width, relwidth=(window_width-(border_width*2))/window_width)

    bottom_resize_frame.bind("<Button-1>", lambda event: start_resize(event, "bottom"))
    bottom_resize_frame.bind("<B1-Motion>", do_resize)
    bottom_resize_frame.bind("<ButtonRelease-1>", stop_resize)

def top_border():#Bottom Resizable Edge
    top_resize_frame = tk.Frame(root, background=border_color, cursor="sb_v_double_arrow", height=border_width)
    top_resize_frame.place(x=0, y=0, relwidth=(window_width-(border_width))/window_width)

    top_resize_frame.bind("<Button-1>", lambda event: start_resize(event, "top"))
    top_resize_frame.bind("<B1-Motion>", do_resize)
    top_resize_frame.bind("<ButtonRelease-1>", stop_resize)

def right_border():#Right Resizable Edge
    global window_width, right_resize_frame
    
    right_resize_frame = tk.Frame(root, background=border_color, cursor="sb_h_double_arrow", width=border_width)
    right_resize_frame.place(x=window_width-border_width, y=border_width, relheight=(window_height-(border_width*2))/window_height)

    right_resize_frame.bind("<Button-1>", lambda event: start_resize(event, "right"))
    right_resize_frame.bind("<B1-Motion>", do_resize)
    right_resize_frame.bind("<ButtonRelease-1>", stop_resize)

def left_border(): #Left Resizable Edge
    left_resize_frame = tk.Frame(root, background=border_color, cursor="sb_h_double_arrow", width=border_width)
    left_resize_frame.place(x=0, y=border_width, relheight=(window_height-(border_width*2))/window_height)

    left_resize_frame.bind("<Button-1>", lambda event: start_resize(event, "left"))
    left_resize_frame.bind("<B1-Motion>", do_resize)
    left_resize_frame.bind("<ButtonRelease-1>", stop_resize)


#Resizable Corners - I cba with top left
def tr_corner():#Bottom Right Corner
    global window_width,window_height, tr_corner_resizer

    tr_corner_resizer = tk.Frame(root, background=corner_color, cursor="bottom_left_corner", height=border_width, width=border_width)
    tr_corner_resizer.place(x=window_width-border_width, y=0)

    tr_corner_resizer.bind("<Button-1>", lambda event: start_resize(event, "top_right"))
    tr_corner_resizer.bind("<B1-Motion>", do_resize)
    tr_corner_resizer.bind("<ButtonRelease-1>", stop_resize)

def br_corner():#Bottom Right Corner
    global window_width,window_height, br_corner_resizer

    br_corner_resizer = tk.Frame(root, background=corner_color, cursor="top_left_corner", height=border_width, width=border_width)
    br_corner_resizer.place(x=window_width-border_width, y=window_height - border_width)

    br_corner_resizer.bind("<Button-1>", lambda event: start_resize(event, "bottom_right"))
    br_corner_resizer.bind("<B1-Motion>", do_resize)
    br_corner_resizer.bind("<ButtonRelease-1>", stop_resize)

def bl_corner():#Bottom Left Corner
    global window_width,window_height, bl_corner_resizer

    bl_corner_resizer = tk.Frame(root, background=corner_color, cursor="top_right_corner", height=border_width, width=border_width)
    bl_corner_resizer.place(x=0, y=window_height - border_width)

    bl_corner_resizer.bind("<Button-1>", lambda event: start_resize(event, "bottom_left"))
    bl_corner_resizer.bind("<B1-Motion>", do_resize)
    bl_corner_resizer.bind("<ButtonRelease-1>", stop_resize)


#Resizing Functions
def start_resize(event, direction):
    global resizing, resize_direction, start_x, start_y, win_width, win_height
    resizing = True
    resize_direction = direction
    start_x = event.x_root
    start_y = event.y_root
    win_width = root.winfo_width()
    win_height = root.winfo_height()

def do_resize(event):
    global dx, dy, bottom_resize_frame, right_resize_frame, br_corner_resizer, bl_corner_resizer, tr_corner_resizer, win_width, win_height

    if resizing and resize_direction:

        ddx = dx - (event.x_root - start_x)
        ddy = dy - (event.y_root - start_y)
        dx = event.x_root - start_x
        dy = event.y_root - start_y
        new_width = win_width
        new_height = win_height
        new_x = root.winfo_x()
        new_y = root.winfo_y()

        # Resize based on the direction
        if "right" in resize_direction:
            new_width += dx
        if "left" in resize_direction:
            new_width -= dx
            new_x -= ddx
        if "bottom" in resize_direction:
            new_height += dy
        if "top" in resize_direction:
            new_height -= dy
            new_y -= ddy
            

        # Set new window size
        root.geometry(f'{new_width}x{new_height}+{new_x}+{new_y}')

        #Update position of borders
        bl_corner_resizer.place(x=0, y=new_height - border_width, height = border_width, width = border_width)
        tr_corner_resizer.place(x=new_width-border_width, y=0, height = border_width, width = border_width)
        br_corner_resizer.place(x=new_width-border_width, y=new_height - border_width, height = border_width, width = border_width)
        bottom_resize_frame.place(x=border_width, y=new_height - border_width, relwidth=(window_width-border_width*2)/window_width)
        right_resize_frame.place(x=new_width-border_width, y=border_width, relheight=(window_height-(border_width*2))/window_height)

def stop_resize(event):
    global resizing, resize_direction, dx, dy
    resizing = False
    resize_direction = ""
    dx = 0
    dy = 0




#---------------------------------------------------------Title Bar--------------------------------------------------------------------------------------

offset_x = 0
offset_y = 0

def on_close():
    root.destroy()

def start_move(event): # Function to initialize the offset when the mouse button is clicked
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def move_window(event): # Function to move the window, using the offset
    x = event.x_root - offset_x
    y = event.y_root - offset_y
    root.geometry(f'+{x}+{y}')

def title_bar():# Title bar
    title_bar = ttk.Frame(root, style = 'TitleBar.TFrame')
    title_bar.place(x=border_width, y=border_width, relwidth=1, height=titlebar_width)

    title_bar.pack_propagate(False)

    # Title
    title_label = ttk.Label(title_bar, text=Title, style = 'TitleBar.TLabel')
    title_label.pack(side="left", padx=10)

    # Close button
    close_button = ttk.Button(title_bar, text="X", style = 'TitleBar.TButton', command=on_close, width = 2)
    close_button.pack(side="right", padx = 2*border_width, fill="y")

    # Bind mouse events to move the window
    title_bar.bind("<Button-1>", start_move)    
    title_bar.bind("<B1-Motion>", move_window)




#---------------------------------------------------------Main Window-----------------------------------------------------------------------------------

if use_custom_titlebar == 'True': #Custom Title Bar
    root.overrideredirect(True)  # Hides the default title bar

    main_window = ttk.Frame(root)
    main_window.place(x=border_width, y=border_width + titlebar_width, relwidth=(window_width-(border_width*2))/window_width, relheight=(window_height-(border_width*2))/window_height)

    left_border()
    title_bar()
    bl_corner()
    bottom_border()
    right_border()
    br_corner()
    top_border()
    tr_corner()
else: #Default OS Title Bar
    main_window = ttk.Frame(root)
    main_window.pack(fill='both', expand='True')

#Show Pokemon List
options = data_lists.pk_list
pk_combobox = ttk.Combobox(main_window, values=options, font= (font_family, font_size, font_weight), width = 33 )
pk_combobox.set(options[0])
pk_combobox.grid(row=0, column = 0, columnspan = 4, padx=pad_x, pady=(10,10), sticky = "w")
pk_combobox.bind("<<ComboboxSelected>>", lambda event: pk_combobox_update())
def update_combobox(event):#Updates list based on typed characters
    typed_text = pk_combobox.get()
    if typed_text == '':
        pk_combobox['values'] = pk_list
    else:
        filtered_options = [item for item in pk_list if typed_text.lower() in item.lower()]
        pk_combobox['values'] = filtered_options

    pk_combobox.delete(0, tk.END) 
    pk_combobox.insert(0, typed_text) 
    pk_combobox.icursor(tk.END)
pk_combobox.bind('<KeyRelease>', update_combobox)

#Show EXP Group
exp_group_show = ttk.Label(main_window)
exp_group_show.grid(row=1, column = 0, columnspan = 4, padx=pad_x, pady=(0,10), sticky="w")

#Show Nature List
nat_combobox = ttk.Combobox(main_window, values=data_lists.natures, font= (font_family, font_size, font_weight), width = 33 )
nat_combobox.set("Brave (+Att, -Speed)")
nat_combobox.grid(row=2, column = 0, columnspan = 4, padx=pad_x, pady=(10,20), sticky = "w")
nat_combobox.bind("<<ComboboxSelected>>", lambda event: display_stats(ordered_tr_ind_list))

#Show Level
Lvl_label = ttk.Label(main_window, text = "Level:", anchor="e")
Lvl_label.grid(row=3, column = 0, padx=3, sticky = "e")

Lvl_label_show = ttk.Label(main_window, text = init_lvl, justify = 'left', anchor="w")
Lvl_label_show.grid(row=3, column = 1, padx=3, sticky = "w")

#Level Progress Bar
lvl_progress = tk.IntVar()
lvl_progressbar = ttk.Progressbar(main_window, orient = 'horizontal', maximum = 100, variable=lvl_progress, length = 260)
lvl_progressbar.grid(row=4, column = 0, columnspan = 4, padx=pad_x, pady = (0,15), sticky = "w")

#EV Boxes and Total EVs label
EV_start_row = 5
EV_boxes = [0,0,0,0,0,0]
ev_name = ["HP EV","Att EV","Def EV", "Sp.A EV","Sp.D EV", "Spe EV"]
for x in range(6):
    if x < 3:
        col_num = 0
    else:
        col_num = 2
    if x < 5 and col_num != 2:
        row_num = x+EV_start_row
    else:
        row_num = (x+EV_start_row)-3
    label = ttk.Label(main_window, text = ev_name[x], anchor="e")
    label.grid(row=row_num, column = col_num, pady=1, sticky = "e")
    EV_boxes[x] = ttk.Entry(main_window, width=4, justify = 'center', font= (font_family, font_size, font_weight))
    EV_boxes[x].grid(row=row_num, column = col_num+1, pady=1)
    EV_boxes[x].insert(0,init_ev)
    EV_boxes[x].config(state='readonly')

tot_new_EV = 0
tot_EV_box = ttk.Label(main_window, text = f'Total EVs:   {tot_new_EV}')
tot_EV_box.grid(row=EV_start_row+3, column = 0, padx=pad_x, pady = (10,25), columnspan=4)

#IV Boxes and Hidden Power Label
IV_start_row = 9
iv_boxes = [0,0,0,0,0,0]
iv_name = ["HP IV","Att IV","Def IV", "Sp.A IV","Sp.D IV", "Spe IV"]
for x in range(6):
    if x < 3:
        col_num = 0
    else:
        col_num = 2
    if x < 5 and col_num != 2:
        row_num = x+IV_start_row
    else:
        row_num = (x+IV_start_row)-3
    label = ttk.Label(main_window, text = iv_name[x], anchor="e")
    label.grid(row=row_num, column = col_num, pady=1, sticky = "e")
    iv_boxes[x] = ttk.Entry(main_window, width=4, justify = 'center', font= (font_family, font_size, font_weight))
    iv_boxes[x].grid(row=row_num, column = col_num+1, pady=1)
    iv_boxes[x].insert(0,init_iv)
    iv_boxes[x].bind("<Return>", lambda event: IV_box_update())

hiddenp_type, hiddenp_power = hidden_power_find()
hidden_power_box = ttk.Label(main_window, text = f'Hidden Power:  {hiddenp_type}  -  {hiddenp_power}')
hidden_power_box.grid(row=IV_start_row+3, column = 0, padx=pad_x, pady = (10,25), columnspan=4)

#Stat Boxes
stat_start_row = 13
stat_boxes = [0,0,0,0,0,0]
stat_name = ["HP","Attack","Defense", "Sp. Attack","Sp. Defense", "Speed"]
for x in range(6):
    if x < 3:
        col_num = 0
    else:
        col_num = 2
    if x < 5 and col_num != 2:
        row_num = x+stat_start_row
    else:
        row_num = (x+stat_start_row)-3
    label = ttk.Label(main_window, text = stat_name[x], anchor="e")
    label.grid(row=row_num, column = col_num,pady=1, sticky = "e")
    stat_boxes[x] = ttk.Entry(main_window, width=4, justify = 'center', font= (font_family, font_size, font_weight))
    stat_boxes[x].grid(row=row_num, column = col_num+1, pady=1)
    stat_boxes[x].config(state='readonly')

#Select Starter
rival_starter_label = ttk.Label(main_window, text = 'Rival Starter',justify = 'left', anchor="w")
rival_starter_label.grid(row=16, column = 0, padx=pad_x, pady = (20,0), columnspan=4,sticky = "w")

starter_list = ['Treecko', 'Torchic', 'Mudkip']
starter_combobox = ttk.Combobox(main_window, values=starter_list, font= (font_family, font_size, font_weight), width = 33 )
starter_combobox .set(init_starter)
starter_combobox .grid(row=17, column = 0, columnspan = 4, padx=pad_x, pady=(0,20), sticky = "w")
starter_combobox .bind("<<ComboboxSelected>>", lambda event: starter_select())
def starter_select():
    global trainer_checkbox_index_pairs, checkboxes_all

    selected_starter = starter_combobox.get()

    selected_rivals = []
    for index, trainer_index in enumerate(tindex_list):
        if tstart_list[index] == selected_starter:
            selected_rivals.append(trainer_index)

    for pair in trainer_checkbox_index_pairs:
        if pair[0] in selected_rivals:
            checkboxes_all[pair[1]].configure(state ='normal')

    non_selected_starters = []
    for starter in starter_list:
        if selected_starter != starter:
            non_selected_starters.append(starter)

    non_selected_rivals = []
    for index, trainer_index in enumerate(tindex_list):
        if tstart_list[index] in non_selected_starters:
            non_selected_rivals.append(trainer_index)

    for pair in trainer_checkbox_index_pairs:
        if pair[0] in non_selected_rivals:
            if checkbox_vars[pair[1]].get() == True:
                checkboxes_all[pair[1]].configure(state ='normal')
                checkbox_vars[pair[1]].set(False)
                checkbox_clicked(pair[1])
            checkboxes_all[pair[1]].configure(state ='disabled')
    
#Reset All Button
reset_button = ttk.Button(main_window, text="Reset")
reset_button.grid(row=18, column = 0,columnspan=4, padx = pad_x, pady=(20,0), sticky="w")
reset_button.bind("<Button>", lambda event: reset_all())

#Select all Mandatory Button
all_mandatory_button = ttk.Button(main_window, text="Select All Mandatory")
all_mandatory_button.grid(row=19, column = 0, columnspan=4, padx = pad_x, sticky="w")
all_mandatory_button.bind("<Button>", lambda event: select_all_mandatory())



#---------------------------------------------------------Tabs--------------------------------------------------------------------------------------------

tabControl = ttk.Notebook(main_window)
tabControl.grid(row=0, column = 5, rowspan= 100, padx = 20)

tab_names = [] #List of tab names
for x in range(len(tab_list)):
    if tab_list[x] not in tab_names:
        tab_names.append(tab_list[x])

index_offset = 0
prev_tr = 0
for x in range(len(tab_names)): #For each tab name, find routes, create a tab and display trainers
    tr_and_routes = route_select(tab_names[x])
    index_offset = display_routes(tab_names[x], tr_and_routes[0], index_offset)
    



#----------------------------------------------------------------------------------------------------------------------------------------------------------

#Initialize Exp group, rivals and stats
find_exp_group()
starter_select()
display_stats(ordered_tr_ind_list)

main_window.mainloop()
