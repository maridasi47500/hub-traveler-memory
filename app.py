from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_userarrival", methods=["GET","POST"])
def add_one_userarrival():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        tousleshub= query_db("select * from hub")

        one_user = query_db("insert into userarrival (hub_id,date) values (:hub_id,:date)",hey)
        user = query_db('select * from userarrival')

        return render_template("userarrivalform.html", userarrivals=user, one_user=one_user, the_title="add new userarrival", tousleshub=tousleshub)


    tousleshub= query_db("select * from hub")

    user = query_db('select * from userarrival')
    one_user = query_db("select * from userarrival limit 1", one=True)
    return render_template("userarrivalform.html", userarrivals=user, one_user=one_user, the_title="add new userarrival", tousleshub=tousleshub)

@app.route("/add_one_linkkarmavideo", methods=["GET","POST"])
def add_one_linkkarmavideo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        tousleskarma_video= query_db("select * from karma_video")

        one_user = query_db("insert into linkkarmavideo (user_id,karma_video_id) values (:user_id,:karma_video_id)",hey)
        user = query_db('select * from linkkarmavideo')

        return render_template("linkkarmavideoform.html", linkkarmavideos=user, one_user=one_user, the_title="add new linkkarmavideo", touslesuser=touslesuser, tousleskarma_video=tousleskarma_video)


    touslesuser= query_db("select * from user")

    tousleskarma_video= query_db("select * from karma_video")

    user = query_db('select * from linkkarmavideo')
    one_user = query_db("select * from linkkarmavideo limit 1", one=True)
    return render_template("linkkarmavideoform.html", linkkarmavideos=user, one_user=one_user, the_title="add new linkkarmavideo", touslesuser=touslesuser, tousleskarma_video=tousleskarma_video)

@app.route("/add_one_linkkarmaphoto", methods=["GET","POST"])
def add_one_linkkarmaphoto():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        tousleskarma_photo= query_db("select * from karma_photo")

        one_user = query_db("insert into linkkarmaphoto (user_id,karma_photo_id) values (:user_id,:karma_photo_id)",hey)
        user = query_db('select * from linkkarmaphoto')

        return render_template("linkkarmaphotoform.html", linkkarmaphotos=user, one_user=one_user, the_title="add new linkkarmaphoto", touslesuser=touslesuser, tousleskarma_photo=tousleskarma_photo)


    touslesuser= query_db("select * from user")

    tousleskarma_photo= query_db("select * from karma_photo")

    user = query_db('select * from linkkarmaphoto')
    one_user = query_db("select * from linkkarmaphoto limit 1", one=True)
    return render_template("linkkarmaphotoform.html", linkkarmaphotos=user, one_user=one_user, the_title="add new linkkarmaphoto", touslesuser=touslesuser, tousleskarma_photo=tousleskarma_photo)

@app.route("/add_one_linkkarmasound", methods=["GET","POST"])
def add_one_linkkarmasound():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        tousleskarma_sound= query_db("select * from karma_sound")

        one_user = query_db("insert into linkkarmasound (user_id,karma_sound_id) values (:user_id,:karma_sound_id)",hey)
        user = query_db('select * from linkkarmasound')

        return render_template("linkkarmasoundform.html", linkkarmasounds=user, one_user=one_user, the_title="add new linkkarmasound", touslesuser=touslesuser, tousleskarma_sound=tousleskarma_sound)


    touslesuser= query_db("select * from user")

    tousleskarma_sound= query_db("select * from karma_sound")

    user = query_db('select * from linkkarmasound')
    one_user = query_db("select * from linkkarmasound limit 1", one=True)
    return render_template("linkkarmasoundform.html", linkkarmasounds=user, one_user=one_user, the_title="add new linkkarmasound", touslesuser=touslesuser, tousleskarma_sound=tousleskarma_sound)

