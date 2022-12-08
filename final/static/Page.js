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

function Search(){
  var name = document.getElementById("movie-name").value
  var genre1 = document.getElementById("dropdown").value
  var genre2 = document.getElementById("dropdown2").value
  var genre3 = document.getElementById("dropdown3").value

  console.log(name)
  console.log(genre1)
  console.log(genre2)
  console.log(genre3)

  if (name =="" && genre1 == "None" && genre2 == "None" && genre3 == "None"){
    console.log("Nothing")
  } else if(name =="" && genre1 == "None" && genre2 == "None" && genre3 != "None"){
    console.log("1 Genre, Genre3")
  } else if(name =="" && genre1 == "None" && genre2 != "None" && genre3 == "None"){
    console.log("1 Genre, Genre2")
  } else if(name =="" && genre1 != "None" && genre2 == "None" && genre3 == "None"){
    console.log("1 Genre, Genre1")
  } else if(name =="" && genre1 == "None" && genre2 != "None" && genre3 != "None"){
    console.log("2 Genre, Genre 3 and 2")
  } else if(name =="" && genre1 != "None" && genre2 != "None" && genre3 == "None"){
    console.log("2 Genre, Genre 1 and 2")
  } else if(name =="" && genre1 != "None" && genre2 == "None" && genre3 != "None"){
    console.log("2 Genre, Genre 1 and 3")
  } else if(name =="" && genre1 != "None" && genre2 != "None" && genre3 != "None"){
    console.log("3 Genre")
  } else if (name !="" && genre1 == "None" && genre2 == "None" && genre3 == "None"){
    console.log("Name only")
    nameSearch()
  } else if(name !="" && genre1 == "None" && genre2 == "None" && genre3 != "None"){
    console.log("Name and Genre3")
  } else if(name !="" && genre1 == "None" && genre2 != "None" && genre3 == "None"){
    console.log("Name and Genre2")
  } else if(name !="" && genre1 != "None" && genre2 == "None" && genre3 == "None"){
    console.log("Name and Genre1")
  } else if(name !="" && genre1 == "None" && genre2 != "None" && genre3 != "None"){
    console.log("Name + Genre 3 and 2")
  } else if(name !="" && genre1 != "None" && genre2 != "None" && genre3 == "None"){
    console.log("Name + Genre 1 and 2")
  } else if(name !="" && genre1 != "None" && genre2 == "None" && genre3 != "None"){
    console.log("Name + Genre 1 and 3")
  } else if(name !="" && genre1 != "None" && genre2 != "None" && genre3 != "None"){
    console.log("Name + 3 Genres")
  }
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


async function nameSearch(){
  var name = document.getElementById("movie-name").value
  console.log("nameSearch")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "nameSearch/"+ name, true);
    xhttp.onload = function(){
      document.getElementById("display").innerHTML = this.responseText
    };
    
    xhttp.send(name);
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