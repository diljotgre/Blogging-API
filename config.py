from configparser import ConfigParser

def config(filename = "db.ini", section="postgresql"):
    parser = ConfigParser()
    
    parser.read(filename)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception('Section not found')
    
    return db
    

config()