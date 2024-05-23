import pandas as pd
import platform
os_system = platform.system()
# style
font_style = 'Helvetica 30 bold'
cross_font_style = 'Helvetica 40 bold'
background_color = 'black'
# background_color = '#c1c1c0' # original grey background
font_color = 'white'


image_width =  283
image_height = 283


# position variable
# | 1 | 2 | 3 |
# —————————————
# | 4 | 5 | 6 |
# —————————————
# | 7 | 8 | 9 |
imgpos_ninegrid_2_x = 0.5 # 0~1, relative position
imgpos_ninegrid_2_y = 0.2 
imgpos_ninegrid_5_x = 0.5 
imgpos_ninegrid_5_y = 0.5 
imgpos_ninegrid_7_x = 0.25 
imgpos_ninegrid_7_y = 0.7  
imgpos_ninegrid_9_x = 0.75 
imgpos_ninegrid_9_y = 0.7  

# time variable
selected_image_display_time = 2500 # in millisecond, means 2.5 seconds
cross_image_display_time = 2000 # in millisecond, means 2.0 seconds
coin_display_time = 1000 # in millisecond, means 1.0 seconds


# variable may vary from MacOS or WindowsOS
# code for macOS    
if os_system == "Darwin":  # macOS
    # folder path example: /Users/leeliang/Desktop/twostep/
    # must start and end with /
    folder_path = "/Users/leeliang/Desktop/twostep/"
    # Load image
    rocket1_path = folder_path + "image_new/rocket1_norm.jpg"
    rocket2_path = folder_path + "image_new/rocket2_norm.jpg"
    rocket1_X_path = folder_path + "image_new/rocket1_sp.jpg"
    rocket2_X_path = folder_path + "image_new/rocket2_sp.jpg"
    rocket1_act_path = folder_path + "image_new/rocket1_a1.jpg"
    rocket2_act_path = folder_path + "image_new/rocket2_a1.jpg"
    rocket1_deact_path = folder_path + "image_new/rocket1_deact.jpg"
    rocket2_deact_path = folder_path + "image_new/rocket2_deact.jpg"
    alien1_path = folder_path + "image_new/alien1_norm.jpg"
    alien2_path = folder_path + "image_new/alien2_norm.jpg"
    alien3_path = folder_path + "image_new/alien3_norm.jpg"
    alien4_path = folder_path + "image_new/alien4_norm.jpg"
    alien1_act_path = folder_path + "image_new/alien1_a1.jpg"
    alien2_act_path = folder_path + "image_new/alien2_a1.jpg"
    alien3_act_path = folder_path + "image_new/alien3_a1.jpg"
    alien4_act_path = folder_path + "image_new/alien4_a1.jpg"
    alien1_deact_path = folder_path + "image_new/alien1_deact.jpg"
    alien2_deact_path = folder_path + "image_new/alien2_deact.jpg"
    alien3_deact_path = folder_path + "image_new/alien3_deact.jpg"
    alien4_deact_path = folder_path + "image_new/alien4_deact.jpg"
    alien1_X_path = folder_path + "image_new/alien1_sp.jpg"
    alien2_X_path = folder_path + "image_new/alien2_sp.jpg"
    alien3_X_path = folder_path + "image_new/alien3_sp.jpg"
    alien4_X_path = folder_path + "image_new/alien4_sp.jpg"
    coin_path = folder_path + "image_new/t.jpg"
    congrat_path = folder_path + "image_new/congrat.gif"
    payoff_practice_list = pd.read_csv(f"{folder_path}payoff/payoff_practice.csv", index_col = 0).values

