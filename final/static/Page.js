const url = "http://127.0.0.1:5000/"

async function filter() {
    
    fetch(url+"displayMovie", {
      method: "GET", 
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      
    })
    .then(response =>response.json())
    .then(data => DisplayData(data))
  }

function DisplayData(data){
  display = document.getElementById("display")
  while (display.firstChild) {
    display.removeChild(display.firstChild);
  }
  var entry = ""

  for (item in data){
    entry +="<br>"+ String(data[item]) + "<br>"
  }
  document.getElementById("display").innerHTML = entry;
}