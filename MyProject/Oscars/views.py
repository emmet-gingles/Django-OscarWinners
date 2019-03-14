from django.shortcuts import render			# For rendering templates
from django.db import connections			# For MySQL connections

# Function that returns that returns all rows from a specified table. 
# It takes three parameters the first one being the table name
# The second parameter is a boolean winnersOnly that determines whether or not only Oscar winners are returned.
# The third parameter is startYear which has a default value of None. When specified only data after that year is returned.
def getData(table, winnersOnly, startYear=None):
	# Get MySQL connection parameters from the settings file
	cursor = connections['default'].cursor()
	# If True then return only rows that are winners
	if winnersOnly:
		# If startYear is specified then only return rows that are greater than or equal to startYear
		if startYear != None:
			cursor.execute("SELECT * FROM "+table + " WHERE Winner = 'Yes' AND year >= "+startYear+"")
		else:
			cursor.execute("SELECT * FROM "+table + " WHERE Winner = 'Yes'")
	# Otherwise it is False so return all rows
	else:
		if startYear != None:
			cursor.execute("SELECT * FROM "+table + " WHERE year >= "+startYear+"")
		else:
			cursor.execute("SELECT * FROM "+table + "")
	# Retrieve all the rows and return them
	res = cursor.fetchall()
	return res
	
# Function that returns all best actor winners 
# This is achieved by calling the getData function and passing in the boolean True for the winnersOnly parameter to return only certain rows from the table
# The data is then sent to a HTML template where it is viewed by the user
def showActorWinners(request):
	# If startYear is specified in the parameters then save it to variable. If not specified set variable to ''
	startYear = request.GET.get('startyear', '')
	# If the startYear variable is set then use it in function call 
	if startYear != '':
		# Call function to get all rows from nominee_best_actor table passing in True for winnersOnly and the startYear 
		res = getData("nominee_best_actor", True, startYear)
	# Otherwise call the function without a startYear
	else:
		res = getData("nominee_best_actor", True)
	# Render the HTML template and pass in the query results and the type of data
	return render(request, "showWinners.html", {"results" : res, "type" : "actor" })

