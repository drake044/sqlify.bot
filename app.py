!pip install vanna
import vanna as vn


vn.set_api_key('e52b103b11e84521b78e73d4e19034d4')
vn.set_model('chinook')
str = vn.ask('What are the top 10 artists by sales?')
print(str)
