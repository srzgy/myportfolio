Nama : Deandra Sulthan Al Yudasswara

NPM : 2506592743

Kelas : PBP C

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