# code for Windows
elif os_system == "Windows":
    # folder path example: "C:\\Users\\User\\Downloads\\twostep\\"
    # if "/" doesn't work, change "/" to "\\" probably will do
    folder_path = "C:\\Users\\User\\Downloads\\twostep\\"
    # Load image
    rocket1_path = folder_path + "image_new\\rocket1_norm.jpg"
    rocket2_path = folder_path + "image_new\\rocket2_norm.jpg"
    rocket1_X_path = folder_path + "image_new\\rocket1_sp.jpg"
    rocket2_X_path = folder_path + "image_new\\rocket2_sp.jpg"
    rocket1_act_path = folder_path + "image_new\\rocket1_a1.jpg"
    rocket2_act_path = folder_path + "image_new\\rocket2_a1.jpg"
    rocket1_deact_path = folder_path + "image_new\\rocket1_deact.jpg"
    rocket2_deact_path = folder_path + "image_new\\rocket2_deact.jpg"
    alien1_path = folder_path + "image_new\\alien1_norm.jpg"
    alien2_path = folder_path + "image_new\\alien2_norm.jpg"
    alien3_path = folder_path + "image_new\\alien3_norm.jpg"
    alien4_path = folder_path + "image_new\\alien4_norm.jpg"
    alien1_act_path = folder_path + "image_new\\alien1_a1.jpg"
    alien2_act_path = folder_path + "image_new\\alien2_a1.jpg"
    alien3_act_path = folder_path + "image_new\\alien3_a1.jpg"
    alien4_act_path = folder_path + "image_new\\alien4_a1.jpg"
    alien1_deact_path = folder_path + "image_new\\alien1_deact.jpg"
    alien2_deact_path = folder_path + "image_new\\alien2_deact.jpg"
    alien3_deact_path = folder_path + "image_new\\alien3_deact.jpg"
    alien4_deact_path = folder_path + "image_new\\alien4_deact.jpg"
    alien1_X_path = folder_path + "image_new\\alien1_sp.jpg"
    alien2_X_path = folder_path + "image_new\\alien2_sp.jpg"
    alien3_X_path = folder_path + "image_new\\alien3_sp.jpg"
    alien4_X_path = folder_path + "image_new\\alien4_sp.jpg"
    coin_path = folder_path + "image_new\\t.jpg"
    # practice 
    payoff_practice_list = pd.read_csv(f"{folder_path}payoff\\payoff_practice.csv", index_col = 0).values


####################################################
# instruction text
instruction1_text = """Welcome to the experiment!\n
In this task, you will see pairs of ships and targets. Your job
is to choose one of the ships and then one of the targets.\n
Each type of target has a certain chance of having a piece of gold.\n 
Your aim is to find the target with the highest chance
of having gold, and choose it. Your goal is to win as much gold 
as possible. Press 'space' to continue. 
"""
instruction2_text = """To select the left ship, press the (Left) “2” key.\n 
To select the right ship, press the (Right) “6” key.\n 
The ship you selected will be highlighted. \n 
Press 'space' to continue.
"""
instruction3_text = """After selecting the ship, you'll then be taken to two different "targets".\n
To select the left target, press the (Left) “2” key.\n 
To select the right target, press the (Right) “6” key.\n 
The target you selected will be highlighted. \n 
Press 'space' to continue.
"""
instruction4_text = """If you take too long to make a choice, the trial will end.\n
In that case, you will see red Xs on the screen and a new trial will start.\n
Do not feel rushed, but please try to respond in time on every trial.\n
Press 'space' to continue.
"""
instruction5_text = """After you choose an target,\n
you will learn the result of your choice - whether you get the gold or not.\n
Different targets may have a higher or lower chance of having gold. \n
Your aim is to figure out how to get as much gold as possible during the game.\n
Press 'space' to continue.
"""
practice_text = """Here is the practice section. \n
Remember, your goal is to try to find the target with gold.\n
Press 'space' to continue.
"""
start_text = """Now we will begin the experiment.\n Remember, press (Left) ‘2’ for left item and (Right) ‘6’ for right item.\n
Press waiting or '5' to continue.
"""
pause_text = """The task will continue after a short break.\n
Press '1' to continue whenever you are ready.
"""
probe_phase_text = """Now we will begin the follow up experiment. \n
The aim of this task is to select the target in each pair which is more likely to have gold. \n
This task will be played only once, without any practice.\n
Again, press (Left) ‘2’ for left item and (Right) ‘6’ for right item.\n
Press '1' to continue.
"""
byebye_text = """End of experiment. Thank you for participating. Press 'space' to end.
"""
#############################
probe_phase_list = [
    ["alien1", "alien2"],
    ["alien1", "alien3"],
    ["alien1", "alien4"],
    ["alien2", "alien3"],
    ["alien2", "alien4"],
    ["alien3", "alien4"]
    ]
