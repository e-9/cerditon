$( document ).ready(function() {

  $.get('/cerdoton/graphData/', function(data) {
        console.log(data);

        var data = {
          labels: ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"],
          datasets: data
        };

        var ctx = $("#myChart").get(0).getContext("2d");
        var myLineChart = new Chart(ctx).Line(data);

  });
});
