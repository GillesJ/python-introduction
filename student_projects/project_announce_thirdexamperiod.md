These are the final project guidelines for those participating in the third exam period.

***In order to partake in the third exam period it is necessary to meet the first project proposal brainstorming deadline of 20 May 2018.***
You will not be enrolled if you do not post the initial project proposal on the forum, 20 May 2018. If you have made a project proposal in the previous semester there is no need to repeat any steps, you are assumed to partake in the exam.

The project submission exam deadline and presentation date will be announced later this semester.

# Processing Language with Python: Third Exam Period Final Projects
---
You will formulate a practical problem for which you program a tool or application in Python. Examples projects are given below, but we encourage you to think creatively about an issue/tool that is useful for yourself.

The final project applies all the skills and knowledge seen in the course but also goes beyond requiring you to make use of online resources and external libraries. The problem you intend to solve should be sufficiently extensive.

You are allowed to formulate a project in group or solo. When you choose a group project, each person will solve a well-defined part of the larger problem; each part should be sufficiently extensive per person.

***Deadlines:***
- Project proposal brainstorming post on Minerva forum: ***20 May 2018, 23:59h***.
- Finished project proposal with problem analysis: ***27 May 2018, 23:59h***.
- Final project submission: ***To Be Announced***.
- Project demonstration presentation: ***To Be Announced***.

The project accounts for 100% of the final grade. The graded assignments give you extra points on top of the project score.

## A. Project proposal:
### Step 1: Brainstorming
The first step in the project proposal is to explain the problem. 
You will write a project proposal on the Project Minerva forum. Open a thread with your Firstname_Lastname (or the Firstname_Lastname of every person in your group) as the topic. The teachers will guide you in delineating an appropriate project if necessary.

Describe a problem or program you want to write in Python. The initial post is mainly for brainstorming purposes. We will discuss and give suggestions to delineate the project.

If you have trouble thinking of a project, think about a personal/academic field of interest, identify a task that is repetitive, requires a lot of counting or data processing. Try to make a vague idea as specific as possible.

***Deadline: 20 May 2018, 23:59h***.

### Step 2: Problem analysis
When you have a well-delineated problem, you will move to step 2 of the project proposal which involves breaking down the problem in several steps.

In your forum thread make a post with:
- Introduce the problem you want to solve.
- Problem analysis:
	- Input: 
		- Describe the data requirements: 
			- Do you need data? Will you use an existing corpus/dataset or will you collect your own?
			- What is the form and encoding of the data? 
			- Where will you get the data if you do not have it?
			- How will you collect the data?
		- Describe if your program requires user input.
	- Output:
		- Describe the expected result of the program.
		- Describe which information you write to file.
	- Processing:
		- Describe the expected steps involved in going from input to output.
- Give an example of typical input and the output you expect.

We will discuss the project proposal together on the forum and in the project class sessions. When the project discussion is completed you may write a brief project description based on the schema above to a file (.txt, .pdf, .docx) to be included in the final project folder.

***Deadline: 27 May 2018, 23:59h***.

## B. Project guidelines:
- Variable and function names should be in English. (This will also help when looking online for help.)
- Comments: Write clear and concise comments in the source code that explain what a function does. Try to avoid commenting where functionality is really obvious
- We advise to keep the project text-based, i.e. do not try to include a fancy GUI. GUIs are often completed and require a lot of work. Try to work with text-based inputs and outputs.
- Remove any unused ("dead") code.

## C. Submission
Submit the project folder as zipfile named Firstname_Lastname_project.zip file to the relevant Minerva gradebook before the deadline.

Included in the source code .zip folder you should have:
- A subfolder named "src" containing:
	- All Python scripts.
	- Example data if applicable in a /data subfolder.
	- A short README.txt usage/manual file (.txt, .pdf, .docx, .md, .html).
	   - Describe which script does what, (you should be able to copy-paste this from the opening comment of each script.) e.g. `main.py: this script runs the full program; count.py: counts the elements of a collection.`
	   - How do you run the full program: `To run use "python main.py"`
	   - What are the options and how do you set them (if applicable).
	- if you installed modules with conda or pip:

	     Run `pip freeze > requirements.txt` in the Anaconda Prompt/terminal (with your project virtualenv active) to get a list of used modules.
	     Place that file in the zip.
- A file with the project proposal (.txt, .pdf, .docx, .md, .html).
- Name the .zip file `FIRSTNAME_LASTNAME(for every person in the group)_PROJECTTITLE_finalproject2018.zip`


***Deadline: To Be Announced***.

## D. Evaluation
The final project will be scored on four criteria:
- The scope of the problem (this does not equal the amount of lines of code!).
- Code quality:
	- Program design: Is the problem solved correctly? Is the program designed in a well-planned and thought out manner? 
	- Program execution: Does it run correctly without issue? Does it provide correct output consistently? Does it work on unexpected inputs? Testing with many different inputs is adviced.
- Readability: Is the code well-written and commented. Does it have clear and understable variable names?
- Process: Did you independently use the course material and online sources to get to good solutions?

## E. Demo presentation
You will give a short live demonstration of the working program and a quick run-through of the source code.
This gives you the chance to comment and defend your code, highlight difficulties, and go in discussion.

You will not have to prepare a powerpoint presentation. You only have to make sure that:
- Your program runs on the computer/laptop you will use in the demo.
- You are familiar enough with the source code to answer some questions.

Please go the [Minerva Forum](http://minerva.ugent.be/main/forum/viewforum.php?forum=1152781) and let us know your preferred time slot (taking into account the reactions of other students). ***Slots will be posted and announced later this semester***.

## F. Example projects:
- Price comparison tool: Compares prices on several webstores for a certain book by webscraping.
- Interactive vocabulary learning tool: Reads a vocabulary list, asks a students for the translation of each word, and scores the student.
- Post-processing of machine translation output: Process KantanMT machine translation output to correct errors in translation of numbers.
- Crossword solver: lists possible words based on length and filled in letters.
- Lexical relation tool: list synonyms and antonyms, together with their gloss for a list of words.
- Readability analyzer tool: how readable and creative is an input text?

General techniques and topics:
- Web crawling in order to collect a dataset/text corpus and perform text analysis.
- Enriching text by linguistic processing and analysis of some sort.
- Automated corpus analysis.