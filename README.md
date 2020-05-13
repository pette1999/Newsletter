# Newsletter

**Libraries**
- gspread
    - pip install gspread
- requests
    - already in the python library
- json
    - already in the python library
- sendgrid
    - echo "export SENDGRID_API_KEY='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'" > sendgrid.env
    - echo "sendgrid.env" >> .gitignore
    - source ./sendgrid.env
    - pip install sendgrid
- gmail to send emails
    - dailynewsletter@gamil.com
    - pw: dailynewsletter
    - Client database: in google sheet, named Client

**Instructions**
- in terminal type
    - pip install gspread
    - echo "export SENDGRID_API_KEY='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'" > sendgrid.env
    - echo "sendgrid.env" >> .gitignore
    - source ./sendgrid.env
    - pip install sendgrid
    - python main.py

**Meghana Shastri**
- Doing research on how to connect to the News API
- getNews.py(now in news.py)
    - getNews.py currently retrieves the top 10 headlines of BBC news 
    - this was done by fetching the data in the JSON format
    - then the articles were stored as a variable and put in a list called results
    - the urls for the articles were also stored in a list
    - then using a for loop, the headline and url of each article was printed

**Meghana Shastri TODO**
- Do research on how to use SMTP to send emails from one user to another in python
- Make a program that uses STMP to send out the results and url lists (from getNews.py) in an email  

**Audrey Bichelmeir**
- Doing research on how to send emails daily by accessing the google sheets 

**Audrey Bichelmeir TODO**
- create an automated program that sends out the information through the email addresses of the clients in the google sheets. 
