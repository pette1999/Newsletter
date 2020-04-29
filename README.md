# Newsletter

**Instructions**
python3 news.py

**Peter Chen**
- authentication.py
- manageData.py
    - getlist(): This function allows us to get information from specific column from the google sheets
    - writelist(): This function allows us to write a list to the google sheets to a specific column
- .gitignore
    - hip-host-262902-bbbb44360c3f.json
    - this is ou credential file to allow us to connect with Google API
    - .gitignore prevents it being uploaded to the Github
- news.py
    - Since there is no Google News Api, we found another news api, which basically can do the same thing
    - api.txt
    - I put the api key in this file, so the api key won't appear on Github, which would prevent the api leaking
    - This program would grab top trend news(around 20 news) from all the sources, including BBC, The New York Times, The Los Angeles Times and so on, and output their title and the links to the article

**Peter TODO**
- Improve news.py to allow users to choose regions, sources, topics and so on. Then the program would grab the top 20 trend news that match these requirements
- Do research on how to send emails to our clients
- Impove manageData.py for more fucntions

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