# Function that returns all best actress winners 	
def showActressWinners(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_actress", True, startYear)
	else:
		res = getData("nominee_best_actress", True)
	return render(request, "showWinners.html", {"results" : res, "type" : "actress" })

# Function that returns all best supporting actor winners 
def showSupportingActorWinners(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_supporting_actor", True, startYear)
	else:
		res = getData("nominee_best_supporting_actor", True)
	return render(request, "showWinners.html", {"results" : res, "type" : "supporting actor" })

# Function that returns all best supporting actress winners
def showSupportingActressWinners(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_supporting_actress", True, startYear)
	else:
		res = getData("nominee_best_supporting_actress", True)
	return render(request, "showWinners.html", {"results" : res, "type" : "supporting actress" })
	
# Function that returns all best director winners
def showDirectorWinners(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_director", True, startYear)
	else:
		res = getData("nominee_best_director", True)
	return render(request, "showWinners.html", {"results" : res, "type" : "director" })

# Function that returns all best picture winners
def showPictureWinners(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_picture", True, startYear)
	else:
		res = getData("nominee_best_picture", True)
	return render(request, "showWinners.html", {"results" : res, "type" : "picture" })
	
	
# Function that returns all best actor nominees
# This is achieved by calling the getData function and passing in the boolean False for the winnersOnly parameter to return all rows from the table
# The data is then sent to a HTML template where it is viewed by the user
def showActorNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_actor", False, startYear)
	else:
		res = getData("nominee_best_actor", False)	
	return render(request, "showNominees.html", {"results" : res, "type" : "actor" })

# Function that returns all best actress nominees
def showActressNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_actress", False, startYear)
	else:
		res = getData("nominee_best_actress", False)
	return render(request, "showNominees.html", {"results" : res, "type" : "actress" })

# Function that returns all best supporting actor nominees
def showSupportingActorNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_supporting_actor", False, startYear)	
	else:
		res = getData("nominee_best_supporting_actor", False)	
	return render(request, "showNominees.html", {"results" : res, "type" : "supporting actor" })
		
# Function that returns all best supporting actress nominees	
def showSupportingActressNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_supporting_actress", False, startYear)
	else:
		res = getData("nominee_best_supporting_actress", False)
	return render(request, "showNominees.html", {"results" : res, "type" : "supporting actress" })
		
# Function that returns all best director nominees		
def showDirectorNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_director", False, startYear)
	else:
		res = getData("nominee_best_director", False)
	return render(request, "showNominees.html", {"results" : res, "type" : "director" })
	
# Function that returns all best picture nominees
def showPictureNominees(request):
	startYear = request.GET.get('startyear', '')
	if startYear != '':
		res = getData("nominee_best_picture", False, startYear)
	else:
		res = getData("nominee_best_picture", False)
	return render(request, "showNominees.html", {"results" : res, "type" : "pictue" })
	
# Function that returns all information for a particular year. Can be just all nominees or just winners
# Data is sent to a HTML template where it is viewed by the user
def showYear(request, year):
	# Variables to store the minimum and maximum year 
	minYear = 1928
	maxYear = 2018
	
	# If the year is outside of the minimum and maximum then render the 404 template and pass in a message for the user
	if int(year) < minYear or int(year) > maxYear:
		return render(request, "404.html", {"message" : "Please enter a number between {0} and {1}".format(minYear, maxYear) });
	else:
		# Get the path of the request eg. oscars/winners/year/2018
		path = request.get_full_path()
		# Split the path and retrieve the second index 
		type = path.split('/')[2]
		
		cursor = connections['default'].cursor();
		# If the type is winners
		if type == "winners":	
			# For each table retrieve all rows that are winners and have that year.
			# Create variable for storing each table's data 
			cursor.execute("SELECT actor, film FROM nominee_best_actor WHERE winner = 'Yes' AND year = "+year);
			actor = cursor.fetchall();
			cursor.execute("SELECT actress, film FROM nominee_best_actress WHERE winner = 'Yes' AND year = "+year);
			actress = cursor.fetchall();
			cursor.execute("SELECT director, film film FROM nominee_best_director WHERE winner = 'Yes' AND year = "+year);
			director = cursor.fetchall();
			cursor.execute("SELECT film, producers FROM nominee_best_picture WHERE winner = 'Yes' AND year = "+year);
			picture = cursor.fetchall();
			cursor.execute("SELECT actor, film FROM nominee_best_supporting_actor WHERE winner = 'Yes' AND year = "+year);
			supActor = cursor.fetchall();
			cursor.execute("SELECT actress, film FROM nominee_best_supporting_actress WHERE winner = 'Yes' AND year = "+year);
			supActress = cursor.fetchall();
			# Render the HTML template passing in all the variables
			return render(request, "showYear.html", {"year": year, "picture": picture, "director": director, "actor": actor, "actress": actress, "supporting_actor": supActor, "supporting_actress": supActress });
		# Otherwise type is nominees	
		else:
			# For each table retrieve all rows that have that year.
			# Create variable for storing each table's data 
			cursor.execute("SELECT actor, film, winner FROM nominee_best_actor WHERE year = "+year);
			actor = cursor.fetchall();
			cursor.execute("SELECT actress, film, winner FROM nominee_best_actress WHERE year = "+year);
			actress = cursor.fetchall();
			cursor.execute("SELECT director, film, winner film FROM nominee_best_director WHERE year = "+year);
			director = cursor.fetchall();
			cursor.execute("SELECT film, producers, winner FROM nominee_best_picture WHERE year = "+year);
			picture = cursor.fetchall();
			cursor.execute("SELECT actor, film, winner FROM nominee_best_supporting_actor WHERE year = "+year);
			supActor = cursor.fetchall();
			cursor.execute("SELECT actress, film, winner FROM nominee_best_supporting_actress WHERE year = "+year);
			supActress = cursor.fetchall();
			# Render the HTML template passing in all the variables
			return render(request, "showYearNominees.html", {"year": year, "picture": picture, "director": director, "actor": actor, "actress": actress, "supporting_actor": supActor, "supporting_actress": supActress });

# Function that searches both actor tables and return all the films they were nominated for 
# Underscores should be used for the search parameter instead of spaces eg. "tom_hanks"	
def searchActor(request, search):
	cursor = connections['default'].cursor();
	# Replace any underscores with spaces
	search = search.replace("_", " ")
	# Return all rows from both table that match the search parameter.
	# Use UNION to combine both results set into one and order the results by year
	cursor.execute("SELECT year, film, winner FROM nominee_best_actor WHERE actor LIKE '%"+search +"' \
	UNION SELECT year, film, winner from nominee_best_supporting_actor WHERE actor LIKE '%"+search+"' ORDER BY year");
	res = cursor.fetchall()
	# Return HTML template passing in the variables
	return render(request, "showInfo.html", {"results": res, "name": search, "type": "actor"})
	
# Function that searches both actress tables and return all the films they were nominated for 
# Underscores should be used for the search parameter instead of spaces eg. "meryl_streep"	
def searchActress(request, search):
	cursor = connections['default'].cursor();
	search = search.replace("_", " ")
	cursor.execute("SELECT year, film, winner FROM nominee_best_actress WHERE actress LIKE '%"+search +"' \
	UNION SELECT year, film, winner from nominee_best_supporting_actress WHERE actress LIKE '%"+search+"' ORDER BY year");
	res = cursor.fetchall()
	return render(request, "showInfo.html", {"results": res, "name": search, "type": "actress"})

# Function that searches the director table and returns all the films they were nominated for 	
# Underscores should be used for the search parameter instead of spaces eg. "steven_spielberg"	
def searchDirector(request, search):
	cursor = connections['default'].cursor();
	search = search.replace("_", " ")
	cursor.execute("SELECT year, film, winner FROM nominee_best_director WHERE director LIKE '%"+search +"' ORDER BY year");
	res = cursor.fetchall()
	return render(request, "showInfo.html", {"results": res, "name": search, "type": "director"})
	
# Function that returns a summary of data for each actor/actress/director 
# Summary data include both number of nominations and number of wins 
# Parameters are the data type, the order of the data and whether to sort in ascending or descending order (default is descending)
def getSumData(data, order, sort="DESC"):
	cursor = connections['default'].cursor();
	# Searching both actor tables
	if data == "actor":
		# If order is "actor" then order as "actor, total_wins, total_nomination"
		if order == 'actor':
			orderby = "actor "+sort+", total_wins DESC, total_noms DESC"
		# If order is "nominations" then order as "total_nomination, total_wins, actor"
		elif order == "nominations":
			orderby = "total_noms "+sort+", total_wins DESC, actor ASC"
		# Else order is "wins" then order as "total_wins, total_nomination, actor"
		else:
			orderby = "total_wins "+sort+", total_noms DESC, actor ASC"	
		# Call query to return the total wins and total nominations for each actor
		# A subquery is used to combine the results from both 'nominee_best_actor' and 'nominee_best_supporting_actor' tables
		cursor.execute("SELECT actor, SUM(total_noms) AS total_noms, SUM(total_wins) AS total_wins \
		FROM (SELECT actor, COUNT(actor) AS total_noms, COUNT(IF(winner = 'Yes', 1, null)) AS total_wins FROM nominee_best_actor \
		GROUP BY actor UNION SELECT actor, COUNT(actor) AS total_noms, COUNT(IF(winner = 'Yes', 1, null)) AS total_wins \
		FROM nominee_best_supporting_actor GROUP BY actor) AS res \
		GROUP BY actor ORDER BY "+orderby)
	# Searching both actress tables
	elif data == "actress":
		if order == 'actress':
			orderby = "actress "+sort+", total_wins DESC, total_noms DESC"
		elif order == "nominations":
			orderby = "total_noms "+sort+", total_wins DESC, actress ASC"
		else:
			orderby = "total_wins "+sort+", total_noms DESC, actress ASC"	
		# Call query to return the total wins and total nominations for each actress
		# A subquery is used to combine the results from both 'nominee_best_actress' and 'nominee_best_supporting_actress' tables
		cursor.execute("SELECT actress, SUM(total_noms) AS total_noms, SUM(total_wins) AS total_wins \
		FROM (SELECT actress, COUNT(actress) AS total_noms, COUNT(IF(winner = 'Yes', 1, null)) AS total_wins FROM nominee_best_actress \
		GROUP BY actress UNION SELECT actress, COUNT(actress) AS total_noms, COUNT(IF(winner = 'Yes', 1, null)) AS total_wins \
		FROM nominee_best_supporting_actress GROUP BY actress) AS res \
		GROUP BY actress ORDER BY "+orderby)
	# Searching director table
	else:
		if order == 'director':
			orderby = "director "+sort+", total_wins DESC, total_noms DESC"
		elif order == "nominations":
			orderby = "total_noms "+sort+", total_wins DESC, director ASC"
		else:
			orderby = "total_wins "+sort+", total_noms DESC, director ASC"	
		# Call query to return the total wins and total nominations for each director 
		# Substring is used to remove any brackets from the director names
		cursor.execute("SELECT DISTINCT( IF(SUBSTRING(Director, LENGTH(Director)) = ')', \
		SUBSTRING(Director, 1, POSITION('(' IN Director)-1), Director)) \
		AS name, COUNT(Director) AS total_noms, COUNT(IF(winner = 'Yes', 1, null)) AS total_wins \
		FROM nominee_best_director GROUP BY name ORDER BY "+orderby);
	res = cursor.fetchall();
	return(res);
	
# Function that is used to set the sort parameter
def setSort(sort):
	# Convert sort parameter to lowercase
	sort = sort.lower()
	#  If sort is 'true' then return "ASC"
	if sort == 'true':
		return "ASC"
	# Else if sort is 'false' then return "DESC"
	elif sort == 'false':
		return "DESC"
	# Else return an empty string
	else:
		return ''
	
# Function that returns actors ordered by their total nominations
def showActorsByNomination(request):
	# If the orderby parameter is specified in the URL then save it to a variable. If not then set variable to an empty string 
	orderby = request.GET.get('orderby', '')
	# If the asc parameter is specified in the URL then save it to a variable. If not then set variable to an empty string
	ascending = request.GET.get('asc', '')
	# If both parameters are set
	if orderby != '' and ascending != '':
		# Call function to get the sort using the ascending variable
		sort = setSort(ascending)
		# If it is not empty then call the getSumData() function passing in the parameters - 'actor', orderby and sort
		if sort != '':
			res = getSumData("actor", orderby, sort);
		# Else sort is empty so call the getSumData() function passing in the first two parameters
		else:
			res = getSumData("actor", orderby)
	# Otherwise one or both parameters are not set 
	else:
		# Call getSumData() function passing in the parameters - 'actor' and 'nominations' for the order
		res = getSumData("actor", "nominations")
	# Render HTML template passing in the results set and the type
	return render(request, "showMostNominations.html", {"results": res, "type": "actor"})
	
# Function that returns actresses ordered by their total nominations
def showActressesByNomination(request):
	orderby = request.GET.get('orderby', '')
	ascending = request.GET.get('asc', '')
	if orderby != '' and ascending != '':
		sort = setSort(ascending)
		if sort != '':
			res = getSumData("actress", orderby, sort);
		else:
			res = getSumData("actress", orderby)
	else:
		res = getSumData("actress", "nominations")
	return render(request, "showMostNominations.html", {"results": res, "type": "actress"})

# Function that returns directors ordered by their total nominations	
def showDirectorsByNomination(request):
	orderby = request.GET.get('orderby', '')
	ascending = request.GET.get('asc', '')
	if orderby != '' and ascending != '':
		sort = setSort(ascending)
		if sort != '':
			res = getSumData("director", orderby, sort);
		else:
			res = getSumData("director", orderby)
	else:
		res = getSumData("director", "nominations")
	return render(request, "showMostNominations.html", {"results": res, "type": "director"})
	
# Function that returns actors ordered by their total wins
def showActorsByWins(request):
	orderby = request.GET.get('orderby', '')
	ascending = request.GET.get('asc', '')	
	if orderby != '' and ascending != '':
		sort = setSort(ascending)
		if sort != '':
			res = getSumData("actor", orderby, sort);
		else:
			res = getSumData("actor", orderby)
	else:
		res = getSumData("actor", "wins")
	return render(request, "showMostWins.html", {"results": res, "type": "actor"})
	
# Function that returns actresses ordered by their total wins
def showActressesByWins(request):
	orderby = request.GET.get('orderby', '')
	ascending = request.GET.get('asc', '')	
	if orderby != '' and ascending != '':
		sort = setSort(ascending)
		if sort != '':
			res = getSumData("actress", orderby, sort);
		else:
			res = getSumData("actress", orderby)
	else:
		res = getSumData("actress", "wins")
	return render(request, "showMostWins.html", {"results": res, "type": "actress"})
	
# Function that returns directors ordered by their total wins
def showDirectorsByWins(request):
	orderby = request.GET.get('orderby', '')
	ascending = request.GET.get('asc', '')	
	if orderby != '' and ascending != '':
		sort = setSort(ascending)
		if sort != '':
			res = getSumData("director", orderby, sort);
		else:
			res = getSumData("director", orderby)
	else:
		res = getSumData("director", "wins")
	return render(request, "showMostWins.html", {"results": res, "type": "director"})
	
	
