from flask import Flask, render_template
app = Flask(__name__)

# dummy dictionaries
restaurant = {'name': 'The CRUDy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'}, {'name':'Taco Hut', 'id':'3'}]

items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



@app.route('/')
@app.route('/restaurants')
def showRestaurants():
	return render_template('restaurants.html')

@app.route('/restaurant/new')
def newRestaurant():
	return render_template('newrestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
	return render_template('editrestaurant.html', restaurant=restaurant, restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
	return render_template('deleterestaurant.html', restaurant=restaurant, restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
	 return render_template('menu.html', restaurant=restaurant, items=items, restaurant_id=restaurant_id)
	
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
	return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
	return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
	return render_template('deletemenuitem.html', item=item)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)

