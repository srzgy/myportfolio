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