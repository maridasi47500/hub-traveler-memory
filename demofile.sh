
mkdir templates 
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py userarrival hub_id:references date
python3 scaffold.py linkkarmavideo user_id:references karma_video_id:references
python3 scaffold.py linkkarmaphoto user_id:references karma_photo_id:references
python3 scaffold.py linkkarmasound user_id:references karma_sound_id:references
python3 scaffold.py linkkarmaprogram user_id:references karma_program_id:references
python3 scaffold.py city country_id:references name
python3 scaffold.py airport_hub name city_id:references
python3 scaffold.py country name
python3 scaffold.py karma_video user_id:references vid:file description
python3 scaffold.py karma_photo user_id:reference pic:file description
python3 scaffold.py karma_sound user_id:reference zik:file description
python3 scaffold.py karma_program user_id:reference script:file description
python3 scaffold.py welcome_video title vid
python3 scaffold.py welcome_sound title zik
