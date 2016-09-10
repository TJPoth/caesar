import webapp2

# html boilerplate for top of page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
    <h1>Caesar!</h1>
"""

# html boilerplate for bottom of page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.caesar.com/
    """
    def get(self):

        edit_header = "<h3>Enter some text to be encrypted:</h3>"

        rot13_form = """
        <form method="post">
            <textarea name="new-text" placeholder="Enter text to be encrypted" rows="4" cols="50"></textarea>
            <br>
            <input type="submit" value="Encrypt!"/>
        </form>
        """

        # if we have an error
        # error = self.request.get("error")
        # error_element = "<p class='error'>" + error + "</p>" if error else ""

        # combine all pieces fo built content response
        main_content = edit_header + rot13_form
        response = page_header + main_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
