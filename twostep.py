import tkinter as tk
import tkinter.messagebox as tmsg
import time
import pandas as pd
pd.set_option("display.precision", 20) # data decimal
from PIL import Image, ImageTk
import random
import threading
import twostep_constants as const # import constants from twostep_constants.py

import platform
os_system = platform.system()
print(f"OS:{os_system}")


# root settings
root = tk.Tk()
root.title("two step task") 
root.attributes('-fullscreen', True) # full screen
#root.geometry("1920x1080+0+0")# width x height + initial x + initial y(+0+0:upper left corner) 
root.configure(bg = 'black')# background color
def quitApp(event):# 按esc推出
    # if 'logs' in globals():
    if len(logs) > 0:
        saveLog()
    else:
        pass
    root.destroy()
root.bind('<Escape>', quitApp)
##################################################
#################### variable ####################
##################################################
image_rocket1 = ImageTk.PhotoImage(Image.open(const.rocket1_path).resize((const.image_width, const.image_height)))# (width, height)
image_rocket2 = ImageTk.PhotoImage(Image.open(const.rocket2_path).resize((const.image_width, const.image_height)))
image_rocket1_act = ImageTk.PhotoImage(Image.open(const.rocket1_act_path).resize((const.image_width, const.image_height)))
image_rocket2_act = ImageTk.PhotoImage(Image.open(const.rocket2_act_path).resize((const.image_width, const.image_height)))
image_rocket1_deact = ImageTk.PhotoImage(Image.open(const.rocket1_deact_path).resize((const.image_width, const.image_height)))
image_rocket2_deact = ImageTk.PhotoImage(Image.open(const.rocket2_deact_path).resize((const.image_width, const.image_height)))
image_rocket1_X = ImageTk.PhotoImage(Image.open(const.rocket1_X_path).resize((const.image_width, const.image_height)))
image_rocket2_X = ImageTk.PhotoImage(Image.open(const.rocket2_X_path).resize((const.image_width, const.image_height)))
image_alien1 = ImageTk.PhotoImage(Image.open(const.alien1_path).resize((const.image_width, const.image_height)))
image_alien2 = ImageTk.PhotoImage(Image.open(const.alien2_path).resize((const.image_width, const.image_height)))
image_alien3 = ImageTk.PhotoImage(Image.open(const.alien3_path).resize((const.image_width, const.image_height)))
image_alien4 = ImageTk.PhotoImage(Image.open(const.alien4_path).resize((const.image_width, const.image_height)))
image_alien1_act = ImageTk.PhotoImage(Image.open(const.alien1_act_path).resize((const.image_width, const.image_height)))
image_alien2_act = ImageTk.PhotoImage(Image.open(const.alien2_act_path).resize((const.image_width, const.image_height)))
image_alien3_act = ImageTk.PhotoImage(Image.open(const.alien3_act_path).resize((const.image_width, const.image_height)))
image_alien4_act = ImageTk.PhotoImage(Image.open(const.alien4_act_path).resize((const.image_width, const.image_height)))
image_alien1_deact = ImageTk.PhotoImage(Image.open(const.alien1_deact_path).resize((const.image_width, const.image_height)))
image_alien2_deact = ImageTk.PhotoImage(Image.open(const.alien2_deact_path).resize((const.image_width, const.image_height)))
image_alien3_deact = ImageTk.PhotoImage(Image.open(const.alien3_deact_path).resize((const.image_width, const.image_height)))
image_alien4_deact = ImageTk.PhotoImage(Image.open(const.alien4_deact_path).resize((const.image_width, const.image_height)))
image_alien1_X = ImageTk.PhotoImage(Image.open(const.alien1_X_path).resize((const.image_width, const.image_height)))
image_alien2_X = ImageTk.PhotoImage(Image.open(const.alien2_X_path).resize((const.image_width, const.image_height)))
image_alien3_X = ImageTk.PhotoImage(Image.open(const.alien3_X_path).resize((const.image_width, const.image_height)))
image_alien4_X = ImageTk.PhotoImage(Image.open(const.alien4_X_path).resize((const.image_width, const.image_height)))
orig_image_coin = Image.open(const.coin_path).resize((const.image_width, const.image_height))
image_coin = ImageTk.PhotoImage(orig_image_coin)
image_congrat = tk.PhotoImage(const.congrat_path)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# initialize variables
score = 0
current_counter = 0
probe_counter = 0
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
cross_length = 50

