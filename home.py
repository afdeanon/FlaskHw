from flask import Flask

myapp_obj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/")
def home():
        return '''
<html>
<head>
        <title>Flask Project</title>
</head>
<body>
        <h1>Welcome ''' + name + '''!</h1>
	<a href="www.google.com/">not google</a>
        <ul>
                <li>''' + city_names[0] + '''</li>
                <li>''' + city_names[1] + '''</li>
                <li>''' + city_names[2] + '''</li>
                <li>''' + city_names[3] + '''</li>
        </ul>
</body>
</html>
'''
#myapp_obj.run()
