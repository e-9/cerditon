$( document ).ready(function() {

  $.get('/cerdoton/graphData/weight/', function(data) {
        console.log(data);

        var data = {
          labels: ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"],
          datasets: data
        };

        var ctx = $("#weightChart").get(0).getContext("2d");
        var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

  });

  $('#myTab a').click(function (e) {
    e.preventDefault()

    if ($(this).text() === "Peso")
    {
      $.get('/cerdoton/graphData/weight/', function(data) {
            console.log(data);

            var data = {
              labels: ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"],
              datasets: data
            };

            var ctx = $("#weightChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }
    else if ($(this).text() === "Grasa")
    {
      $.get('/cerdoton/graphData/fat/', function(data) {
            console.log(data);

            var data = {
              labels: ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"],
              datasets: data
            };

            var ctx = $("#fatChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }
    else if ($(this).text() === "Músculo")
    {
      $.get('/cerdoton/graphData/muscle/', function(data) {
            console.log(data);

            var data = {
              labels: ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"],
              datasets: data
            };

            var ctx = $("#muscleChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }

    $(this).tab('show')
  })

});
