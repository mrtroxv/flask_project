from database_interaction import Database
songs=Database.db.session.query(Database.Songs)
detail={}
def select(id):
 for i in songs:
     if i.id==id:
       detail['id']=i.id
       detail['name']=i.name
       detail['author']=i.author
       detail['type']=i.type
       detail['image_url']=i.image_url
       detail['file_url']=i.file_url
       detail['rating']=i.rating
       detail['tag']=i.tag
       return detail
       break

  
      
         