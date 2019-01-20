let baseURL = "https://www.scopeandtrack.com/api"


function getAllOrgs() {
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
            else {
                orgDiv.style.display = "none";
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