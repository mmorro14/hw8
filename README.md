# Unit 8 Homework – Javascript and jQuery - mmorro14

## Concept Questions

1. (4 points) For any small Javascript task, give the syntax for doing it normally and then give an example of how jQuery makes that task easier to code. (Can just be one or two lines of code each)

2. (4 points) What is the difference in Javascript between declaring a variable that will hold an integer and a variable that will hold a string?

3. (4 points) Provide the single line of code that would be required to pop up an alert to the user and make
   the contents of the alert the 4th element of an array called 'warnings'

4. (4 points) Show the jQuery selector syntax that would select all elements on the page of class 'warnings' and make them hidden.

5. (4 points) Show the jQuery syntax for saving the value of a form element with id 'codon' into a variable called 'codonVal'.

## Practice Assignment

The following exercise should be performed on the class server and will be checked once the assignment is due.

1. ( 30 points ) 'Autocompletion' and 'type-ahead lookup' are common names for providing functionality so that a user can type in a form element and, as they type, suggested matching values to your query are displayed. This helps guide the user when they may not quite know the entire term or saves them time from typing it all out. You've probably noticed this using Google search and many other sites. It's something that's pretty easy to do (though scaling it well is a challenge with larger data.) In the a previous HW you modified our gene search program to read out of a database instead of parsing through the Genbank file, displaying the results in a table.

In the lectures from this week I modified that code to show how to perform that search as an AJAX call
that returned and parsed JSON formatted results and display them on the browser. That code can be found on the server here:

[/var/www/html/mmorro14/unit08](/var/www/html/mmorro14/unit08)

Make a copy of that directory into your web area (unless you want to use your own). Read the jQuery documentation on the 'autocomplete' function here: <http://jqueryui.com/demos/autocomplete/> Then modify the unit08 code I provided to add auto-complete functionality to the search box. The source of data should still be the Genbank file or a database search. That is, don't take the easier way out and hard-code a list of terms in a Javascript array. Limit the number of rows returned to 5 so that large lists aren't returned. As always, use internet searches, the forums, office hours and e-mail if you run into any problems.
