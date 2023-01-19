from flask import Flask, redirect, render_template, request, flash
from models import db, Pet, connect_db
from flask_debugtoolbar import DebugToolbarExtension
import subprocess
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "Testing"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

try:
    command = "psql -c 'create database adopt'"
    subprocess.call(command, shell = True)
except:
    print(Exception)
    print("Moving on then")

    
connect_db(app)

with app.app_context():
    db.create_all()


#==================================HOME=====================================
@app.route("/", methods=['GET'])
def home():
    """Displays our list of pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

#==================================ADD======================================
@app.route("/add", methods=['GET','POST'])
def add_pet():
    """Pet add form; handles adding"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet()
        form.populate_obj(pet)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name} the {species}")
        return redirect("/add")
    else:
        return render_template("/pet_add_form.html", form = form)

#==============================DISPLAY/EDIT=================================
@app.route("/<int:pet_id>", methods=['GET','POST'])
def edit_pet(pet_id):
    """Display pet edit form and handle edit"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Changes Saved")
        return redirect(f"/{pet_id}")
    else:
        return render_template("/pet_edit_form.html", form=form, pet=pet)