First before activating be sure to install Pytesseract on your system via https://github.com/tesseract-ocr/tesseract and all dependecies from the requirements.txt file with the command

pip install -r requirements.txt

Or install manually

pip install pyautogui
pip install Pillow
pip install pytesseract

In the Command line or Terminal

###

You may choose your own Keywords and the language 

###

The bot uses python to automate GUI on the device to scroll and take screenshots after every scroll.
###

After every 10 scroll the bot will use pytesseract to scan all the images inside the folder for specified keywords(if a folder doesnt exist the app will create one).
###

The bot will remove any images that do not contain any of the keywords and then resume scrolling and taking screenshots.

###

Before continuing to scroll the bot will first count the amount of images with keywords in the folder, If the amount of photos is equal or exceeds 75 the bot will stop the proccess automatically

###

To manually stop the bot move the mouse cursor to the bottom of the screen and wait for a popup window to appear with the words "Program has stopped" informing you that the program has stopped