Nama : Deandra Sulthan Al Yudasswara

NPM : 2506592743

Kelas : PBP C

PWS Website: https://deandra-sulthan-myportfolio.pws.cs.ui.ac.id
# i purposefully chose to write "portfolio" instead of "portofolio" for this individual project to stay consistent with the english language.

### Tugas 1 Reflective Questions

1. yes, i specifically used <section>. i used it to split the three sections i've made: #profile (#hero), #experience, and #skills. using <section> is great because it makes the overall .html structure look clean, visually splitting each section so it's easier for me to read and write compared to just using <div>
2. the main layout challenge i encountered when setting up the responsive CSS was ensuring the grid didn't break or look completely squashed on mobile-view. I evaluated which elements needed repositioning based on readability and visual flow. for the mobile view, i used a `@media (max-width: 600px)` query to change the `.hero-grid` to a single column (`1fr`) and reorganized the `grid-template-areas` so the layout stacks vertically: "identity" at the top, then "photo", and finally "details". I also applied `flex-wrap: wrap` and `justify-content: center` to the `nav` so the links adjust neatly without clashing with the brand name.
3. as a pure static web page right now, the biggest limitation is that every data/information about myself is hardcoded into HTML. if i had to update my portfolio, i have to manually rewrite the code in the .html file. hopefully, the next thing i'd like to implement is database integration (using Django). this will allow me to manage my portfolio information dynamically through a backend system without editing the HTML file again.

### Tugas 1 AI Usage
- for this assignment, early on, i used gemini to reverse-engineer the code given from Tutorial 1 and teach me about everything i need to know about both html and css.
- i spent a decent amount of time trying to imagine the structure of the web visuals, but honestly, i haven't gotten that familiar with the syntax and rules so i had to prompt gemini to turn my visual ideas into actual syntax i can use for my html and css files.
- other than that, all visual choices and aesthetics, such as color palette, text capitalization, visual blocks (cards for experience, pills for skills), was all from my ideas.


### Tugas 2 Reflective Questions

