# Introduction to Programming with Python
This repository contains the course files for the introductory Python course.
This course borrows heavily from 'Python for the Humanities', a course by Folgert Karsdorp and Maarten van Gompel with modifications and contributions by Mike Kestemont, Lars Wieneke, Bart Desmet, Gilles Jacobs, and Patrick Goethals.

The courses are thematically grouped by chapter notebooks:
- `chapter`: for teaching without the DIY class exercises filled.
- `chapter+_course_notes`: filled class exercises to be given after teaching.
- `chapter+_final_exercises`: final exercises to be given as assignment after teaching.
- `chapter+_final_exercises_keys`: Key to the final exercises to be given after assignment.

NBDime https://github.com/jupyter/nbdime can help you merge and diff Jupyter notebooks for when you decide to edit.
In /util I have also provided a python3 script for joining/appending notebooks, handy for joining chapters or assignments into one file: `python3 nbjoin.py nb1.ipynb nb2.ipynb > joined.ipynb`

![Python intro course logo](images/python-intro-logo.jpg?raw=true "Python intro course logo")

Announce the following before the first class:
# Course preparation
In the course we will be using software that works best with Google Chrome. Firefox 6 (or above) and Safari will also work. Internet Explorer is not supported. All recommended software is cross-platform and works on Windows, OSX, and Linux. Please, make sure that the software described below is installed and working before coming to the first class.

We will be using Python 3.6+ for our course, which is one of the latest major versions. Lower versions are more or less supported, but not recommended.

## Bring laptop
This course will not be taught in computer classes and relies on each student to bring their own laptop.

## Text editor
We advice you to install a good text editor, Sublime Text 3 for example. However, feel free to use your own favorite editor. For Sublime Text 3 go to http://www.sublimetext.com/, download the version for your operating system, and install.
Good alternatives are Atom, or (my personal favourite) PyCharm, a full-blown Python IDE.

## Anaconda Python distribution
**Install the Anaconda Python Distribution.** This distribution contains all the necessary modules and packages needed for this course. It is available for all platforms and provides a simple installation procedure. Be sure to choose the **3.6 version** of the distribution for your specific OS.

You can download it from: https://www.anaconda.com/download/
(More detailed installation instructions can be found here: https://docs.anaconda.com/anaconda/install/)

## Jupyter notebooks
In this course we will be using Jupyter notebooks as a teaching tool. These are files that contain text, markup and executable code meant to make presenting code easy. Jupyter is the program that reads these files and presents them to your web-browser. It comes with the Anaconda distribution.

Run Jupyter:
- Windows: Use the Anaconda launcher. There should be a shortcut in your menu with Anaconda and/or Jupyter Notebook like any other installed program.
- OSX: Use the Anaconda launcher.
- Linux: Use the Anaconda launcher or in terminal type: jupyter notebook

In case of issues, you can always install Jupyter separately with pip from Anaconda: https://jupyter.readthedocs.io/en/latest/install.html

## Troubleshooting
Some common problems when Anaconda does not work properly or does not start:
- Disable any anti-malware or anti-virus software that blocks components of Anaconda. Try to restart or reinstall with anti-virus disabled.
