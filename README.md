# PROG_201 Final Project - Ella GRUBER
Final project for the PROG 201 class of the Cogmaster, an experiment coded using PyGame.

**SETTING UP THE SCRIPT**

**VENV CREATION****

Open the Terminal application on your Mac. You can find it in the "Applications" folder under “Utilities.” 

Navigate to the directory where you want to create the venv. You can use the cd command to change directories. For example, if you want to create the venv in your home directory, you can use the following command:  cd ~ 


Once you're in the desired directory, run the following command to create a Python venv:  python -m venv myenv    Replace ‘myenv’ with the desired name for your venv. You can choose any name you like. 

Wait for the command to complete. It will create a new directory called ‘myenv’ (or the name you provided) in your current directory. This directory will contain the isolated Python environment. 

To activate the venv, use the following command: bash  source myenv/bin/activate   Again, replace ‘myenv’ with the name you chose in step 3. You should see (myenv) appear at the beginning of your command prompt, indicating that the venv is active. 

Now that we’re in our venv, we’re ready to install the packages. Use pip3 to install them.  Install the following packages: numpy ; pygame 
Should you want to leave the venv for something, close the Terminal or type:   deactivate 

As a last step, you want to create a folder called “data” in the venv folder, where the txt files put out by the script will be located. Without this folder, the script will refuse to run.

**Running the script**

First, put the script file in the venv we created previously. Just copy + paste it in there 

Open your Terminal and navigate to where the venv is:  cd myenv/location

Activate it:  source myenv/activate

Now that the venv is active, run the script with the command below.  python script.py  Replacing “scrip.py” with the name the script has on your computer. 

You should see the starting window appear where you input the information for the session.



**Instructions:**

In this task, you will see a series of letters shown on the screen, one after another. Your job is to silently repeat each letter in your mind as it appears. The sequence of letters will repeat seamlessly (in a circle) about 3 to 4 times, and your goal is to keep repeating the letters in the correct order as they come up.

After that, the letters will be hidden by black circles or dots on the screen. These circles will appear at the same speed as the letters did before. Your task is to keep mentally rehearsing the letters in the correct order, even though you can't see them. After a certain amount of time, instead of a black dot, a question mark will show up on the screen. This means you have to respond with the correct letter that was supposed to be in that spot in the sequence, based on what you've been silently repeating.

To respond, you just need to type the correct letter on your computer keyboard in front of you. If your response is right, the letter will turn green. If you get it wrong, the letter you typed will turn red. It's important to respond accurately and as quickly as you can.

Remember, you'll have a mandatory 30-second break every 5 minutes during the task. Be careful, as the experiment resumes _immediately_ after you press the space bar. Normally, the whole experience will last between 15 and 20 minutes. However, for your convenience, tehre will be only 3 blocks of 5 trials each.


**Experiment explanation:**

This experiment aims to investigate the effect of articulatory suppression on attention. Articulatory suppression refers to the act of repeating or rehearsing information internally, which can be considered a type of mental "mantra." By examining how participants perform in this task, we can gain insights into how the use of internal repetition impacts attention and the presence of internal noise.

During the task, participants are asked to repeat a sequence of letters internally as they appear on the screen. The sequence is then repeated multiple times while participants continue to mentally rehearse the letters. The subsequent phase involves hiding the letters with black circles, while participants are still expected to maintain accurate internal repetition. Eventually, a question mark appears, indicating that participants need to recall and respond with the correct letter from the sequence.

The experiment explores whether the articulatory suppression (internal repetition) serves as a form of mantra that aids attention by reducing internal noise or interference. By investigating participants' accuracy (the distance between the participant's response and teh correct response in teh sequence of letters) and response times, we can assess the impact of this internal repetition on attentional processes and the ability to filter out distractions or internal noise.

Overall, this experiment studies how mantras, in the form of internal repetition, influence attention and internal noise. It aims to understand the potential benefits of using repetitive mental processes to enhance attentional focus and minimize cognitive interference.
