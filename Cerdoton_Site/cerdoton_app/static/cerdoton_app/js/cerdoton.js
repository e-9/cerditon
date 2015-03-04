$( document ).ready(function() {

  function compare(a,b) {
    if (a.label < b.label)
       return -1;
    if (a.label > b.label)
      return 1;
    return 0;
  }

  var labelArray = ["Inicio", "Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8"];

  $.get('/cerdoton/graphData/weight/', function(data) {
        data.sort(compare);

        var data = {
          labels: labelArray,
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
            data.sort(compare);

            var data = {
              labels: labelArray,
              datasets: data
            };

            var ctx = $("#weightChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }
    else if ($(this).text() === "Grasa")
    {
      $.get('/cerdoton/graphData/fat/', function(data) {
            data.sort(compare);

            var data = {
              labels: labelArray,
              datasets: data
            };

            var ctx = $("#fatChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }
    else if ($(this).text() === "Músculo")
    {
      $.get('/cerdoton/graphData/muscle/', function(data) {
            data.sort(compare);

            var data = {
              labels: labelArray,
              datasets: data
            };

            var ctx = $("#muscleChart").get(0).getContext("2d");
            var myLineChart = new Chart(ctx).Line(data, {datasetFill : false});

      });
    }

    $(this).tab('show')
  });

});
