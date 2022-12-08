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
    .then(data => console.log(data))
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
    Genre1(genre3)
  } else if(name =="" && genre1 == "None" && genre2 != "None" && genre3 == "None"){
    console.log("1 Genre, Genre2")
    Genre1(genre2)
  } else if(name =="" && genre1 != "None" && genre2 == "None" && genre3 == "None"){
    console.log("1 Genre, Genre1")
    Genre1(genre1)
  } else if(name =="" && genre1 == "None" && genre2 != "None" && genre3 != "None"){
    console.log("2 Genre, Genre 3 and 2")
    Genre2(genre2,genre3)
  } else if(name =="" && genre1 != "None" && genre2 != "None" && genre3 == "None"){
    console.log("2 Genre, Genre 1 and 2")
    Genre2(genre1,genre2)
  } else if(name =="" && genre1 != "None" && genre2 == "None" && genre3 != "None"){
    console.log("2 Genre, Genre 1 and 3")
    Genre2(genre2,genre3)
  } else if(name =="" && genre1 != "None" && genre2 != "None" && genre3 != "None"){
    console.log("3 Genre")
    Genre3(genre1,genre2, genre3)
  } else if (name !="" && genre1 == "None" && genre2 == "None" && genre3 == "None"){
    console.log("Name only")
    nameSearch()
  } else if(name !="" && genre1 == "None" && genre2 == "None" && genre3 != "None"){
    console.log("Name and Genre3")
    nameAndGenre1(genre3)
  } else if(name !="" && genre1 == "None" && genre2 != "None" && genre3 == "None"){
    console.log("Name and Genre2")
    nameAndGenre1(genre2)
  } else if(name !="" && genre1 != "None" && genre2 == "None" && genre3 == "None"){
    console.log("Name and Genre1")
    nameAndGenre1(genre1)
  } else if(name !="" && genre1 == "None" && genre2 != "None" && genre3 != "None"){
    console.log("Name + Genre 3 and 2")
    nameAndGenre2(genre2,genre3)
  } else if(name !="" && genre1 != "None" && genre2 != "None" && genre3 == "None"){
    console.log("Name + Genre 1 and 2")
    nameAndGenre2(genre1,genre2)
  } else if(name !="" && genre1 != "None" && genre2 == "None" && genre3 != "None"){
    console.log("Name + Genre 1 and 3")
    nameAndGenre2(genre1,genre3)
  } else if(name !="" && genre1 != "None" && genre2 != "None" && genre3 != "None"){
    console.log("Name + 3 Genres")
    nameAndGenre3(genre1,genre2,genre3)
  }
}


function DisplayData(data){
  display = document.getElementById("display")
  while (display.firstChild) {
    display.removeChild(display.firstChild);
  }
  var entry = ""
  entry += '<tr>'
  entry += "<th>Movie Name</th>"
  entry += "<th>Adult(18+)</th>"
  entry += "<th>Release Year</th>"
  entry += "<th>Duration(mins)</th>"
  entry += "<th>Genre</th>"
  entry += "<th>Add Movie</th>"
  entry += "</tr>"
  data2 = []
  filter2 = []
  count = 0
  len = data.length
  console.log(len)
  for(item in data){
    small = data[item]
    if(item > 0 && item != data-1){
      small2 = data[item-1]
      if(small[0]==small2[0]){
        filter2.push(small2[4])
        small2[4] = ""
        console.log(filter2)
      } else {
        filter2.push(small2[4])
        small2[4] = ""
        small2[4] += filter2
        filter2 =[]
        console.log(small2)
      }
    }
    if(item == data.length-1){
      console.log("Final")
      filter2.push(small[4])
      small[4] =""
      small[4] += filter2
      filter2 = []
      console.log(small)
    }
    console.log(item)

  }
  console.log(data)

  for (item in data){
    small = data[item]
    if(small[4] == ""){

    }else{
      data2.push(small)
    }
  }
  console.log(data2)

  for (item in data2){
    small = data2[item]
    entry += "<tr>"
    entry +="<th>"+ small[0] + "<th>"
    entry +="<th>"+ small[1] + "<th>"
    entry +="<th>"+ small[2] + "<th>"
    entry +="<th>"+ small[3] + "<th>"
    entry +="<th>"+ small[4] + "<th>"
    entry += "<th>" + "<button onclick=addMovie(this)>Add Movie</button>" + "</th>"
    entry += "</tr>"
  }
  document.getElementById("display").innerHTML = entry;
}

