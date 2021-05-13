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


window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
    theme: "light2", // "light1", "light2", "dark1", "dark2"
    animationEnabled: true,
    title:{
        text: "Share Value - 2021"   
    },
    axisX: {
        interval: 1,
        intervalType: "month",
        valueFormatString: "MMM"
    },
    axisY:{
        title: "Price (in USD)",
        includeZero: true,
        valueFormatString: "$#0"
    },
    data: [{        
        type: "line",
        markerSize: 12,
        xValueFormatString: "MMM, YYYY",
        yValueFormatString: "$###.#",
        dataPoints: [        
            { x: new Date(2021, 00, 1), y: 61, indexLabel: "gain", markerType: "triangle",  markerColor: "#6B8E23" },
            { x: new Date(2021, 01, 1), y: 71, indexLabel: "gain", markerType: "triangle",  markerColor: "#6B8E23" },
            { x: new Date(2021, 02, 1) , y: 55, indexLabel: "loss", markerType: "cross", markerColor: "tomato" },
            { x: new Date(2021, 03, 1) , y: 50, indexLabel: "loss", markerType: "cross", markerColor: "tomato" },
            { x: new Date(2021, 04, 1) , y: 65, indexLabel: "gain", markerType: "triangle", markerColor: "#6B8E23" },
            { x: new Date(2021, 05, 1) , y: 85, indexLabel: "gain", markerType: "triangle", markerColor: "#6B8E23" },
            { x: new Date(2021, 06, 1) , y: 68, indexLabel: "loss", markerType: "cross", markerColor: "tomato" },
            { x: new Date(2021, 07, 1) , y: 28, indexLabel: "loss", markerType: "cross", markerColor: "tomato" },
            { x: new Date(2021, 08, 1) , y: 34, indexLabel: "gain", markerType: "triangle", markerColor: "#6B8E23" },
            { x: new Date(2021, 09, 1) , y: 24, indexLabel: "loss", markerType: "cross", markerColor: "tomato" },
            { x: new Date(2021, 10, 1) , y: 44, indexLabel: "gain", markerType: "triangle", markerColor: "#6B8E23" },
            { x: new Date(2021, 11, 1) , y: 99, indexLabel: "gain", markerType: "triangle", markerColor: "#6B8E23" }
        ]
    }]
});
chart.render();

}


