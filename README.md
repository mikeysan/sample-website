# sample-website
Attempting to use ChatGPT to create a photography portfolio site

Here's the current structure I am going for:

```lua

myapp/
|-- app.py
|-- templates/
|   |-- index.html
|   |-- about.html
|   |-- gallery.html
|   |-- blog.html
|   |-- instagram.html
|   |-- twitter.html

```

After over an hour of talking. Here's what Chat thinks I have or should have.

```lua

app/
├── __init__.py
├── forms.py
├── models.py
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── style.css
│   │   └── lightbox.css
│   ├── js/
│   │   ├── base.js
│   │   ├── lightbox.js
│   │   └── contact_form.js
│   └── images/
│       ├── gallery/
│       │   ├── image1.jpg
│       │   ├── image2.jpg
│       │   └── image3.jpg
│       └── icons/
│           ├── instagram.svg
│           └── twitter.svg
├── templates/
│   ├── base.html
│   ├── about.html
│   ├── blog.html
│   ├── contact.html
│   └── gallery.html
└── utils/
    └── send_email.py
```
