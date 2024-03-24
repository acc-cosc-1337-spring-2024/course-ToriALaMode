def add_inventory(widgets, widget_name, quantity):
    """
    Add or update the quantity of a widget in the inventory.

    Parameters:
        widgets (dict): A dictionary representing the inventory of widgets.
        widget_name (str): The name of the widget to add or update.
        quantity (int): The quantity of the widget.

    Returns:
        None
    """
    if widget_name in widgets:
        # Update quantity if the widget already exists
        widgets[widget_name] += quantity
    else:
        # Add the widget with the given quantity
        widgets[widget_name] = quantity


def remove_inventory_widget(widgets, widget_name):
    """
    Remove a widget from the inventory.

    Parameters:
        widgets (dict): A dictionary representing the inventory of widgets.
        widget_name (str): The name of the widget to remove.

    Returns:
        str: Message indicating if the widget was successfully removed or not.
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return "Record deleted"
    else:
        return "Item not found"