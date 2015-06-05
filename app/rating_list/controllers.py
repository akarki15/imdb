from flask import Blueprint, render_template
import  os
from config import STATIC

rating_list = Blueprint('rating_list', __name__, url_prefix = '/rating_list') 

@rating_list.route('/',methods=['GET'])
def home():
        list  = []
        with open(os.path.join(STATIC, 'movies.csv')) as file:
                for line in file:
                        name = line.split(',')[0].decode('utf-8')
                        rating = '10'
                        list.append([name, rating]) 
        s = ''
        for item in list:
                print '\n'
                print item[0]
                print '____'
                print item [1]
                s+='\n'
                s+=item[0]
                s+=str(item[1])
        
        return render_template('rating.html',list=list)
