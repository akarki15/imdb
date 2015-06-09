# imdb

### Setup Instructions 
  _Install Dependencies_ 
  - Clone the repo and cd into it
  - Setup a virtualenv 
  
  ```virtualenv venv ```
  - Activate virtualenv
    
  ``` source venv/bin/activate```
  - Install dependencies
    
  ``` pip install -r requirements.txt```
  
_Get the imdb ratings and serve it through a webserver_ 
  - Run the following python script to 

  ``` python setup.py```

  - Run server to see the output at ```http://localhost:8080/rating_list/```
   
  ``` python run.py```


### Explanation of how the webapp works
  - ```setup.py``` reads ```app/static/movies.csv``` and makes sequential get requests to the imdb api. It then stores those results to a file (```app/static/dump```). 
  - ```run.py``` creates a little flask app and serves the results at the localserver. 


### Edge Cases encountered and dealt with
  - Random spaces and double quotes while reading the movies.csv file
  - The API did not have records for some movies. In such cases I did not add those records to the file where I was storing the imdb ratings (```app/static/dump```)
  - Some JSON reponses for movies had ```'N/A'``` for  ```imdbRating``` field. In those cases, I did not store those records to the dump. 
  
  

