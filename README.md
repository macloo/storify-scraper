# Storify Scraper

[Storify will no longer be available after May 16, 2018.](https://storify.com/faq-eol)

The process to download your Storify content, as described at that link, is cumbersome. The Python scraper script in this repo enables you to download all your stories in the same formats provided by Storify &mdash; HTML, XML or JSON &mdash; without using the cumbersome process at their website.

## What you’ll need

* Python (Python 3 is best; script not tested with Python 2)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](http://docs.python-requests.org/en/master/)

If you don't know how to `pip install` Python libraries, this will take some effort. Use Google.

## Steps to GET READY to get your Storify files

1. Open your Storify stories list page at https://storify.com/username
2. Scroll to the bottom, click the "Show more" button, and repeat until there is no "Show more" button.
3. In your browser, File menu &gt; Save Page As ... &gt; Webpage, Complete (as in Chrome; your browser might differ). Note that doing this manually spares you from using Selenium. If you don't know what Selenium is, just be grateful and move along.
4. Note where you saved this file. If you're new to all this, I suggest you make a new, empty folder and drag the file there. You also got a folder full of image files and other stuff when you saved the HTML file. You can put that in the new folder too.
5. If your filename has spaces in it (like *Mindy McAdams's social stories · Storify.html*), **rename it.** A good filename would be: *my_storifys.html*

## Edit the Python file

1. Copy or download the file *storify_scraper.py* and put it in the same folder with the file discussed above.
2. Using a plain-text editor, edit line 5 `filename = "my_storifys.html"` and line 7 `username = "your_user_name"` (change `my_storifys.html` if needed; you must change `your_user_name`).
3. Save the file.

You don't need to change anything else if you want to save HTML versions of all your Storify stories.

If you want to save XML or JSON files, there are options at the end of the Python file.

## Run the Python file

Assuming you have Python on your computer, and you have installed both BeautifulSoup and Requests, change into the directory and run at the bash (`$`) prompt:

```bash
python storify_scraper.py
```

All your Storifys will be saved as individual HTML files in the same folder.

## Note

Your downloaded files will include links to Storify JavaScript files and one Storify CSS file, as well as Livefyre.com links, which might not be available in the future.

If you run into trouble with this before May 16, 2018, please [post an issue](https://github.com/macloo/storify-scraper/issues). After May 16, 2018, there's nothing I can do.
