from urllib import response
from flask import *

app = Flask(__name__)

@app.route('/')

def index():
    if request.method == 'GET':
        whereFrom = request.args.get('from')
        whereTo = request.args.get('to')

        response = None
        '''
        query the database to fetch all TRAINs where
        
        SELECT 
            train.name, train.fare, route.arrival, route.departure, route.id, route|station.position
        FROM 
            train, train|route, route, route|station, station
        WHERE 
            train.routeid = route.id AND
            route.id = route|station.routeid AND
            route|station.stationid = station.id AND
            station.name = whereFrom
        ORDER BY
            (train.name, route|station.position, route.arrival)
        
        SELECT 
            train.name, train.fare, route.arrival, route.departure, route.id, route|station.position
        FROM 
            train, train|route, route, route|station, station
        WHERE 
            train.routeid = route.id AND
            route.id = route|station.routeid AND
            route|station.stationid = station.id AND
            station.name = whereTo
        ORDER BY
            (train.name, route|station.position, route.arrival)
        '''
        HTMLReturn = """<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Serach Trains</title>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
  <link rel="stylesheet" href="css/main.css">

  <script>
	document.getElementById("search-btn").addEventListener("click", myFunction);
	function myFunction1() {
	  window.location.href="pay.html";
	}
</script>
</head>

<body>
  <h1>
  Train Routes
</h1>
<main>
  <table>
    <thead>
      <tr>
        <th>
          Train Name
        </th>
        <th>
          Starting place
        </th>
        <th>
          Destination Place
        </th>
        <th>
          Fare
        </th>
        <th>
          Arrival Time
        </th>
		<th>
		  Departure Time
		  </th>
      </tr>
      
    </thead>
   
    <tbody>"""

    if response:
        for trainData in response:
            HTMLReturn += """<tr>
        <td data-title='Train Name'>
			#%s
        </td>
        <td data-title='Starting place'>
			#%s
        </td>
        <td data-title='Destination Place'>
			#%s
        </td>
        <td data-title='Fare'>
			#%s
        </td>
        <td data-title='Time'>
			#%s
        </td>
        <td data-title='Time'>
			#%s
        </td>
        <td class='select'>
			<button onclick="window.location.href='pay.html'">Book</button>
        </td>
      </tr>""" %trainData.name %trainData.start %trainData.end %trainData.fare %trainData.arrival %trainData.departure
    
    HTMLReturn += """</tbody>
  </table>
</main>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  <script src="js/index.js"></script>

</body>
</html>"""

    return HTMLReturn

if __name__ == '__main__':
    app.run('localhost', 8080)