""" Run this script as a part of setup to download all data from imdb """

import urllib2, urllib, json, pickle

def write():
    """ Reads movies.csv file, gets the imbd rating and stores that into a file """
    with open('movies.csv') as file1:
        json_dump = open('dump', 'w+')
        temp_list = []
        # i = 1
        for line in file1:
            name = parse_input(line.split(',')[0])
            params = urllib.urlencode({'t':name, 'r':'json'})
            response = urllib2.urlopen("http://www.omdbapi.com/?"+params).read()
            json_obj = json.loads(response)
            print params 
            if json_obj['Response'] == "True":
                temp_list.append([name, json_obj['imdbRating']])
                print temp_list[-1]
            else:
                print 'ERROR:', json_obj['Error']
            #if i == 10:
            #    break
            #i = i+1
        pickle.dump(temp_list, json_dump)
        json_dump.close()

def read():
    """ Reads the json_dump into a list and returns it """
    temp_list = []
    with open('dump', 'rb') as dump_file:
        temp_list = pickle.load(dump_file)
    return temp_list

def parse_input(name):
    """ Takes in a movie name and gets rid of abnormalities in it """
    name = name.strip()
    if name[0] == '\"':
        name = name[1:]
    if name[-1] == '\"':
        name = name[:-1]
    return name

# write()
rating_list = read()
sorted_list = sorted(rating_list, key=lambda x: x[1])
for item in sorted_list:
    print item[0], item[1]
