# picKdrama

November 2022
Welcome to PicK-Drama! by Iris Zhang and Sara Rhouate

If you've ever been in the mood for watching kdramas but are at a loss for what to watch, maybe we can help.

   Upon launching the website, you will be asked to create an account. Please create a username, a password containing atleast 8 characters, and
your favorite kdrama. Upon logging in, you will be taken to the main screen, which features the randomizer buttons. A majority of kdramas are
very romanced base and fit into some kind of trope. We have taken the 5 most popular tropes and created an archive of some of these dramas.
Select the trope you are most interested in and click the button. It will return a randomized title. Already watched the drama/not satisfied? Click again!<br />
    If you are curious in finding out more about the drama, head over to Tropes on the navigation board and find the trope that you had clicked.
It will then bring you to a list of all the dramas that was featured in that trope and offer you a brief summary and a quick way to get to a
website that will offer even more information on the title.<br />
    Next, head over to the Iconic Scenes tab. Here, you can check out some iconic scenes from various kdramas, which might peak your an interest
in a drama. There are also some other fun clips to check out. You can either watch a video by clicking on the video itself or for the first 4 videos, you can click the play/pause buttons next to their descriptions on the left. There are also hyperlinks in the more info buttons, as well as in the list of iconic lines at the bottom of the page.<br />
    Finally, if you want to update your favorite drama, you can head to the dashboard and input a new one.

Youtube Linked: https://youtu.be/F6LEfIFUDRY

Our project uses the languages SQL, HTML, Javascript, Python, and CSS. It is a Python Flask web application. The `app.js` file in the static folder includes code, like functions that are called when buttons are clicked. These functions include the `getRecs(list)` function, the Youtube API callback functions, and onPlayerReady(event) function. Some global variables like `player` were declared in the `app.js` file. We created this file or separated some of our javascript code to make the code more readable and easier to find.

Clicking on one of the 5 buttons–`Rich Boy Poor Girl`, `Rich Girl Poor Boy`, `Frenemies to Lovers`, `Love Triangle`, and `Contract Relationship` will call the `getRecs(list)` function, which will generate a random number. This random number is a random position of the list, which represents a random drama title. Using `innerHTML`, the random drama title will replace the space with the id `getRecSection`.

We decided to use lists to generate random recommendations rather than use something like `SELECT drama_title FROM kdramas ORDER BY RAND() LIMIT 1` because it would require more tables (for each trope) and we didn’t plan on adding more kdrama titles. If we had wanted to add more kdrama titles, a SQL database would allow easy inserting into tables. However, we did use SQL for users.

We based the file `app.py` based on the Finance pset where we used Flask. In this file, app routing was used to ensure that webpage urls worked properly and connected to the html files. Without app routing, code like `<a class="dropdown-item" href="/richgirlpoorboy">Rich Girl, Poor Boy</a>` would not be able to lead the user to the Rich Girl, Poor Boy page. This is because every app routing block returns an output by rendering/loading a template (EX// `return render_template("friendstolovers.html")`).

Methods `POST` and `GET` were used to request data and send data. This was required for the dashboard, login, and register pages. For the dashboard page, users can see their username and favorite kdrama. They are able to update their favorite kdrama by submitting a form. When this form is submitted on the dashboard page, data that the user inputted needs to be sent so that the information on the table can be updated. If the form is submitted, the variable `newfavoritekdrama` will be initialized to the drama title that the user inputted. Using SQL statements like `SELECT`, `UPDATE`, the “favoritekdrama” column of the “user” table will be updated for the user whose id matches the current user’s id. The login and register pages uses `request.form.get()` to retrieve the user’s input, checks if their inputs pass certain conditionals (like whether or not the password and re-typed password match), and lastly updates the users table based on the user’s inputs. Some functions in the `app.py` file also call functions in `helpers.py`, which contain the apology messages and `login_required(f)`.

We have app routes for every html page except for `layout.html`. Just like the finance pset, `layout.html` was used so that we could reuse code so we didn’t have to copy and paste it on every page. The code in the html layout page includes the navigation bar code (since we want the navigation bar to be the same on all pages), meta charset which encodes all possible characters for the website, `<script src="/static/app.js"></script>` which links the javascript file code to the HTML code, code linking bootstrap to HTML, code linking the CSS file to HTML (so that styling can be reflected on the webpage), and message flashing which gives the user feedback like invalid password errors.

Code like `{% extends "layout.html" %}` can be seen on the HTML pages. This allows for that HTML file to inherit from the `layout.html`. This ensures that code from the `layout.html` file, like the nav bar code, is able to be used on each HTML page. Template inheritance allowed us to build a base template and also allow for code to execute based on conditionals. For example, our website requires users to login before they can see any information. Once logged in, they can visit the specific trope pages in the “Tropes” dropdown, the Iconic Scenes page, and the Dashboard page. The nav bar code displaying these three menu items falls under `{% if session["user_id"] %}` so that only logged-in users can see it. Otherwise, people can only see the Register and Login pages, which is why this code is enclosed in `{% else %}{% endif %}`.

We used tags for the HTML files for structure, inserting bodies of text, creating buttons, etc.

For the specific trope HTML files, we originally wanted to use an API to easily retrieve summary and title info from My Drama List, but on their forum, they said that they no longer give out API keys. 

Each HTML page is viewable on the website because of the template rendering in `app.py`,  `styles.css` files, and the navigation bar code in `layout.html`. All color, border, width, or stylistic changes were made in the `styles.css` file. `Styles.css` contains selectors that allow us to make style changes to certain selected elements. For example, one of the selectors we used was `h1{}`. This implements style changes to the titles inside of the `h1` tag.

Overall, these are the technicalities of our website, picK-Drama. View comments in specific files to learn more.
