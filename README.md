# RecruitData
A python project to extract information about:
1. Recruits for given states / years
2. Draft data

This is the final assignment for a course using Pandas / Matplotlib for creating effective graphs. I extended this project 
to learn more data-mining techniques and the process of grabbing data for manipulation. This project is split into three main sections.

--------------------
<h2>Recruit Data</h2>
 <h4>read247.py</h4>

For the recruit data, I decided to use 247Composite as the source for this information, as it's a comprehensive rating combining existing ratings from services like 247, Rivals, & ESPN.

For my purposes, I was only interested in recruit data for a given range of years and for a select number of states.

Given there's no current API to work with for 247, it was time to learn how to scrape some data.

In order to grab this information, the theory was simple:

1. Find the URL that prints out the list of recruits for a given state and a given year
2. Define the list of states & years that we are interested in, construct the URL dynamically given these params
3. Loop through the range of years for each state and grab ths data from the page we're interested in.
4. Print that information to a CSV for easier consumption for other tools / purposes.

--------------------
<h2>Draft Data</h2>
<h4>readDraft.py</h4>

Pro Football reference seemed like the best place to grab the necessary data I needed for my purposes. They have a great tool to select years you're interested and provides a page with 300 rows. They also have a button for transforming the table into CSV data. Great! 

In retrospect, it may have been easier to use BeautifulSoup a bit heavier than the procedure to hover & select the button to transform the table on each page, but alas, we made it work. The basic outline of the process goes as follows:

1. Load URL for given draft years we're looking for
2. Hover over the menu to expose the button to convert table to CSV data. Click button.
3. Grab the element that holds the CSV, concatenate our string with that data.
4. Continue 2-4 while there's still a "Next" button on the page, then do 2-4 once more at the end for the final page.
5. Write the string to a CSV file.

--------------------

This project uses the following tools / libraries to accomplish this:

<h3>1. Selenium Webdriver</h3>
<ul>
<li>Have only tangentially worked with Selenium, but knew it had the capabilities to perfrom actions within a web browser, which was necessary, here.</li>
<li>Each URL has a "Load More" button that loads an additional 50 recruits. Selenium Webdriver makes this possible to loop through and select this button each time it appears until all recruits for a given URL are loaded.</li>
</ul>

<h3>2. BeautifulSoup</h3>
<ul>
<li>Necessary library to pull data from HTML elements. This allowed me to search for the individual classes within the HTML source to extract the recruit information I was interested in (name, stars, rating)</li>
 </ul>

<h3>3. CSV</h3>
<ul>
<li>Write the results to a CSV for easier consumption, later on.</li>
</ul>

---------------------

<h2> Future Enhancements </h2>
This is a <i>very</i> custom approach to gather data for a specific project. I'm going to be committing other files as a part of this project to extract similar data from recent NFL drafts to cross-reference with the data exported from this.

For this specific extractor tool, it'd be nice for the following features:
<ul>
  <li>Walk through the set-up steps for you to run this file yourself (Downloading python, selenium web driver, beautiful soup, etc)</li>
  <li>Provide a list of years at runtime</li>
  <li>Provide a list of states at runtime</li>
  <li>Provide a list of of desired attributes to be written to the CSV file</li>
</ul>

This is definitely a work in progress and something that I encourage others to make feature requests.

Reach out to me on Twitter @StephenToski and let me know any thoughts!
