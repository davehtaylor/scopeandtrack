function createOrgFormSubmit() {
    let orgForm = document.getElementById("createOrgForm");
    let data = {};
    let req = new XMLHttpRequest();

    url = baseURL + "/organizations";
    req.open("POST", url, true);
    req.setRequestHeader("Content-Type", "application/json");

    for (let i = 0; i < orgForm.length; i++) {
        element = orgForm.elements[i];

        // Check for empty values and set them to null if they're just ""
        if (element.value != "") {
            newPair = { [element.name]: element.value };
        }
        else {
            newPair = { [element.name]: null };
        }
        
        // This loop wants to grab the Submit button too. Don't want that
        if (element.value != "Submit") {
            data = {...data, ...newPair};
        }
    }

    console.log("JSON data: " + JSON.stringify(data));

    req.onload = function () {
        console.log(req.response);
    }

    req.send(JSON.stringify(data));
    orgForm.reset();
}


function getAllOrgs() {
    let req = new XMLHttpRequest();
    url = baseURL + "/organizations";

    req.open("GET", url, true);

    req.onload = function () {

        // Get the JSON data
        let data = JSON.parse(this.response);

        if (req.status == 200) {
            // Add the data from the API call to the list on the profile page
            let ul = document.getElementById("orgList");
            let orgDiv = document.getElementById("orgs");

            data.organizations.forEach( organization => {
                let li = document.createElement("li");
                ul.appendChild(li);

                li.innerHTML += organization.name;
            });

            // Show the hidden div containing the list
            if (orgDiv.style.display === "none") {
                orgDiv.style.display = "block";
            }
            // Otherwise, hide the div and empty the list
            else {
                orgDiv.style.display = "none";
                orgList.innerHTML = "";
            }
        }
        else {
            console.log("Could not get organizations");
        }
    }

    req.send();
}


function getOrgByID(orgID) {
    let req = new XMLHttpRequest();
    url = baseURL + "/organizations" + orgID;


}

var modal = document.getElementById("orgModal");
var button = document.getElementById("modalButton");
var span = document.getElementById("close");

button.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
// function showOrgModal() {
//     console.log("showOrgModal() called");
//     let modal = document.getElementById("orgModal");
//     if (modal.style.display == "none") {
//         modal.style.display = "block";
//     }
// }


// function closeModal() {
//     console.log("closeModal() called");
//     let modal = document.getElementById("orgModal");
//     modal.style.display = "none";
// }


// window.onclick = function(event) {
//     let modal = document.getElementById("orgModal");
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }