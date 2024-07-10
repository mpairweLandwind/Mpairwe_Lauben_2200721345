from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Create wildconservation species list
species_list =[
    {'name': 'Blue Morpho', 'habitat': 'rainforests', 'conservation_status': 'Endangered'},
    {'name': 'Giant Panda', 'habitat': 'rainforests', 'conservation_status': 'Threatened'},
    {'name': 'African Elephant', 'habitat': 'savannahs', 'conservation_status': 'Vulnerable'},
     {'name': 'Falcon', 'habitat': 'Antarcticas', 'conservation_status': 'Vulnerability'},
     {'name': 'Eagle', 'habitat': 'Antarcticas', 'conservation_status': 'Critically Endangered'},
     {'name': 'Blue Whale', 'habitat': 'Seas', 'conservation_status': 'Critically Endangered'},
     {'name': 'Polar Bear', 'habitat': 'Arctic and Antarctic', 'conservation_status': 'Critically Endangered'},
     {'name': 'Snail', 'habitat': 'Freshwater ecosystems', 'conservation_status': 'Critically Endangered'},
     {'name': 'Bat', 'habitat': 'Bat', 'conservation_status'   : 'Critically Endangered'},
 
    # Add more species as needed
]

@app.route('/')
def index():
    return render_template('index.html',species_list=species_list)

@app.route('/add', methods=['POST','GET'])
def add_species():
    if request.method == 'POST':
        name = request.form['name']
        habitat = request.form['habitat']
        conservation_status = request.form['conservation_status']
        species_list.append({'name': name, 'habitat': habitat, 'conservation status': conservation_status})
        return redirect(url_for('index'))
    return render_template('add_species.html');


if __name__ == '__main__':
    app.run(debug=True)
    
    