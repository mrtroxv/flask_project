from datetime import datetime
from tokenize import Floatnumber
import database
song1=database.Songs(id=1,name='rockstar',author="postmelano",type='pop',image_url='http',file_url='http',rating=0.5,tag='#34')
database.db.session.add(song1)
database.db.session.commit()