@app.route("/add_one_linkkarmaprogram", methods=["GET","POST"])
def add_one_linkkarmaprogram():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        tousleskarma_program= query_db("select * from karma_program")

        one_user = query_db("insert into linkkarmaprogram (user_id,karma_program_id) values (:user_id,:karma_program_id)",hey)
        user = query_db('select * from linkkarmaprogram')

        return render_template("linkkarmaprogramform.html", linkkarmaprograms=user, one_user=one_user, the_title="add new linkkarmaprogram", touslesuser=touslesuser, tousleskarma_program=tousleskarma_program)


    touslesuser= query_db("select * from user")

    tousleskarma_program= query_db("select * from karma_program")

    user = query_db('select * from linkkarmaprogram')
    one_user = query_db("select * from linkkarmaprogram limit 1", one=True)
    return render_template("linkkarmaprogramform.html", linkkarmaprograms=user, one_user=one_user, the_title="add new linkkarmaprogram", touslesuser=touslesuser, tousleskarma_program=tousleskarma_program)

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (country_id,name) values (:country_id,:name)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_airport_hub", methods=["GET","POST"])
def add_one_airport_hub():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into airport_hub (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from airport_hub')

        return render_template("airport_hubform.html", airport_hubs=user, one_user=one_user, the_title="add new airport_hub", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from airport_hub')
    one_user = query_db("select * from airport_hub limit 1", one=True)
    return render_template("airport_hubform.html", airport_hubs=user, one_user=one_user, the_title="add new airport_hub", touslescity=touslescity)

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_karma_video", methods=["GET","POST"])
def add_one_karma_video():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['vid']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["vid"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into karma_video (user_id,vid,description) values (:user_id,:vid,:description)",hey)
        user = query_db('select * from karma_video')

        return render_template("karma_videoform.html", karma_videos=user, one_user=one_user, the_title="add new karma_video", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from karma_video')
    one_user = query_db("select * from karma_video limit 1", one=True)
    return render_template("karma_videoform.html", karma_videos=user, one_user=one_user, the_title="add new karma_video", touslesuser=touslesuser)

@app.route("/add_one_karma_photo", methods=["GET","POST"])
def add_one_karma_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        one_user = query_db("insert into karma_photo (user_id:reference,pic,description) values (:user_id:reference,:pic,:description)",hey)
        user = query_db('select * from karma_photo')

        return render_template("karma_photoform.html", karma_photos=user, one_user=one_user, the_title="add new karma_photo")


    user = query_db('select * from karma_photo')
    one_user = query_db("select * from karma_photo limit 1", one=True)
    return render_template("karma_photoform.html", karma_photos=user, one_user=one_user, the_title="add new karma_photo")

@app.route("/add_one_karma_sound", methods=["GET","POST"])
def add_one_karma_sound():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['zik']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["zik"]=uploaded_file.filename


        one_user = query_db("insert into karma_sound (user_id:reference,zik,description) values (:user_id:reference,:zik,:description)",hey)
        user = query_db('select * from karma_sound')

        return render_template("karma_soundform.html", karma_sounds=user, one_user=one_user, the_title="add new karma_sound")


    user = query_db('select * from karma_sound')
    one_user = query_db("select * from karma_sound limit 1", one=True)
    return render_template("karma_soundform.html", karma_sounds=user, one_user=one_user, the_title="add new karma_sound")

@app.route("/add_one_karma_program", methods=["GET","POST"])
def add_one_karma_program():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['script']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["script"]=uploaded_file.filename


        one_user = query_db("insert into karma_program (user_id:reference,script,description) values (:user_id:reference,:script,:description)",hey)
        user = query_db('select * from karma_program')

        return render_template("karma_programform.html", karma_programs=user, one_user=one_user, the_title="add new karma_program")


    user = query_db('select * from karma_program')
    one_user = query_db("select * from karma_program limit 1", one=True)
    return render_template("karma_programform.html", karma_programs=user, one_user=one_user, the_title="add new karma_program")

@app.route("/add_one_welcome_video", methods=["GET","POST"])
def add_one_welcome_video():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into welcome_video (title,vid) values (:title,:vid)",hey)
        user = query_db('select * from welcome_video')

        return render_template("welcome_videoform.html", welcome_videos=user, one_user=one_user, the_title="add new welcome_video")


    user = query_db('select * from welcome_video')
    one_user = query_db("select * from welcome_video limit 1", one=True)
    return render_template("welcome_videoform.html", welcome_videos=user, one_user=one_user, the_title="add new welcome_video")

@app.route("/add_one_welcome_sound", methods=["GET","POST"])
def add_one_welcome_sound():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into welcome_sound (title,zik) values (:title,:zik)",hey)
        user = query_db('select * from welcome_sound')

        return render_template("welcome_soundform.html", welcome_sounds=user, one_user=one_user, the_title="add new welcome_sound")


    user = query_db('select * from welcome_sound')
    one_user = query_db("select * from welcome_sound limit 1", one=True)
    return render_template("welcome_soundform.html", welcome_sounds=user, one_user=one_user, the_title="add new welcome_sound")

