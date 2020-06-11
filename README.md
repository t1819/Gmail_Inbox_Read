Read your Gmail inbox using imap.

Features:
---

	* Read any Gmail label. ex: 'Inbox'.
	* Read emails for specific duration emails.

How to use script?
----------
* Clone git repo
	```python
	git clone https://github.com/t1819/Gmail_Inbox_Read.git
	```

* Create a config.py file with below details:
	```python
	email = 'example@gmail.com' # your email address.
	password = 'password' # your email password.
	label = 'Inbox' # email label.
	from_date = '27-Apr-2019' # start date.
	to_date = '1-May-2019' # to date.
	```
* Execute the script and get all the emails subjects from gmail label. 
	```python
	cd src/
	python Email_Read_IMAP.py
	```