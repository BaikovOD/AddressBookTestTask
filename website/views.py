from flask import Blueprint, render_template, request, flash, \
    jsonify, redirect, url_for, abort
import website.address_operations as addrOper
import json
from .settings import API_KEY


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for("views.addresses"))

# ---------------------------------------------
# Addresses blueprints

@views.route('/addresses/')
def addresses():
    """full list of addresses"""

    error, addr_list = addrOper.get_list()
    if error:
        flash(error, category='error')
    html_params = {
        "addresses": enumerate(addr_list),
        'disabled_btn_all': 'disabled'
    }
    return render_template("addresses.html", **html_params)


@views.route('/addresses/import/', methods=['GET', 'POST'])
def addresses_import():
    """import addresses via json loader"""

    if request.method == 'POST' and request.form.get('data') is not None:
        # ---------------------
        # Add new addresses
        data = json.loads(request.form.get('data'))
        if data is None or len(data) == 0:
            flash("No JSON data was entered!", category="error")
        else:
            addrOper.add_many(data)
            flash('New addresses successfully parsed and added!', category='success')

            return redirect(url_for('views.addresses'))
    else:
        return render_template("addresses_import.html")


@views.route('/addresses/parse/', methods=['POST'])
def addresses_parse():
    """External API ENDPOINT: Parses the JSON data and adds all the new addresses
    params:
        key - secret key
        json_data - json data with addresses

    returns json {"success":"true/false"}
    """

    if request.form.get('key') != API_KEY:
        abort(403, description="Incorrect key")
        
    json_data = request.form.get('json_data')
    if json_data is None or json_data == "":
        abort(400, description='data is empty')

    addr_list = json.loads(json_data)
    return jsonify(addrOper.add_many(addr_list))


@views.route('/addresses/filter/')
def addresses_filter():
    """filtered by value list of addresses"""

    error, addr_list = addrOper.get_list(request.args.get('value'))
    if error:
        flash(error, category='error')
    html_params = {
        "addresses": enumerate(addr_list),
        'disabled_btn_' + request.args.get('value'):'disabled'
    }
    return render_template("addresses.html", **html_params)


@views.route('/addresses/add', methods=['GET', 'POST'])
def address_add():
    """new address addition"""

    if request.method == 'POST':
        # add new Address
        errors, addr_info = addrOper.process_and_get(request.form)
        if errors:
            for error in errors:
                flash(error, category='error')
        else:
            addrOper.add_one(addr_info)
            flash('New address successfully added!', category='success')

    return render_template("address_add.html")
