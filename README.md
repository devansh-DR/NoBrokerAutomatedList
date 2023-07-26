# NoBrokerAutomatedList

Please note that web scraping might be subject to legal and ethical considerations, and it's essential to ensure you have the right to scrape data from the NoBroker website before proceeding with this automated process. Additionally, always be respectful of a website's terms of service and use web scraping responsibly.

Do not use it for commercial purposes.

Go to the NoBroker website at https://www.nobroker.in/.

Input filters such as city, area, BHK type, availability, and any other preferences you have for the flats you want to find, and then click on the "Search" button.

Once the site loads and displays the list of flats based on your preferences, copy the URL from the address bar of your web browser.

Paste the copied URL into the "URL" section of the NewMain.py file. This file is likely a Python script that you will be working with.

Create a Google Form with fields for the flat's title and link. This form will be used to collect information about the flats you find on NoBroker.

Copy the URL of the Google Form and paste it into the "FORM_LINK" section of the NewMain.py file.

Locate the XPath of the input section for the flat's title and the link section of the Google Form, and then paste these XPaths into the corresponding sections of the NewMain.py file.

Once you've completed the setup, click the "run" button to execute the script.

The automated process using the NewMain.py script will gather all the flat descriptions and links based on your preferences from the NoBroker website. It will then save this information into a Google Form, allowing you to conveniently import the data into a Google Sheet later on for further analysis or record-keeping purposes.

