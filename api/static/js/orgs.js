let baseURL = "https://www.scopeandtrack.com/api"


function createOrgFormSubmit() {
    console.log("createOrgFormSubmit() function called");

    let orgForm = document.getElementById("createOrgForm");
    let req = new XMLHttpRequest();
    url = baseURL + "/organizations";
    req.open("POST", url, true);

    // let formData = new FormData(document.getElementById("createOrgForm"));
    // console.log(formData);

    let data = {};

    for (let i = 0; i < orgForm.length; i++) {
        data[item.elements[i].name] = item.elements[i].value;
        console.log(orgForm.elements[i].name + " " + orgForm.elements[i].value);
    }

    console.log("Data: " + data);

    req.onload = function () {
        console.log(req.response);
    }

    req.send(JSON.stringify(data));
}


function getAllOrgs() {
    console.log("getAllOrgs() function called");

    let req = new XMLHttpRequest();
    url = baseURL + "/organizations";

    req.open("GET", url, true);

    req.onload = function () {

        // Get the JSON data
        let data = JSON.parse(this.response);

        if (req.status == 200) {
            // data.organizations.forEach( organization => {
            //     console.log(organization.name + " " + organization.orgID)
            // });

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
    url = baseURL + "/organizations/" + orgID;


}