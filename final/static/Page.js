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

//DROPDOWN BUTTON
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}