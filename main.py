from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    # You could replace the list below with a call to a database or API that provides your photos
    photos = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg']
    return render_template('gallery.html', photos=photos)

@app.route('/blog')
def blog():
    # You could replace the list below with a call to a database or API that provides your blog posts
    blog_posts = [{'title': 'My first blog post', 'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
                  {'title': 'My second blog post', 'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'}]
    return render_template('blog.html', blog_posts=blog_posts)

@app.route('/instagram')
def instagram():
    # You could replace the URL below with the URL of your Instagram feed
    instagram_feed = 'https://www.instagram.com/your_username/'
    return render_template('instagram.html', instagram_feed=instagram_feed)

@app.route('/twitter')
def twitter():
    # You could replace the URL below with the URL of your Twitter feed
    twitter_feed = 'https://twitter.com/your_username'
    return render_template('twitter.html', twitter_feed=twitter_feed)

if __name__ == '__main__':
    app.run()
