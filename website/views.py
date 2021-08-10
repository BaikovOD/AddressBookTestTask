from flask import Blueprint, render_template, request, flash, \
    jsonify, redirect, url_for, get_flashed_messages
from . import db
from .models import Address, AddressValue
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for("views.addresses"))


# Addresses

def get_addr_list(value=None):
    if value is None:
        return Address.query.all()

    elif value not in AddressValue.__members__:
        # not in enum
        flash("Incorrect value in filter", category="error")
        return Address.query.all()

    else:
        addr_list = Address.query.filter_by(value=value).all()
        if addr_list:
            return addr_list

    # return empty list
    return []


def process_addr_info(source, flashMsg=False):
    columns = ['name', 'address', 'city', 'state', 'postal_code', 'value']
    values_dict = {}
    errors = False
    for col in columns:
        col_val = source.get(col)
        if col_val is None:
            values_dict[col] = ''
            if flashMsg:
                flash(f"Field '{col}' is empty!", category='error')
            errors = True
        else:
            values_dict[col] = col_val

    return (errors, values_dict)


@views.route('/addresses/')
def addresses():
    addr_list = get_addr_list()
    return render_template("addresses.html", addresses=enumerate(addr_list), disabled_all='disabled')


@views.route('/addresses/parse/', methods=['GET', 'POST'])
def addresses_parse():
    if request.method == 'POST' and request.form.get('data') is not None:
        # ---------------------
        # Add new addresses
        data = json.loads(request.form.get('data'))
        if data is None or len(data) == 0:
            flash("No JSON data vas entered!", category="error")
        else:
            for addr in data:
                errors, addr_info = process_addr_info(addr, flashMsg=False)
                if not errors:
                    new_address = Address(**addr_info)
                    db.session.add(new_address)

            db.session.commit()
            flash('New addresses successfully parsed and added!', category='success')

            return redirect(url_for('views.addresses'))

    return render_template("addresses_parse.html")


@views.route('/addresses/filter/')
def addresses_filter():
    addr_list = get_addr_list(request.args.get('value'))
    disabled_dict = {'disabled_' + request.args.get('value'):'disabled'}
    return render_template("addresses.html", addresses=enumerate(addr_list), **disabled_dict)


@views.route('/addresses/add', methods=['GET', 'POST'])
def address_add():
    if request.method == 'POST':
        # add new Address
        errors, addr_info = process_addr_info(request.form, flashMsg=True)
        if not errors:
            new_address = Address(**addr_info)
            db.session.add(new_address)
            db.session.commit()
            flash('New address successfully added!', category='success')

    return render_template("address_add.html")
