Plotly.d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json', function(redjson) {

  Plotly.d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json', function(bluejson) {

    Plotly.newPlot("graph", [{
      type: 'scattermapbox',
      lat: [46],
      lon: [-74]
    }], {
      title: "Florida Counties",
      height: 600,
      width: 600,
      mapbox: {
        center: {
          lat: 27.2,
          lon: -84
        },
        style: 'light',
        zoom: 5,
        layers: [
          {
            sourcetype: 'geojson',
            source: redjson,
            type: 'fill',
            color: 'rgba(163,22,19,0.8)'
          },
          {
            sourcetype: 'geojson',
            source: bluejson,
            type: 'fill',
            color: 'rgba(40,0,113,0.8)'
          },        
        ]
      }
    }, {
      mapboxAccessToken: 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiRy1GV1FoNCJ9.yUPu7qwD_Eqf_gKNzDrrCQ'
    });
      
    
});

});
