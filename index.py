from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
  return "Lists all the restaurants"


@app.route('/restaurant/new')
def newRestaurant():
  return "Adds new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
  return "Edit restaurant"


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
  return "Deletes restaurant"


@app.route('/restaurant/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
  return "Lists all menu items"


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
  return "Adds new menu item"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
  return "Edit menu item"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
  return "Delete menu item"


if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', port=5000)