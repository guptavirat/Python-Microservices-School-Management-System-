from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.mod_people.forms import PersonForm
from app.mod_people.models import Person

mod_people = Blueprint('people', __name__, url_prefix='/Admin')


@mod_people.route('/')
def index():
    people = Person.query.all()
    return render_template('people/index.html', people=people)


@mod_people.route('/new', methods=['GET', 'POST'])
def new():
    form = PersonForm(request.form)
    if request.method == "POST" and form.validate():
        person = Person(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                        phone=form.phone.data, eid=form.eid.data, gen=form.gen.data, cls=form.cls.data,
                        Adr=form.Adr.data, bgr=form.bgr.data, fname=form.fname.data, mname=form.mname.data,
                        dob=form.dob.data)

        db.session.add(person)
        db.session.commit()

        return redirect(url_for('people.index'))

    return render_template('people/new.html', form=form)


@mod_people.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    person = Person.query.get(id)
    form = PersonForm(formdata=request.form, obj=person)
    if request.method == "POST" and form.validate():
        form.populate_obj(person)
        db.session.commit()
        return redirect(url_for('people.index'))

    return render_template('people/edit.html', form=form, person=person)


@mod_people.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('people.index'))