save_data = [] # store main experiment
save_data_probe = [] # store probe phase
current_page = 1
coin_label = None
logs = []
logs.append(f"OS:{os_system}\n") # save operation system
##################################################
################ function ########################
##################################################
# clear all widgets from root
def clearScreen():
    for widget in root.winfo_children():
        widget.destroy()

##################################################
##################################################
##################################################
# Save ID to login data dictionary and go on to instruction page
def saveId():
    global global_save_file_name, login_space, f
    login_time = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
    login_ID = entry_id.get()
    login_session = entry_session.get()
    login_space = var_space.get()
    global_save_file_name = f'{const.folder_path}{login_ID}_{login_session}_{login_space}_{login_time}'
    
    log_path = global_save_file_name + '_log.txt'
    f = open(log_path, 'w')    
    
    # check entry empty
    if (entry_id.get() == "") or (entry_session.get() == "") or (var_space.get() == ""):
        tmsg.showinfo("Error!","Not complete!")
        print("Input Error")
        logs.append("Input Error\n")
    else: # go to instruction page
        print(f'| {login_ID} | {login_session} | {login_space} |')
        logs.append(f'| {login_ID} | {login_session} | {login_space} |\n')
        print("===============================")
        root.after(0, lambda: instructionPage(current_page))
def saveLog():
    if len(logs) > 1:# already save OS, so start from 1
        f.writelines(logs)
        f.close()
    else:
        pass
def coinAnimation(label, orig_image, steps=20, delay=10):
    max_scale = 1.0  # full size
    min_scale = 0.1  # start/end size
    def zoom_in(current_step):
        # Calculate current scale for zooming in
        scale = min_scale + (max_scale - min_scale) * (current_step / steps)
        new_width = int(orig_image.width * scale)
        new_height = int(orig_image.height * scale)
        # Ensure width and height are > 0
        new_width = max(new_width, 1)
        new_height = max(new_height, 1)
        # Resize image
        resized_image = orig_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(resized_image)
        label.config(image=photo_image)
        label.image = photo_image  # Keep a reference to avoid garbage collection
        label.place(relx = const.imgpos_ninegrid_2_x, rely = const.imgpos_ninegrid_2_y, anchor="center")

        # Continue the animation until the final step
        if current_step < steps:
            label.after(delay, lambda: zoom_in(current_step + 1))
    zoom_in(0)
    # def zoom_out(current_step):
    #     # Calculate current scale for zooming out
    #     scale = max_scale - (max_scale - min_scale) * (current_step / steps)
    #     new_width = int(orig_image.width * scale)
    #     new_height = int(orig_image.height * scale)
    #     # Ensure width and height are > 0
    #     new_width = max(new_width, 1)
    #     new_height = max(new_height, 1)
    #     # Resize the image
    #     resized_image = orig_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    #     photo_image = ImageTk.PhotoImage(resized_image)
    #     label.config(image=photo_image)
    #     label.image = photo_image  # Keep a reference to avoid garbage collection
    #     # Center the image
    #     label.place(relx = const.imgpos_ninegrid_2_x, rely = const.imgpos_ninegrid_2_y, anchor="center")
    #     # Continue the animation until the final step
    #     if current_step < steps:
    #         label.after(delay, lambda: zoom_out(current_step + 1))
    # # Start the zoom-out animation
    # zoom_out(0)
def congratGifAnimation():
    def updateFrame(index):
        if not keep_animating:
            return  # Stop the animation
        try:
            frame = tk.PhotoImage(file=const.congrat_path, format=f"gif -index {index}")
            gif_label.config(image=frame)
            gif_label.image = frame  # Keep a reference
            root.after(frame_delay, lambda: updateFrame((index+1) % frame_count))
        except tk.TclError:
            pass  # This can occur when the window is closed before the animation completes

    def stop_animation():
        global keep_animating
        keep_animating = False
        gif_label.config(image=None)  # Clear the label
    
    
    keep_animating = True

    image_congrat = tk.PhotoImage(const.congrat_path)
    gif_label = tk.Label(root, image=image_congrat, bg = const.background_color)
    gif_label.place(relx = const.imgpos_ninegrid_2_x, rely = 0.15, anchor="center")# show_coin_label
    
    frame_delay = 100  # Milliseconds between frames
    frame_count = 10
    updateFrame(0)
    root.after(1000, stop_animation)
