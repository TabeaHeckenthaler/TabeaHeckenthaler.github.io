# Advanced Python Course 2021

[About me](https://tabeaheckenthaler.github.io/aboutMe)

## Lecture 1 Oct. 26th:

* Gabor explained about the process of cloning, sending a push and a pull request.
* git status
* git diff
* git add .
* git commit -m "comment"
* git log - shows the logs of the commits
* git push


### [Testing](https://code-maven.com/slides/python/testing-demo)

* [doctest](https://code-maven.com/slides/python/testing-demo-doctest)
* [unitest](https://code-maven.com/slides/python/testing-demo-unittest) - the example was with a Class, object oriented, which we do not need to write in the course
* [pytest](https://code-maven.com/slides/python/testing-demo-pytest) need to install

### HW:

- [x] Send a pull request with notes and json with personal details
- [x] 10 exercises on exercism with mentoring\


## Lecture 2 Nov. 2nd:
I started to do the homework. 
My site is linked [here](https://tabeaheckenthaler.github.io).
Subject line: Subject: WIS Advanced Programming skills 2021-2022 - after day 1 - Tabea Heckenthaler

## Lecture 3 Nov 9th:
* use Slack!
* We need to do the homework... Checking some webpage
* How to create stuff in flask: Every computer has a number (IP number)
* Every computer calls himself (127.0.0.1) ...
* Google.com is actually just a number, connecting to 'googles computer'
* Build a search engine with some data from your research (work in pairs!!)
* FLASK: uses jinja (some computation in python, templating engine, like email with 'Hi, firstname')
* install flask, it will create routing map (answers to specific requests and returns a route?)... 
* @app (decorator, changes the behaviour of the decorated function)
* seperate code and data
* map some address to some function
* on Windows (windows command line): <br />
set FLASK_APP=app <br />
set FLASK_DEBUG=1 <br />
flask run

* debug mode makes dynamic updates when I change my python file
* browser, application is running, editor
* Run flask from the command line, it creates a routing map locally on your computer and it waits for someone to ping to your computer
* You have to install pytest in your environment
* If you turn off the computer, no one would be able to access, because flask is not waiting for anyone to ping to your computer from the browser.
* when you open a website you temporarily store the html, this is already downloading
* SSH client: connect to WEXAC terminal using Putty or MobaXTerm
* You can use the requests package to access any website... scraping
* To prevent that computers pretend to be humans... like with the requests website, they ask you to click the watermelon
- [ ] Write a calculator 
- app.logger... can help you deal with errors in your website\
- pull request with a link in your json files (homework)

## Lecture 4 Nov 16th:
* mapping fixed paths. We learned this. 
* Now, lets see, if we can have dynamic paths, ... like you have on exercism
* Put in the decorator: \

@app.route{'\user\', defaults={'userID': 'zero'}} (not necessary)\
@app.route('\user\<str:userID>') \
def something(userID):\
 return userID\
* curl : access the internet from your command line without browser, it will return the html from whatever website
* how to safely store passwords: hashing algorithm
* dictionaries use hashes, to find the place where to store
* You can use html template matching,... this is somehow cool
* Jinja helps you deal with html template matching... use render_template ... does something with jinja... 
* [jinja html template](https://code-maven.com/slides/python/flask-jinja-list-of-dictionaries)
* [jinja include](https://code-maven.com/slides/python/flask-jinja-include)
* images: put in directory called static/img
* What is right to say: I am German, and I don't deny the atrocities of my nation. I love the Jewish nation. 
* Cookies: I build up a new connection every time. You need a server to understand, who you are. 
* Account
* css bootstrap, bulma is a nicer way to create html websites. 
* css is a separate language. but them in style brackets
* css allows you to define classes, of how to display text 
* css allows you to define ids.
* I think you have to learn how to use css. 
* css means cascading style sheet\
* you can link to the css style sheet, so you can put the css in a seperate file. 
* b (bold),p (paragraph), div (like paragraphs), span (mark some text, but please dont break it into two lines)
* You can use HEX to chose colors
* find more stuff on the class README.md
* separate the business logic, from the web application and the command line script.
* send Gabor a pull request with interesting modules
* Tk toolkit, helps you create a desktop application, it talks to your Betriebssystem
* there is a video in the bootcamp about tk.
* tk is a nice way to make guis. ... maybe you can do this for your research :)


## Lecture 5 Nov 23rd:
* jupyter notebook is just an environment, and editor, to program interactively
* jupyter notebook run a web application
* --ip means: Suddenly the server is listening to all other computers as well. 
* --no-browser: Will not open a browser
* which python are we running? python (which is actually python3) by default installed on Windows
* python as a directory, where it installs all of its modules. 
* pip install ... or conda install
* venv directory is in your project directory.
* venv directory should not be in version control
* Better: requirements.txt (you can even specify the version you need... like this: numpy >= 1.03)
* You can install them all at once is: pip install -requirements.txt
* pip freeze > requirements.txt will create a requirements.txt. 
* [Gabor says](https://code-maven.com/python-package-dependency-management): Create your own requirements.txt
* pip install -r requirements.txt -c constraints.txt
* pip freeze > constraints.txt
* Wrapper: Pandas is a wrapper of numpy. So, the data inside a pandas dataframe is stored as numpy array
* Algorithms and datastructures: scalars (string, number), lists, dictionaries (immutable key, some value), 
* Behind the scenes: Trees, graphs, binary graphs.
* What type of data structure to use? Add value, find value, 
* ordered list makes it less computationally heavy to find a value, by checking in the half. (from O(n) to O(log(n))) 
* sorting a list can be n^2 and n*log(n)
* Homework: improve the speed of a program, multiple CPUs, and reduce complexity
* it can be bad, if you don't choose lists 
* Look at your program, and make sure that the order of your program is reasonable. 
* Speed up your CS diagram creator... :) Should be fun :) ... you can check bounding box. 
* In order to run in parallel,
* CPU (central computing unit)
* GPU (graphical processing unit), created only for handling your screen. Its like a stupid CPU. 
* Recently, they found that numpy type operations is good to run on GPU, because he does exactly what we need very well. Physically GPU is physical built for heavy computations.
* python Levenshtein ... distance of two words. This has an implementation in C
* Fast marching method could be improved by using symmetry? But we dont update our CS in a symmetrical fashion* FIFO (first in, first out), LIFO (last in, last out): watch 3 bootcamp movies
* FIFO (first in, first out), LIFO (last in, last out): watch 3 bootcamp movies
* deque is the module in python that will do this. 
* Numpy is behind the scene written in C. This is why it's fast. 
* forking (multiprocessing) and threading (single threaded vs multi threaded)
* asynchronous non blocking or synchronous vs. blocking cooperative multitasking
* time slicing (operating system gives the CPU to different tasks)
* Deadlocking to avoid mis-computation (for example in threading, shared memory)
* Resource starvation: you run out of memory
* Depending on the type of application that you are running... IO (reading from file, or downloading stuff), CPU (computation)... that determines how many threads you want to open
* [Thread counting](https://code-maven.com/slides/python/class-counter-central)
* locker.acquire() and locker.release()
* counter_central_plain (this is just linear counting), counter_central_lock (you have a lot of overhead from all the locking etc.)
* GIL - global interpreter lock (only one of the threads can run at the same time).
* What is the difference between an iterator and a stack?
* best module: [multiprocessing as mp](https://code-maven.com/slides/python/multiprocess-file)
* map is a nice method, similar to list comprehension

## Lecture 6 Nov 30th
* Why do we need machine learning?
* We have more variables: Map variables to some classification
* supervised: Already know answers...
* unsupervised: Grouping... without knowing any answer

### Regression problem
* Predict continuous value output (housing prices, life expectancy)
* Solutions: Linear regression with sklearn (over-fitting: Every new data point totally changes the polynom fitted)
* get good data!! This is really important :) 

### Classification problem
* Predict binary value output
* Example: Tumor size... malignant or benign
* Unsupervised Learning: Clustering... 
* Random seed fixed to 42
* 