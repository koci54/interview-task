# interview-task

## Task 1
`data.txt` contains **"** character on line 21 and 29 with cust_no C20 and C28.
As explained in `data-as-html.py` and `data-as-string.py`, I assume that this data was entered incorrectly.
So I decided to delete **"** character in the beginning of the lines mentioned above so I can proceed with the task.

Please find bash script `sort-and-update-date.sh` where data is sorted and date is modified. Datasource is `data-bash.txt`. New file `updated-data.txt` is generated.

### Some examples of resources to complete task 1:
The book Writing about Linux System Administration using LaTeX https://github.com/murraydavis/Linux-System-Administration
This book has practical examples bash scripts, regex, etc.

https://regex101.com/ to test the regex.

Multilne string example in Python - https://stackoverflow.com/questions/35903017/is-there-any-way-to-use-variables-in-multiline-string-in-python


## Instructions for the task-2
Http protocol can be implemented in many different ways. This simple server proxy may not be ready for production purposes, however I have chosen Python for this task becasue this is the technology I am most familiar with.

get the repo

`git clone https://github.com/koci54/interview-task.git`

cd into task-2 direrctory

create virtual environment

`python3 -m venv task-2-venv`

start the virtual environment

`source task-2-venv/bin/activate`

install packages 

`pip install -r requirements.txt`

when finished, to stop virtual environment

`deactivate`

### Some examples of resources to complete task 2:
#### Libraries used
requests - 
https://requests.readthedocs.io/en/master/user/advanced/

urllib - https://docs.python.org/3/library/urllib.parse.html

flask - https://requests.readthedocs.io/en/v1.2.3/user/install/

xmltodict - https://github.com/martinblech/xmltodict

#### Resources
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask - create api with flask.

http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/#requests-to-the-rescue - URL query.

https://www.geeksforgeeks.org/python-xml-to-json/ - xml to json.

https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask - content for query string.

https://docs.python.org/3/library/urllib.request.html#urllib-examples - urllib examples.