##################################################
def instructionPage(current_page): 
    global payoff_list, probability_alien1, probability_alien2, probability_alien3, probability_alien4, max_iterations
    clearScreen()
    root.config(cursor="none") # hide mouse
    
    # read payoff data from file
    if os_system == "Darwin":  # macOS
        payoff_list = pd.read_csv(f"{const.folder_path}payoff/payoff_{login_space}.csv", index_col = 0).values
    elif os_system == "Windows": # Windows
        payoff_list = pd.read_csv(f"{const.folder_path}payoff\\payoff_{login_space}.csv", index_col = 0).values
    max_iterations = len(payoff_list)
    
    def setup_instruction1():# rocket1, rocket2
        clearScreen()
        tk.Label(root, text = const.instruction1_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")# instruction1_label
        tk.Label(root, image = image_rocket1).place(relx=0.25, rely=0.8, anchor="center")# tk_rocket1_img_label
        tk.Label(root, image = image_rocket2).place(relx=0.75, rely=0.8, anchor="center")# tk_rocket2_img_label
    def setup_instruction2():# rocket1_act, rocket2_act
        clearScreen()
        tk.Label(root, text = const.instruction2_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")# instruction2_label
        tk.Label(root, image = image_rocket1_act).place(relx=0.25, rely=0.8, anchor="center")# tk_rocket1_act_img_label
        tk.Label(root, image = image_rocket2_act).place(relx=0.75, rely=0.8, anchor="center")# tk_rocket2_act_img_label
    def setup_instruction3():# alien1_act, alien2_act
        clearScreen()
        tk.Label(root, text = const.instruction3_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")# instruction2_label
        tk.Label(root, image = image_alien1_act).place(relx=0.25, rely=0.8, anchor="center")# tk_rocket1_act_img_label
        tk.Label(root, image = image_alien2_act).place(relx=0.75, rely=0.8, anchor="center")# tk_rocket2_act_img_label
    def setup_instruction4():# rocket1_cross, rocket2_cross
        clearScreen()
        tk.Label(root, text = const.instruction4_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")# instruction3_label
        tk.Label(root, image = image_rocket1_X).place(relx=0.25, rely=0.8, anchor="center")# tk_rocket1_cross_img_label
        tk.Label(root, image = image_rocket2_X).place(relx=0.75, rely=0.8, anchor="center")# tk_rocket2_cross_img_label
    def setup_instruction5():# coin
        clearScreen()
        tk.Label(root, text = const.instruction5_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")# instruction4_label
        tk.Label(root, image = image_coin).place(relx=0.5, rely=0.8, anchor="center")# coin_img_label
    def setup_instruction6():# ready for practice
        clearScreen()
        tk.Label(root, text = const.practice_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")
    def setup_instruction7():# ready for start
        clearScreen()
        tk.Label(root, text = const.start_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")
    def setup_instruction8():# pause page
        clearScreen()
        tk.Label(root, text = const.pause_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")
    def setup_instruction9():# ready for probe phase
        clearScreen()
        tk.Label(root, text = const.probe_phase_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.4, anchor="center")
    
    def on_key_press(event):
        global current_page
        if event.keysym == 'space':
            if current_page == 6:# ready for practice 
                root.unbind("<Key-space>")
                mainExperiment(len(const.payoff_practice_list), "pract", None)
            elif current_page < 6:
                current_page += 1
                page_functions[current_page - 1]()
            else:
                pass  # After Page 7, do nothing for space key
    def on_key_press_5(event):
        global current_counter, score
        if event.char == '5' and current_page == 7: # ready for main experiment
            root.unbind("<Key-space>")
            root.unbind('<KeyPress-5>')
            start_main_time = time.time()
            print(f"key5 start time:{start_main_time}")
            logs.append(f"key5 start time:{start_main_time}\n")
            current_counter = 0
            score = 0
            mainExperiment(max_iterations, "main", start_main_time)
    def on_key_press_1(event):
        global current_counter
        if event.char == '1' and current_page == 8: # pause page
            start_pause_time = time.time()
            print(f"break end exp start time:{start_pause_time}")
            logs.append(f"break end exp start time:{start_pause_time}\n")
            root.unbind("<Key-space>")
            root.unbind('<KeyPress-5>')
            root.unbind('<KeyPress-1>')
            current_counter += 1
            mainExperiment(max_iterations, "main", start_pause_time)
        elif event.char == '1' and current_page == 9:# ready for probe phase
            root.unbind("<Key-space>")
            root.unbind('<KeyPress-5>')
            root.unbind('<KeyPress-1>')
            probePhase()
            
    def quitApp(event):
        if 'logs' in globals():
            saveLog()
        else:
            pass
        root.destroy()
    page_functions = [setup_instruction1, setup_instruction2, 
                      setup_instruction3, setup_instruction4, 
                      setup_instruction5, setup_instruction6] 
                    #   setup_instruction7, setup_instruction8, 
                    #   setup_instruction9]

    root.bind('<KeyPress-space>', on_key_press)
    root.bind('<KeyPress-5>', on_key_press_5)
    root.bind('<KeyPress-1>', on_key_press_1)
    
    if current_page == 1:
        setup_instruction1()
    elif current_page == 7:
        setup_instruction7()
    elif current_page == 8:
        setup_instruction8()
    elif current_page == 9:
        setup_instruction9()

def mainExperiment(max_iterations, status,start_main_time):
    def incrementCounter(success_fail_state):
        global current_counter
        if success_fail_state == False:
            print(f"{status} trial {current_counter} fail!")
            logs.append(f"{status} trial {current_counter} fail!\n")
        elif success_fail_state == True:    
            save_data.append([current_counter, 
                            probability_alien1, 
                            probability_alien2, 
                            probability_alien3, 
                            probability_alien4,  
                            current_alien_images,
                            key1, key2, comrar,
                            select_rocket_time, select_alien_time,
                            rt1, rt2, 
                            win_lose_state, score,
                            start_main_time])
            df = pd.DataFrame(save_data, columns=['Trial', 
                                                'p1', 'p2', 'p3', 'p4', 
                                                'transition', 
                                                'key1', 'key2', 'com/rar',
                                                'rocket_select_time', 'alien_select_time', 
                                                'rt1', 'rt2', 
                                                "winorlose", "totalgold", 
                                                "start_time"])
            df.to_csv(global_save_file_name + '.csv', index=False)
            # print(f"save trial:{current_counter}, status:{status}")
            logs.append(f"save trial:{current_counter}, status:{status}\n")
        
        # pause trial
        if (current_counter in [max_iterations//3, max_iterations*2//3]) and (status == "main"):# [69, 139] means trial 70 and 140
            print(f"trial {current_counter}:ready for break")
            logs.append(f"trial {current_counter}:ready for break\n")
            current_page = 8
            instructionPage(current_page)
        else:
            current_counter += 1
            
            if current_counter < max_iterations:
                displayRocketImages()  # Start the next cycle
            else:
                displayFinalScore()  # Or any other final action
            
    # display final score
    def displayFinalScore():
        global current_page
        clearScreen()
        tk.Label(root, text = f"You have earned {score} gold.", font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# Position 5 # final_score_label
        if status == "pract":
            current_page = 7
            instructionPage(current_page) # go to ready to start instruction
        elif (current_counter == max_iterations) and (status == "main"):
            current_page = 9
            instructionPage(current_page)# go to probe phase instruction
            
    # display images rocket1 and rocket2 side by side
    def displayRocketImages():
        global current_counter, key_pressed, start_rocket_time, probability_alien1, probability_alien2, probability_alien3, probability_alien4
        # start of main experiment 
        
        # set p1~p4
        if status == "pract":
            probability_alien1 = const.payoff_practice_list[current_counter][0] # Probabilities for scoring after selecting each B image
            probability_alien2 = const.payoff_practice_list[current_counter][1]
            probability_alien3 = const.payoff_practice_list[current_counter][2]
            probability_alien4 = const.payoff_practice_list[current_counter][3]
        elif status == "main":
            probability_alien1 = payoff_list[current_counter][0] # Probabilities for scoring after selecting each B image
            probability_alien2 = payoff_list[current_counter][1]
            probability_alien3 = payoff_list[current_counter][2]
            probability_alien4 = payoff_list[current_counter][3]

        key_pressed = False
        clearScreen()
        tk.Label(root, image=image_rocket1).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# Position 7# label_rocket1
        tk.Label(root, image=image_rocket2).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# Position 9# label_rocket2
        start_rocket_time = time.time()
                
        # handle rocket key press
        def rocketKeyPress(event):
            global key_pressed, key1, rt1, select_rocket_time
            key1 = event.char
            select_rocket_time = time.time()
            rt1 = select_rocket_time - start_rocket_time
            if event.char in ["2", "6"]:
                key_pressed = True
                timer_rocket.cancel()
                selectRocketImage("rocket1" if event.char == "2" else "rocket2")
                root.unbind("<Key>")
        
        root.bind("<Key>", rocketKeyPress)
        timer_rocket = threading.Timer(3, displayRocketX)
        timer_rocket.daemon = True
        timer_rocket.start()
        
    def dontDetect(event):
        pass

    def displayRocketX():
        global key_pressed, current_counter
        if not key_pressed:
            clearScreen()
            tk.Label(root, image = image_rocket1_X).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# rocket1_X_label
            tk.Label(root, image = image_rocket2_X).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# rocket1_X_label
            root.bind("<Key>", dontDetect)
            root.after(const.cross_image_display_time, lambda: incrementCounter(False)) 
        
    # after slecting A image Function to handle key presses for A images
    def selectRocketImage(selected_rocket):
        clearScreen()
        if selected_rocket == "rocket1":
            tk.Label(root, image = image_rocket1_act).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# selected_label
            tk.Label(root, image = image_rocket2_deact).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# deact_label
            root.after(const.selected_image_display_time, lambda: displayAlienImages("rocket1"))
        elif selected_rocket == "rocket2":
            tk.Label(root, image = image_rocket2_act).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# selected_label
            tk.Label(root, image = image_rocket1_deact).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# deact_label
            root.after(const.selected_image_display_time, lambda: displayAlienImages("rocket2"))

    # Function to display images alien_left and alien_right side by side
    def displayAlienImages(selected_rocket):
        global key_pressed, current_alien_images, start_alien_time, timer_alien, comrar
        key_pressed = False
        clearScreen()
        if selected_rocket == "rocket1":
            current_alien_images, comrar = (['alien1', 'alien2'], "common") if random.random() <= 0.7 else (['alien3', 'alien4'], "rare")# 70% alien12; 30% alien34
            tk.Label(root, image = image_rocket1_deact).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# rocket1_deact_label
        elif selected_rocket == "rocket2":
            current_alien_images, comrar = (['alien1', 'alien2'], "rare") if random.random() <= 0.3 else (['alien3', 'alien4'], "common")# 70% alien34; 30% alien12
            tk.Label(root, image = image_rocket2_deact).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# rocket2_deact_label

        tk.Label(root, image = globals()["image_" + current_alien_images[0]]).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# label_alien_left
        tk.Label(root, image = globals()["image_" + current_alien_images[1]]).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# label_alien_right
        start_alien_time = time.time()
        
        def alienKeyPress(event):
            global key_pressed, key2, rt2, select_alien_time
            key2 = event.char
            select_alien_time = time.time()
            rt2 = select_alien_time - start_alien_time
            if event.char == "2" or event.char == "6":
                key_pressed = True
                timer_alien.cancel()
                selectAlienImage(current_alien_images[0] if event.char == "2" else current_alien_images[1])
                root.unbind("<Key>")
                

        root.bind("<Key>", alienKeyPress)
        timer_alien = threading.Timer(3, displayAlienX)
        timer_alien.daemon = True
        timer_alien.start()

    def displayAlienX():
        global key_pressed, current_counter
        if not key_pressed:
            clearScreen()
            tk.Label(root, image = globals()["image_" + current_alien_images[0] + "_X"]).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# Position 7
            tk.Label(root, image = globals()["image_" + current_alien_images[1] + "_X"]).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# Position 9
            root.bind("<Key>", dontDetect)
            root.after(const.cross_image_display_time, lambda: incrementCounter(False))    

        
    # Function to handle key presses for B images
    def selectAlienImage(chosen_alien):
        global win_lose_state 
        clearScreen()
        if chosen_alien == "alien1" or chosen_alien == "alien3":
            tk.Label(root, image = globals()["image_" + current_alien_images[0] + "_act"]).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# selected_label
            tk.Label(root, image = globals()["image_" + current_alien_images[1] + "_deact"]).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# not_selected_label
            win_lose_state = updateScore(globals()["probability_" + current_alien_images[0]])
        
        elif chosen_alien == "alien2" or chosen_alien == "alien4":
            tk.Label(root, image = globals()["image_" + current_alien_images[1] + "_act"]).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# selected_label
            tk.Label(root, image = globals()["image_" + current_alien_images[0] + "_deact"]).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# not_selected_label
            win_lose_state = updateScore(globals()["probability_" + current_alien_images[1]])
        else:
            return    
        root.after(const.selected_image_display_time, lambda: showCoin(win_lose_state,chosen_alien))
        
    def showCoin(win_lose_state,chosen_alien): 
        global coin_label
        clearScreen()
        tk.Label(root, image = globals()["image_" + chosen_alien + "_deact"]).place(relx = const.imgpos_ninegrid_5_x, rely = const.imgpos_ninegrid_5_x, anchor="center")# selected_deact_label
        if win_lose_state == 1: # win
            # tk.Label(root, image = image_coin).place(relx = const.imgpos_ninegrid_2_x, rely = const.imgpos_ninegrid_2_y, anchor="center")# show_coin_label
            congratGifAnimation()
            coin_label = tk.Label(root, image = image_coin)
            coin_label.place(relx = const.imgpos_ninegrid_2_x, rely = const.imgpos_ninegrid_2_y, anchor="center")# show_coin_label
            coin_label.image = image_coin  # keep reference
            tk.Label(root, text = f"{score} gold!!", font = const.font_style, bg="white", fg= "red").place(relx = const.imgpos_ninegrid_2_x, rely = const.imgpos_ninegrid_2_y, anchor="center")# current_score_label
            coinAnimation(coin_label, orig_image_coin)# start zoom-in animation
        root.after(const.coin_display_time, lambda: incrementCounter(True))

    # Function to update the score
    def updateScore(probability):
        global score
        if random.random() < probability:
            score += 1
            return 1 # win
        else:
            return 0 # lose

    displayRocketImages()

def probePhase():
    def show_cross():    
        clearScreen()
        tk.Label(root, text="+", font = const.cross_font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.5, anchor="center")# +
        timer_probe_alien = threading.Timer(1, displayProbeAlienImages)
        timer_probe_alien.daemon = True
        timer_probe_alien.start()

    def displayProbeAlienImages():
        global start_probe_alien_time, probe_alien_pair
        clearScreen()
        probe_alien_pair = const.probe_phase_list[probe_counter % len(const.probe_phase_list)]
        tk.Label(root, image=globals()["image_" + probe_alien_pair[0]]).place(relx = const.imgpos_ninegrid_7_x, rely = const.imgpos_ninegrid_7_y, anchor="center")# Position 7
        tk.Label(root, image=globals()["image_" + probe_alien_pair[1]]).place(relx = const.imgpos_ninegrid_9_x, rely = const.imgpos_ninegrid_9_y, anchor="center")# Position 9
        start_probe_alien_time = time.time()
        root.bind("2", lambda e: save_selection_and_proceed("2"))
        root.bind("6", lambda e: save_selection_and_proceed("6"))
        
    def save_selection_and_proceed(key):
        global probe_counter
        probe_rt = time.time() - start_probe_alien_time
        save_data_probe.append([probe_alien_pair[0], probe_alien_pair[1], key, probe_rt])
        probe_df = pd.DataFrame(save_data_probe, columns=['probe_left', 'probe_right', 'probe_key', 'probe_rt'])
        probe_df.to_csv(global_save_file_name + '_probe.csv', index=False)
        print(f"save trial:{probe_counter}, status:probe")
        logs.append(f"save trial:{probe_counter}, status:probe\n")

        probe_counter += 1
        if probe_counter < len(const.probe_phase_list)*5:
            show_cross()
        else:
            show_end_text()

    def show_end_text():
        clearScreen()
        tk.Label(root, text = const.byebye_text, font = const.font_style, bg=const.background_color, fg= const.font_color).place(relx=0.5, rely=0.5, anchor="center")# +
        root.unbind('<Key>')
        root.bind("<space>", quitApp)
    show_cross()
##################################################
################### login page ###################
##################################################
# Configure the grid layout for root
root.grid_columnconfigure(1, weight=3)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=3)
root.grid_rowconfigure(3, weight=3)
root.grid_rowconfigure(4, weight=3)
root.grid_rowconfigure(5, weight=1)
# create four frames: frame_ID, frame_session, frame_space, frame_next
frame_empty_top = tk.Frame(root, bg = const.background_color)
frame_ID = tk.Frame(root, bg = const.background_color)
frame_session = tk.Frame(root, bg = const.background_color)
frame_space = tk.Frame(root, bg = const.background_color)
frame_confirm = tk.Frame(root, bg = const.background_color)
frame_next = tk.Frame(root, bg = const.background_color)
frame_empty = tk.Frame(root, bg = const.background_color)
# frame position
frame_empty_top.grid(row=0, column=0, columnspan=2, sticky="nsew")
frame_ID.grid(row=1, column=0, columnspan=2, sticky="nsew")
frame_session.grid(row=2, column=0, columnspan=2, sticky="nsew")
frame_space.grid(row=3, column=0, columnspan=2, sticky="nsew")
frame_confirm.grid(row=4, column=0, columnspan=2, sticky="nsew")
frame_next.grid(row=5, column=0, columnspan=2, sticky="nsew")
frame_empty.grid(row=6, column=0, columnspan=2, sticky="nsew")

for frame in [frame_ID, frame_session, frame_space, frame_confirm, frame_next]:
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

# frame_ID
label_id = tk.Label(frame_ID, bg = const.background_color, text="Enter participant:", font = const.font_style, fg= const.font_color)
entry_id = tk.Entry(frame_ID, 
                    insertontime = 0, 
                    width=30, 
                    font = const.font_style, 
                    bg = "grey",
                    bd = 2, 
                    highlightbackground='red')
entry_id.focus() # can type ID without mouse clicking 

# frame_session
label_session = tk.Label(frame_session, bg = const.background_color, text="Enter session:", font = const.font_style, fg= const.font_color)
entry_session = tk.Entry(frame_session, 
                         insertontime = 0, 
                         width=30, 
                         font = const.font_style, 
                         bg = "grey",
                         bd = 2, 
                         highlightbackground='red')

# frame_space
var_space = tk.StringVar() # space variable

# button press UI
def space_selected(selected_button):
    ID = entry_id.get()
    session = entry_session.get()
    label_block_selected.configure(text = f"Participant:{ID}\nsession:{session}\nspace:{selected_button}")
    if selected_button == "test1":
        button_space_test1.configure(foreground = "white", background = "red")
        button_space_1.configure(foreground = "grey", background = "black")
        button_space_2.configure(foreground = "grey", background = "black")
        button_space_3.configure(foreground = "grey", background = "black")
        button_space_4.configure(foreground = "grey", background = "black")
        button_space_5.configure(foreground = "grey", background = "black")
    elif selected_button == "1":
        button_space_test1.configure(foreground = "grey", background = "black")
        button_space_1.configure(foreground = "white", background = "red")
        button_space_2.configure(foreground = "grey", background = "black")
        button_space_3.configure(foreground = "grey", background = "black")
        button_space_4.configure(foreground = "grey", background = "black")
        button_space_5.configure(foreground = "grey", background = "black")
    elif selected_button == "2":
        button_space_test1.configure(foreground = "grey", background = "black")
        button_space_1.configure(foreground = "grey", background = "black")
        button_space_2.configure(foreground = "white", background = "red")
        button_space_3.configure(foreground = "grey", background = "black")
        button_space_4.configure(foreground = "grey", background = "black")
        button_space_5.configure(foreground = "grey", background = "black")
    elif selected_button == "3":
        button_space_test1.configure(foreground = "grey", background = "black")
        button_space_1.configure(foreground = "grey", background = "black")
        button_space_2.configure(foreground = "grey", background = "black")
        button_space_3.configure(foreground = "white", background = "red")
        button_space_4.configure(foreground = "grey", background = "black")
        button_space_5.configure(foreground = "grey", background = "black")
    elif selected_button == "4":
        button_space_test1.configure(foreground = "grey", background = "black")
        button_space_1.configure(foreground = "grey", background = "black")
        button_space_2.configure(foreground = "grey", background = "black")
        button_space_3.configure(foreground = "grey", background = "black")
        button_space_4.configure(foreground = "white", background = "red")
        button_space_5.configure(foreground = "grey", background = "black")
    elif selected_button == "5":
        button_space_test1.configure(foreground = "grey", background = "black")
        button_space_1.configure(foreground = "grey", background = "black")
        button_space_2.configure(foreground = "grey", background = "black")
        button_space_3.configure(foreground = "grey", background = "black")
        button_space_4.configure(foreground = "grey", background = "black")
        button_space_5.configure(foreground = "white", background = "red")

## create button in space frame
## cursor shape:https://docstore.mik.ua/orelly/perl3/tk/ch23_02.htm
label_space = tk.Label(frame_space, bg = const.background_color, text="Select space:", font = const.font_style, fg= const.font_color)
button_space_test1 = tk.Radiobutton(frame_space, text = "test1", variable = var_space, value="test1", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("test1"))
button_space_1 = tk.Radiobutton(frame_space, text = "  1  ", variable = var_space, value="1", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("1"))
button_space_2 = tk.Radiobutton(frame_space, text = "  2  ", variable = var_space, value="2", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("2"))
button_space_3 = tk.Radiobutton(frame_space, text = "  3  ", variable = var_space, value="3", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("3"))
button_space_4 = tk.Radiobutton(frame_space, text = "  4  ", variable = var_space, value="4", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("4"))
button_space_5 = tk.Radiobutton(frame_space, text = "  5  ", variable = var_space, value="5", font = const.font_style, indicatoron=False, selectcolor="yellow",cursor="draft_large", command=lambda: space_selected("5"))

# frame_next
label_block_selected = tk.Label(frame_confirm,bg = "gold", fg = "grey5", text="", font = const.font_style, justify = "left")
button_next = tk.Button(frame_next, text="Next", command=saveId, font = const.font_style)
label_empty = tk.Label(frame_empty, bg = const.background_color, text="          ", font = const.font_style)
label_empty_top = tk.Label(frame_empty_top, bg = const.background_color, text="          ", font = const.font_style)
# element position in frame
label_id.grid(row=0, column=0, sticky = tk.E)
entry_id.grid(row=0, column=1)
label_session.grid(row=0, column=0, pady=10, sticky = tk.E)
entry_session.grid(row=0, column=1, pady=10)
label_space.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky = tk.E)
button_space_test1.grid(row=0, column=1, ipadx=15, ipady=5, sticky = tk.E)# 
button_space_1.grid(row=0, column=2, ipadx=25, ipady=5)
button_space_2.grid(row=0, column=3, ipadx=25, ipady=5, sticky = tk.W)
button_space_3.grid(row=1, column=1, ipadx=25, ipady=5, sticky = tk.E)
button_space_4.grid(row=1, column=2, ipadx=25, ipady=5)
button_space_5.grid(row=1, column=3, ipadx=25, ipady=5, sticky = tk.W)
frame_space.grid_columnconfigure(0, weight=2)
for i in range(1,4):
    frame_space.grid_columnconfigure(i, weight=1)
label_block_selected.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
button_next.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
label_empty.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
label_empty_top.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
##################################################
root.mainloop()
