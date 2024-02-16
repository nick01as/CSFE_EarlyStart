const ipDisplay = document.getElementById('ipInfo')
async function fetchData(){
    ipDisplay.innerText = "";
    const ip_address = document.getElementById("ipAddress").value;
    const IP_URL = `https://ipapi.co/${ip_address}/json/`

    fetch(IP_URL)
        .then(response => response.json())
        .then(responseJson => {
            let loc = responseJson['city'] + ", " + responseJson['region'] + ", " + responseJson['country'];
            const ipLoc = document.createElement('h2');
            console.log(responseJson['city']);
            if(responseJson['city'] == undefined){
                ipLoc.innerText = "Not a Valid IP Address";
                ipDisplay.append(ipLoc);
            }
            else{
                ipLoc.innerText = loc;
                ipDisplay.append(ipLoc);
            }
        })

}
