from website.models import Address, AddressValue
from . import db


def get_list(value=None):
    """
    Fetches/filters all the addresses from db

    :param value:AddressValue - filter by value enum(low, medium, high)
    :returns tuple(error_messages, address_list)
    """

    if value is None:
        return ("", Address.query.all())

    elif value not in AddressValue.__members__:
        # not in enum
        return ("Incorrect value in filter", Address.query.all())

    else:
        addr_list = Address.query.filter_by(value=value).all()
        return ("", addr_list)


def process_and_get(source):
    """
    processes the source and checks the fields emptiness
    :param source: filter by value (low, medium, high)
    :returns tuple(column_errors_list, values_dict)
    """
    # TODO:EMPTY COLUMNS GO LIKE NOT ASSIGNED

    columns = ['name', 'address', 'city', 'state', 'postal_code', 'value']
    values_dict = {}
    column_errors = []
    for col in columns:
        col_val = source.get(col)
        if col_val is None or col_val == "":
            values_dict[col] = ''
            column_errors.append(f"Field '{col}' is empty!")
        else:
            values_dict[col] = col_val
    values_dict['created'] = None

    return (column_errors, values_dict)


def add_one(addr_info):
    new_address = Address(**addr_info)
    db.session.add(new_address)
    db.session.commit()


def add_many(addr_list):
    """
    adds all the addresses to the database
    :param addr_list:
    :return: {"success":True/False, "added":list of added addresses}
    """

    added_list = []
    for addr in addr_list:
        errors, addr_info = process_and_get(addr)
        if not errors:
            new_address = Address(**addr_info)
            addr_info['created'] = new_address.created
            db.session.add(new_address)
            added_list.append(addr_info)

    db.session.commit()

    return {"success": True, "added": added_list}