let baseURL = "https://www.scopeandtrack.com/api"


function getStates() {
    let req = new XMLHttpRequest();
    url = baseURL + "/info/states";
    req.open("GET", url, true);

    req.onload = function () {

        let data = JSON.parse(this.response);

        if (req.status == 200) {
            let dropdown = document.getElementById("stateSelect");
            
            data.states.forEach( state => {
                dropdown[dropdown.length] = new Option(state.state, state.state_abbrev);
            });    
        }
        else {
            console.log("Could not get states");
        }
    }

    req.send();
}


function getCountries() {
    let req = new XMLHttpRequest();
    url = baseURL + "/info/countries";
    req.open("GET", url, true);

    req.onload = function () {
        let data = JSON.parse(this.response);

        if (req.status == 200) {
            let dropdown = document.getElementById("countrySelect");
            
            data.countries.forEach( country => {
                dropdown[dropdown.length] = new Option(country.country, country.country_abbrev);
            });    
        }
        else {
            console.log("Could not get countries");
        }
    }

    req.send();
}


// Populate the state and country dropdowns when the page is loaded
window.onload = function() {
    getStates();
    getCountries();
}