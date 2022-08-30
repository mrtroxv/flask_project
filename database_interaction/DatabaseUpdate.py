from database_interaction import DatabaseSelect, DataBaseInsert, DatabaseDelete
import database_interaction


def update(my_dict):
    our_dict = {}
    our_dict = DatabaseSelect.select(my_dict['id'])
    for i in our_dict:
        for j in my_dict:
            if i == j:
                our_dict[i] = my_dict[j]
    DatabaseDelete.delete(our_dict['id'])
    DataBaseInsert.insert_mydata(our_dict)

