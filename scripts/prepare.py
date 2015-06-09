""" script to download all data from imdb """

import urllib2, urllib, json, pickle

def write_dump(input_file, output_file):
    """ Reads movies.csv file, gets the imbd rating and stores that into a file """
    temp_list = []
    counter = 1
    with open(input_file) as file1:
        for line in file1:
            name = parse_input(line.split(',')[0])
            params = urllib.urlencode({'t':name, 'r':'json'})
            response = urllib2.urlopen("http://www.omdbapi.com/?"+params).read()
            json_obj = json.loads(response)
            if json_obj['Response'] == 'True':
                if json_obj['imdbRating'] != 'N/A':
                    temp_list.append([name, json_obj['imdbRating']])
                    print temp_list[-1]
            else:
                print 'ERROR:', json_obj['Error']
            # if counter == 7:
            #    break
            counter+=1
    # Sort the list
    if len(temp_list) > 0:
        sorted_list = sorted(temp_list, key=lambda x: x[1], reverse=True)
        with open(output_file, 'w+') as json_dump:
            pickle.dump(sorted_list, json_dump)
            #for s in sorted_list:
            #    json_dump.write(s)

def read_dump(path_dump):
    """ Reads the json_dump into a list and returns it """
    temp_list = []    
    with open(path_dump, 'rb') as dump_file:
        temp_list = pickle.load(dump_file)
        # temp_list = [line.rstrip(u'\n') for line in dump_file]
    return temp_list

def parse_input(name):
    """ Takes in a movie name and gets rid of abnormalities in it """
    name = name.strip()
    if name[0] == '\"':
        name = name[1:]
    if name[-1] == '\"':
        name = name[:-1]
    return name

def print_ratings(path_dump):
    """ Prints the ratings. Used for debugging """
    rating_list = read_dump(path_dump)
    for item in rating_list:
        print item[0], item[1]