1. Explain what happens when a user opens the new portfolio page, starting from the request received by the project until the data appears in the browser. In your answer, explain the roles of the project’s urls.py, the application’s urls.py, the view, the model, and the template.
    
    Let's say a user opens the new portfolio page, coming through section /education/. The project's urls.py will intercept the request and see that it belongs to the main app, and passes the request to main's urls.py. From here, main's urls.py sees the request asking for the /education/ path, so then it runs the show_education function which is in views.py of main. In views.py, show_education returns a render of the context (that's in the function itself!), towards the education.html page. Also, there is a "education_list": Education.objects.all() in that context block, which refers to the Education object in models.py! In models.py we hardcode what fields or information an object has. Anyways 'Education.objects.all()' basically goes to our local database (for now) and returns all Educations objects that we initialized using the shell, which will be showcased in the education.html page where the 'design' is already hardcoded using django logic to build the final visual structure. Finally, the finished html is shown to the user!


2. Why should the data for the new portfolio section be stored in a model instead of being written directly in the template? Explain how this choice affects application maintenance and future development.
    
    So, I think that the data should be stored in a model because writing it directly in the template will be annoying when you decide to edit, add, or delete the specific data mentioned. Waste of time and energy, basically. So, putting them in a model is better because changing stuffs won't need you to change the template! The template's job is to look good and clean, not hold data that clings onto design.

3. What is the difference between makemigrations and migrate in Django? Give an example of a model change that requires you to run both commands.

    By looking at the terminal when I did these two lines, I realize that makemigrations is usually used after I make new objects in models.py. When I run it, it seems like it reads what I've done to models.py, and prepares some instructions for the next line, which is migrate, for migrate to apply those instructions to the physical database!

### Tugas 2 AI Usage
For this assignment, I used Gemini again to help me deal with the design conflict of Assignment 1 when I was doing Tutorial 2. Tutorial 2 had me creating an experience section that I had made for Assignment 1. The problem was that there were CSS lines that were redundant and it made the CSS lines I wrote for Assignment 1 for the experience section be overwritten by the tutorial.

Other than that, I also asked Gemini for help understanding how Django MVT works, from what to do when creating the new objects in models.py, how views.py correlate to the template html files, and a refresher on unit testing, but Django.


### Tugas 3 Reflective Questions
1. Explain why we use Django’s ModelForm instead of creating HTML forms manually. Additionally, explain why we are required to add {% csrf_token %} to these forms!

    So, I think using ModelForm is basically way easier than writing manual HTML forms because Django just looks at our models.py and automatically builds the form inputs for us. It saves so much time and energy since you don't have to hardcode every single <input> tag and make sure it perfectly matches the database fields. As for the {% csrf_token %}, we are required to add it because it acts like a security bouncer. It stands for Cross-Site Request Forgery, and the token basically verifies that the form submission is actually coming from our own website, and not from some random dude trying to do a fake request onto my server.

2. In Tutorial 03, we discussed JSON and XML data formats. Why is JSON preferred in modern web application development compared to XML?

    JSON is just way better for modern web development because it's so much lighter and easier to read compared to XML. XML uses all these clunky opening and closing tags (just like HTML) which makes the file size bulky and annoying to look at. JSON, on the other hand, looks exactly like a standard Python dictionary or a JavaScript object. Since it literally stands for JavaScript Object Notation, web browsers can process it super fast natively without needing complex parsers. It's just a cleaner and more efficient way to move data around in my opinion.

3. Explain the flow that occurs when you use a view function to return your portfolio data in JSON format. Why do we need to perform the serialization process on Django models before returning the data?

    Let's say a user's browser requests the JSON data. The urls.py sees the request and directs it to our specific view function (like get_education_json). Inside the view, we first grab all the data from the database using something like Education.objects.all(). But the thing is, that data comes out as a complex Django QuerySet, which web browsers and the internet can't just automatically read. That's why we need to do serialization. Serialization basically translates those complex Django Python objects into a simple, universal text format (which is JSON). Once it's translated, the view packages it up in an HttpResponse and sends it back so the browser can actually understand and use the data.

### Tugas 3 AI Usage
For this assignment, I used Gemini as a coding mentor to help me properly structure the layout and resolve CSS conflicts. Specifically, Gemini helped me use object-fit: cover to standardize image dimensions across my cards, fix a mobile responsiveness issue in the header using CSS media queries, and debug my edit_education view when I accidentally queried the wrong model.


### Tugas 4 AI Usage
For this assignment, I fully completed the tutorial 4 without any AI assistance, following each step meticulously. However, I had to go through a CSS problem, where it seems that a style.css file from a completely different and irrelevant directory became the source for base.html. Had to ask Gemini for help regarding this, making me realize that I needed to check the css source code when I ran the server and see whether the source code is identical to the one i have for myportfolio. Hence, I renamed my style.css file into style_srzgy.css so that nothing gets entangled.

However, I did use AI to finish up the only thing in the assignment that I think wasn't in the tutorial, which was to create the 'Editors' role through localhost:8000/admin. Was completely unfamiliar with that, so yeah.


### Tugas 5 Reflective Questions
1. Explain what debouncing is and why this technique is important to implement in a search feature that uses AJAX.

    So, debouncing is basically a way to tell our code to "hold on a sec" before firing off an action. In an AJAX search feature, if we didn't use debouncing, the browser would send a brand new fetch request to the server for every single letter we type. If I type "Tottenham", that's 9 separate server requests in  two seconds. That would completely spam and overwhelm the server. By implementing debouncing (using setTimeout), we force the browser to wait until I actually stop typing for a set amount of time (like 300 milliseconds) before it finally sends one single AJAX request. It's just way more efficient and keeps the server from crashing under pressure.

2. Explain the purpose of using await when we use fetch(). What would happen if we did not use await?

    The purpose of using await with fetch() is to pause the execution of that specific JavaScript function until the server actually replies with our data. Fetching data across the internet takes time, and JavaScript is impatient; usually just wants to keep running the next lines of code immediately. If we didn't use await, JavaScript would run the fetch() request and instantly move on to the next line before the JSON data even arrives. We'd end up trying to render our experience cards with an empty or "undefined" response, which would just break the UI entirely. await basically forces the code to chill out and wait for the Promise to resolve before moving forward.

3. Explain what a Cross-Site Scripting (XSS) attack is and why data displayed through AJAX JavaScript is more vulnerable to this attack than data displayed directly through a Django template.

    An XSS (Cross-Site Scripting) attack is basically when some random dude sneaks dangerous JavaScript code into our database—like putting a <script> tag inside an "Experience Title" input. When other users view that page, their browser reads the malicious code and executes it, which could steal their session cookies or mess up their account.
    
    Data displayed through AJAX is more vulnerable because when we use normal JavaScript to manually inject HTML (using something like innerHTML), the browser just blindly trusts and runs whatever tags are in that string. Django templates, on the other hand, have built-in auto-escaping. If you try to render a script tag in a standard Django {{ variable }}, Django acts like a security guard and automatically converts the brackets into harmless text thingies (like &lt; and &gt;) before it ever hits the browser. When using AJAX, we have to manually build that security guard ourselves using an escapeHtml() function.

### Tugas 5 AI Usage
For this assignment, since I followed the tutorial thorougly to upgrade my Experience section, I feel like I understood what to do when mirroring the exact same upgrade (across Tugas 4 and Tugas 5 things) for my Education section. I still used Gemini to make sure that my code for the Education section mirrors perfectly with my tutorial-based Experience section. The problem I had to face though, was a CSS problem where for the unstarred button in an experience/education card, the colors were all white so they overlapped and the stars, the text, and the number who starred the card, it was all unreadable. I had to ask gemini for help regarding the priority css styling, but I feel like at some point it was also a css cache issue, because the readability was solved once I opened up a fresh google chrome window to open up localhost (i used opera gx mainly, then edge secondarily)

### Tugas 6 Reflective Questions

(heads-up, for this tutorial and assignment, i decided to do the education model for the tutorial, so for the assignment, i implemented the features to the experience model)

1. Explain what REST means and why returning JSON alone isn’t enough to call an API RESTful. Also explain the difference between PUT and PATCH, with an example of when each should be used.

    So, REST basically stands for Representational State Transfer, and it's an architectural style for organizing web APIs rather than just a library or returning JSON files. Just returning a JSON response doesn't automatically make an API RESTful—for example, back in Tutorial 05 we returned JSON from `/api/experience/`, `/experience/add-ajax/`, and `/experience/<uuid>/delete/`, where the actions ("add", "delete") were literally written in the URL paths and everything was basically just GET or POST. A RESTful API organizes things around resources (nouns), like `/api/v1/experiences/` and `/api/v1/experiences/<uuid>/`, and uses standard HTTP methods (GET, POST, PUT, PATCH, DELETE) to represent what action is being done to that resource.

    As for PUT and PATCH, both are used to update existing data, but the difference is how much data you're replacing. PUT replaces the entire object, meaning you have to send all required fields again even if you only wanted to change one word. PATCH, on the other hand, is a partial update where you only send the specific fields you actually want to change. For example, if I have a full edit page with a form that resends the title, description, category, and thumbnail all at once, using PUT makes sense. But if I just want a quick inline edit to change the title of an experience from the console or a quick modal without having to resend the entire description and category, PATCH is way better because `partial=True` keeps all the other fields untouched.

2. Explain the role of a serializer in Django REST Framework. What are its advantages over manually assembling a dictionary with JsonResponse as in Tutorial 05?

    A serializer in DRF basically acts as a two-way translator and bouncer between our Django database models and JSON data. When reading data (GET), it serializes our model objects into clean Python dictionaries (including computed things like `star_count` and `is_starred`) so DRF can output them as JSON. When receiving data (POST, PUT, PATCH), it does deserialization: it takes the incoming JSON, validates every field (like checking if the URL is valid or stripping harmful HTML tags), ignores read-only fields so nobody can tamper with things like star counts, and saves it into the database via `.save()`.

    Compared to manually looping through objects and building dictionaries with `JsonResponse` like we did in Tutorial 05, serializers are just so much cleaner and less repetitive. In Tutorial 05, our read logic was in a manual loop in views while our write validation was inside `ModelForm`. Serializers unite both data representation and validation into one single file. Plus, it gives us flat JSON (like `item.id` and `item.title` instead of the clunky `item.pk` and `item.fields.title` from before) and easily handles partial updates with `partial=True` without needing tons of boilerplate if-else statements.

3. Explain the difference between authentication and authorization in Django REST Framework. Why must access rights be checked with a permission class on the server, rather than only by hiding a button in the template?

    Authentication answers "who are you?", while authorization answers "what are you allowed to do?". In DRF, authentication happens first (`SessionAuthentication` checks the session cookie and sets `request.user`), and authorization happens right after through permission classes (like `IsPortfolioOwnerOrEditorOrReadOnly`) to decide whether that specific user has the right to run that HTTP method before the view even touches the database.

    Checking access rights with a server-side permission class is mandatory because hiding buttons in HTML templates (`{% if user.is_superuser %}`) is only a visual thing for UI/UX. Anyone with basic web knowledge can just open DevTools in their browser, hop into the Console or Network tab, and send a `fetch()` request with a `DELETE` or `POST` directly to `/api/v1/experiences/<uuid>/`. If we don't have permission checks running on the server, any regular user or random visitor could bypass the hidden buttons and delete or modify data directly.

4. Explain why requests that change data still need a CSRF token when an API uses SessionAuthentication. Why isn’t a test using force_authenticate enough to prove that CSRF protection works?

    When an API uses `SessionAuthentication`, browsers will automatically attach the user's login session cookie (`sessionid`) to every request going to that domain. Without CSRF protection on write operations (`POST`, `PUT`, `PATCH`, `DELETE`), a malicious website could trick a logged-in user into triggering an API call on our site, and the browser would blindly send the session cookie with it. Requiring the `X-CSRFToken` header (which JavaScript grabs from the `csrftoken` cookie) ensures that the request actually came from our own frontend and not from some external malicious script.

    `force_authenticate()` isn't enough to test this because it's a testing shortcut that directly attaches a `User` to the request, completely skipping the real `SessionAuthentication` backend and CSRF checks. It's great for checking role permissions, but it doesn't simulate real-world browser cookie sessions. To actually prove CSRF protection works, we have to use `APIClient(enforce_csrf_checks=True)` and log in with `.login()`, which tests the real session flow and confirms that requests missing the CSRF token get rejected with a 403 Forbidden.

### Tugas 6 AI Usage
For this assignment, since Django REST Framework (DRF) is completely new to me, I used Gemini to ask questions about how DRF works conceptually, especially understanding the request pipeline through serializers, permissions, and `@api_view`. 

Most of the implementation itself was me mirroring the pattern I learned from the tutorial (where I built the Education API) onto my Experience section. Along the way, I also used Gemini to clarify a few specific Django and DRF methods and syntaxes that I hadn't encountered before. For example, I asked how `partial=True` works on a serializer instance when handling PATCH requests without requiring all mandatory model fields, and how `prefetch_related("starred_by")` works with DRF `SerializerMethodField` to prevent repeated database queries when calculating star counts and user lists.