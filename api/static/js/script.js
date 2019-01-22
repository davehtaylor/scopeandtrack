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
                dropdown[dropdown.length] = new Option(state.state_abbrev, state.state_abbrev);
                console.log(state.state_abbrev);
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
        let dropdown = document.getElementById("countrySelect")
    }

    req.send();
}