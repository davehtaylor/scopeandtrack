let baseURL = "https://www.scopeandtrack.com/api"


function getAllOrgs() {
    let req = new XMLHttpRequest();
    url = baseURL + "/organizations";

    req.open("GET", url, true);

    req.onload = function () {

        // Get the JSON data
        let data = JSON.parse(this.response);

        if (req.status == 200) {
            data.organizations.forEach( organization => {
                console.log(organization.name + " " + organization.orgID)
            });
        }
        else {
            console.log("Could not get organizations");
        }
    }

    req.send();
}


function getOrgByID(orgID) {

}