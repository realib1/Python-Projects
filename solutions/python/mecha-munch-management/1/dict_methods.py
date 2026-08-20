"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    updated_cart = current_cart.copy()
    for item in items_to_add:
        updated_cart[item] = updated_cart.get(item, 0) + 1
    return updated_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    new_cart = {}
    for item in notes:
        new_cart[item] = new_cart.setdefault(item, 0) + 1
    return new_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()
    for recipe_name, new_ingredients in recipe_updates:
        updated_ideas[recipe_name] = new_ingredients
    return updated_ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    new_cart_mapping = {}
    for item in sorted(cart.keys(), reverse=True):
        if item in aisle_mapping:
            quantity = cart[item]
            new_cart_mapping[item] = [quantity] + aisle_mapping[item]
    return new_cart_mapping


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    stock_update = {}
    for item in sorted(store_inventory.keys(), reverse=True):
        if item in fulfillment_cart:
            new_stock = store_inventory[item][0] - fulfillment_cart[item][0]
            stock_status = new_stock if new_stock > 0 else "Out of Stock"
        else:
            stock_status = store_inventory[item][0]
    
        stock_update[item] = [stock_status] + store_inventory[item][1:]
    return stock_update
