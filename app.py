import webbrowser
import pyautogui
import time
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os
from tkinter import messagebox

load_dotenv()

url = os.getenv("URL")

# checking the mouse position
def mouse_position():
    mouse_x, mouse_y = pyautogui.position()
    screen_x, screen_y = pyautogui.size()
    out_of_bounds = screen_y - 180
    if mouse_y > out_of_bounds:    
        print(f"Y coordinate is {mouse_y}, mouse is out of bounds Code canceled")
        messagebox.showinfo("showinfo", "Program has stopped")
        return True
    return False

def image_counter(images):
    if len(images) >= 75:
        return True
    return False
# Path to Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Open Chrome and navigate to a webpage
webbrowser.open_new_tab(url)

keywords = ["מוצא", "קונים", "להשיג", "איפה", "חלק", "למצוא", "לקנות", "פשפשוק"]

files_with_keywords = []
# Wait for the webpage to load
time.sleep(5)

# Perform scrolling
screen_x, screen_y = pyautogui.size()
scroll_duration = 10  # duration in seconds
scroll_amount = -500  # number of pixels to scroll
scrolls = int(scroll_duration / 0.1)  # number of scrolls to cover the duration

# Store the initial mouse position
initial_mouse_pos = pyautogui.position()

# Directory to save screenshots with keywords
save_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'parts-screenshots')

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


number_of_images = len(os.listdir(save_dir)) 

messagebox.showinfo("showinfo", f"To stop the Program move the mouse to the bottom of the screen for a few seconds.\nYou have {number_of_images} images in the folder.")

# Maximum number of scrolls
max_scrolls = 4
max_screenshots_per_loop = 10
mouse_x, mouse_y = pyautogui.position()
# Infinite loop to repeat the process

continue_program = True

if image_counter(os.listdir(save_dir)):
    continue_program = False

while continue_program:
    # Counter for screenshots taken in this loop
    if image_counter(os.listdir(save_dir)):
        continue_program = False
    if mouse_position():
        continue_program = False
        break
    else:    
        screenshots_taken = 0
        for _ in range(max_scrolls):
            for i in range(scrolls):
                if mouse_position():
                    continue_program = False
                    break
                if not continue_program:
                    break  
                pyautogui.scroll(scroll_amount, x=initial_mouse_pos.x, y=initial_mouse_pos.y)
                time.sleep(2)
                # Capture full-screen screenshot
                # screen = pyautogui.screenshot(region=(0, pyautogui.size()[1]//2, pyautogui.size()[0], pyautogui.size()[1]//2))
                screen = pyautogui.screenshot(region=(0, 0, pyautogui.size()[0], pyautogui.size()[1] * 2 // 3))
                screenshot_path = os.path.join(save_dir, f'screenshot_{time.time()}.png')
                screen.save(screenshot_path)
                screenshots_taken += 1
                if screenshots_taken >= max_screenshots_per_loop:
                    print("Maximum screenshots per loop reached. Stopping.")
                    # continue_program = False
                    break
            
            # Check if the maximum number of screenshots per loop has been reached
            if screenshots_taken >= max_screenshots_per_loop:
                break
            
        # Loop through the photos in the folder and scan each photo for specified keywords
        for filename in os.listdir(save_dir):
            if filename.endswith(('png', 'jpg', 'jpeg', 'gif')):
                screenshot_path = os.path.join(save_dir, filename)
                #Choose the prefered language key for the words your searching for
                text = pytesseract.image_to_string(Image.open(screenshot_path), lang="heb")
                # Add your desired keywords
                for keyword in keywords:
                    if keyword in text:
                        files_with_keywords.append(filename)
                        print(f"Found '{keyword}' in '{filename}'")
                    # Break out of the loop if at least one keyword is found
                        break

        for filename in os.listdir(save_dir):
            if filename not in files_with_keywords:
                screenshot_path = os.path.join(save_dir, filename)
                os.remove(screenshot_path) 
                print(f"Removed '{filename}' as it does not contain any of the specified keywords.") 
        # if image_counter(os.listdir(save_dir)):
        #     continue_program = False
        #     break             
        # Check if the maximum number of scrolls has been reached
        if screenshots_taken < max_screenshots_per_loop:
            print("Maximum number of scrolls reached. Exiting the program.")
            break

images_in_folder = len(os.listdir(save_dir))      
messagebox.showinfo("showinfo", f"Program has finished you have {images_in_folder} images in your folder")
print("Exiting the program.")

