\# Development Log



\## Milestone 1: Initial Setup



\*\*Date:\*\* 2 November 2026



\*\*Work completed:\*\*

Today I set up my repo, my app and tests folders and my virtual environment. I installed packages into the venv, created requirements.txt with pinned versions. I also edited the README.





\*\*Key decisions or problems:\*\*

I was often in the wrong folder for the command I was trying to execute, tried setting up venv from projects instead of inside the repo. While setting up the venv I put a space in between - and m and slipped into the python prompt, Python alerted me to this when I tried to activate the environment. I used Claude to debug the terminal output.



I have a better grasp on file structure now and will check the folder name in the prompt before running commands.



It's hard trying to prevent problems down the line through correct implementation at the foundation of concepts I've yet to really encounter. It's difficult to understand where one deviation can interfere with my outcomes later.



I decided to put the repo on my personal account so as to begin building my portfolio. Outside of that I've mostly followed instruction from the teaching material for example Week 4's lab uses PyJWT and pwdlib/Argon2.



\*\*Commits:\*\*

https://github.com/eua201/piazza-coursework/commit/f6068ab8df6157c0618425479131aa1bd350e175





\*\*Sources and Assistance:\*\*



The teaching material for example class 1's README has :

"Open a new project folder in VS Code.

Create a Python virtual environment.

Create a requirements.txt file.

Install fastapi and uvicorn."

(warestack/cc 2026 accessed 8:00am)



Up to this point that has been instructive. Additionally the assignment's README has been instructive.



02/11 - I've used Claude to create colourful slides to understand the brief and summarise where I could lose/ gain marks e.g e.g making sure the requirements had pinned versions to satisfy D1 and D2.  I've used it for explanations around (venv, requirements, Docker, GCP) checking spelling and grammar in log. No code was generated.





\## Milestone 2: Application development



\### 4 November 2026: Data model design



\*\*Work completed:\*\*

Today I decided on the tables and columns needed for the database schema for the platform. I used excel and followed best practice to identify nouns to identify entities, that didn't entirely work for me so I re-read the brief and every time it said for each this you need this, it indicated a table that needed attributes. It's lead me to understand more vividly the relational aspect of things i.e. one many, many relationships. Time to diagram it for my report.





\*\*Key decisions or problems:\*\*

I'm still unsure as to how to calculate the independent reaction types. I'm not entirely clear the table is set up to allow that. I'm also not sure that I can calculate when the post is to expire based on how I've stored the information in the table. I was trying to link post table directly to topics table but had to create a junction instead.





\*\*Commits:\*\*



\*\*Sources and assistance:\*\*



I refreshed my database knowledge with Ullman, J.D. (1988) Principles of Database and Knowledge-Base Systems, Volume I. Rockville, MD: Computer Science Press. I also used Claude to order my actions and review my proposed table and to understand how to continue my development log, no code was generated.



\### 15 November 2026: App Skeleton and health check



\*\*Work completed:\*\*

The file that holds the app is the app/main.py, it contains the app, its title and the /health route returning 200.



I checked it worked through my browser and through the uvicorn log.



\*\*Key decisions or problems:\*\*

Decided on files to have based on classroom labs e.g. Class 7 to cast an eye to the future and accommodate deploying.



It was kind of difficult to pick where to start and which labs were most relevant.



\*\*Commits:\*\*

https://github.com/eua201/piazza-coursework/commit/f43a042



\*\*Sources and assistance:\*\*

I researched on Stack Exchange to understand what the best app skeleton might look like, I used the labs which I referenced for the code for the health check. I used Claude to understand where I left off and where to pick up, for feedback/explanations on/of code and for git and terminal commands. Also for feedback on sufficiency of development log. No code generated.