function DisplayData2(data){
  

  
  var entry = ""
  entry += '<td>'
  entry += "<th>Movie Name</th>"
  entry += "<th>Adult(18+)</th>"
  entry += "<th>Release Year</th>"
  entry += "<th>Duration(mins)</th>"
  entry += "<th>Genre</th>"
  entry += "<th>Delete Movie</th>"
  entry += "</td>"
  data2 = []
  filter2 = []
  count = 0
  len = data.length
  console.log(len)
  for(item in data){
    small = data[item]
    if(item > 0 && item != data-1){
      small2 = data[item-1]
      if(small[0]==small2[0]){
        filter2.push(small2[4])
        small2[4] = ""
        console.log(filter2)
      } else {
        filter2.push(small2[4])
        small2[4] = ""
        small2[4] += filter2
        filter2 =[]
        console.log(small2)
      }
    }
    if(item == data.length-1){
      console.log("Final")
      filter2.push(small[4])
      small[4] =""
      small[4] += filter2
      filter2 = []
      console.log(small)
    }
    console.log(item)

  }
  console.log(data)

  for (item in data){
    small = data[item]
    if(small[4] == ""){

    }else{
      data2.push(small)
    }
  }
  console.log(data2)

  for (item in data2){
    small = data2[item]
    entry += "<tr>"
    entry +="<th>"+ small[0] + "<th>"
    entry +="<th>"+ small[1] + "<th>"
    entry +="<th>"+ small[2] + "<th>"
    entry +="<th>"+ small[3] + "<th>"
    entry +="<th>"+ small[4] + "<th>"
    entry += "<th>" + "<button onclick=deleteMovie(this)>delete Movie</button>" + "</th>"
    entry += "</tr>"
  }
  document.getElementById("display").innerHTML = entry;
}

function DisplayData3(data){
  console.log("DisplayData3 starting")
  display = document.getElementById("display2")
  while (display.firstChild) {
    display.removeChild(display.firstChild);
  }

  var entry = ""
  data2 = []
  filter2 = []
  count = 0
  len = data.length
  console.log(len)
  for(item in data){
    small = data[item]
    if(item > 0 && item != data-1){
      small2 = data[item-1]
      if(small[0]==small2[0]){
        filter2.push(small2[1])
        small2[1] = ""
        console.log(filter2)
      } else {
        filter2.push(small2[1])
        small2[1] = ""
        small2[1] += filter2
        filter2 =[]
        console.log(small2)
      }
    }
    if(item == data.length-1){
      console.log("Final")
      filter2.push(small[1])
      small[1] =""
      small[1] += filter2
      filter2 = []
      console.log(small)
    }
    console.log(item)

  }
  console.log(data)

  for (item in data){
    small = data[item]
    if(small[1] == ""){

    }else{
      data2.push(small)
    }
  }
  console.log(data2)

  for (item in data2){
    document.getElementById("display2").innerHTML += "<br>"
    document.getElementById("display2").innerHTML += data2[item]
    
    
  }
  
}

async function nameSearch(){
  var name = document.getElementById("movie-name").value
  console.log("nameSearch")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "nameSearch/"+ name, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(name);
}

async function nameAndGenre1(genre){
  var name = document.getElementById("movie-name").value

  console.log("Name and 1 Genre Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "NaG1/"+ name + "/"+genre, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(name,genre);
}

async function Genre1(genre){
  console.log("1 Genre Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "G1/"+genre, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(genre);
}

async function nameAndGenre2(genre,genre2){
  var name = document.getElementById("movie-name").value

  console.log("Name and 2 Genres Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "NaG2/"+ name + "/"+genre + "/" + genre2, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(name,genre,genre2);
}

async function Genre2(genre,genre2){
  console.log("2 Genre Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "G2/"+ genre +"/" + genre2, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(genre,genre2);
}


async function nameAndGenre3(genre,genre2,genre3){
  var name = document.getElementById("movie-name").value

  console.log("Name and 3 Genres Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "NaG3/"+ name + "/"+genre + "/" + genre2+ "/" + genre3, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(name,genre,genre2,genre3);
}

async function Genre3(genre,genre2, genre3){
  console.log("3 Genre Search")
  const xhttp = new XMLHttpRequest();
    xhttp.open('GET', url + "G3/"+ genre +"/" + genre2 + "/" + genre3, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      data = JSON.parse(this.responseText)
      console.log(data)
      DisplayData(data)
     
    };
    
    xhttp.send(genre,genre2,genre3);
}

async function addMovie(element){
  var name = document.getElementById("movie-name").value
  var num = element.parentNode.parentNode.rowIndex
  console.log("addMovie with" + name + " and row #" + num)
  const xhttp = new XMLHttpRequest();
    xhttp.open('POST', url + "addCurrentMovie/"+ name + "/" + num, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      alert(this.responseText)
     
    };
    
    xhttp.send(name,num);
}

async function deleteMovie(element){
  var num = element.parentNode.parentNode.rowIndex
  console.log("deleteMovie with and row #" + num)
  const xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', url + "deleteCurrentMovie/"+ num, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function(){

      alert(this.responseText)
     
    };
    
    xhttp.send(name,num);
}

async function DisplayList(){
  
  const xhttp = new XMLHttpRequest();
  xhttp.open('GET', url + "getList", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onload = function(){

    data = JSON.parse(this.responseText)
    console.log(data)
    DisplayData2(data)
  };
  xhttp.send();

  DisplayList2()

}

async function DisplayList2(){
  console.log("dispalylist2 triggered")
  const xhttp = new XMLHttpRequest();
  xhttp.open('GET', url + "getList2", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onload = function(){

    data = JSON.parse(this.responseText)
    console.log(data)
    DisplayData3(data)
  };
  xhttp.send();


}