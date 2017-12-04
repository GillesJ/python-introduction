# Processing Language with Python
This repository contains the course files for the Processing Language with Python class.

The courses are thematically grouped by chapter notebooks:
- chapter: for teaching without the DIY class exercises filled.
- chapter+_course_notes: filled class exercises to be given after teaching.
- chapter+_final_exercises: final exercises to be given as assignment after teaching.
- chapter+_final_exercises_keys: Key to the final exercises to be given after assignment.

Historical course plan, feedback, assignments and projects of every year are stored in their corresponding directories for posteriority.

The project specification and announcement can be found in `/student_projects`.

NBDime https://github.com/jupyter/nbdime can help you merge and diff Jupyter notebooks for when you decide to edit.
In /util I have also provided a python3 script for joining/appending notebooks, handy for joining chapters or assignments into one file: `python3 nbjoin.py nb1.ipynb nb2.ipynb > joined.ipynb`

Copy the following announcement on Minerva before the first class:
____________________________________________________________________________________
# Course preparation
In the course we will be using software that works best with Google Chrome. Firefox 6 (or above) and Safari will also work. Internet Explorer is not supported. All recommended software is cross-platform and works on Windows, OSX, and Linux. Please, make sure that the software described below is installed and working before coming to the first class.

We will be using Python 3 for our course, which is the latest version. Lower versions are more or less supported, but not recommended.

## Bring laptop
This course will not be taught in computer classes and relies on each student to bring their own laptop.

## Text editor
We advice you to install a good text editor, Sublime Text 3 for example. However, feel free to use your own favorite editor. For Sublime Text 3 go to http://www.sublimetext.com/, download the version for your operating system, and install.

## Anaconda Python distribution
**Install the Anaconda Python Distribution.** This distribution contains all the necessary modules and packages needed for this course. It is available for all platforms and provides a simple installation procedure. Be sure to choose the **3.6 version** of the distribution for your specific OS.

You can download it from: http://continuum.io/downloads
(More detailed installation instructions can be found here: http://docs.continuum.io/anaconda/install.html)

## Jupyter notebooks
In this course we will be using Jupyter notebooks as a teaching tool. These are files that contain text, markup and executable code meant to make presenting code easy. Jupyter is the program that reads these files and presents them to your web-browser. It comes with the Anaconda distribution. 

Run Jupyter:
- Windows: Use the Anaconda launcher. There should be a shortcut in your menu with Anaconda and/or Jupyter Notebook like any other installed program.
- OSX: Use the Anaconda launcher.
- Linux: Use the Anaconda launcher or in terminal type: jupyter notebook

In case of issues, you can always install Jupyter separately with pip from Anaconda: https://jupyter.readthedocs.io/en/latest/install.html

## Troubleshooting
Some common problems when Anaconda does not work:
- Disable any anti-malware or anti-virus software that blocks components of Anaconda. Try to restart or reinstall with anti-virus disabled.
