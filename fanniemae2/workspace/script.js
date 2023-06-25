function updatePlot() {
	// Load the data from the CSV file
	Plotly.d3.csv('Del1.csv', function(data) {
		// Extract the years and delinquency rates from the data
		var years = [];
		var delinquencyRates = [];
		for (var i = 0; i < data.length; i++) {
			years.push(data[i]['years']);
			delinquencyRates.push(data[i]['delinquency_rate']);
		}
		
		// Create a scatter plot of the data
		var trace1 = {
			x: years,
			y: delinquencyRates,
			mode: 'markers',
			type: 'scatter'
		};
		
		// Load the model from the JSON file
		Plotly.d3.json('model.json', function(model) {
			// Predict the delinquency rates for the years in the data
			var predictedDelinquencyRates = [];
			for (var i = 0; i < years.length; i++) {
				var year = years[i];
				var predictedDelinquencyRate = model['intercept'] + model['slope'] * year;
				predictedDelinquencyRates.push(predictedDelinquencyRate);
			}
			
			// Create a line plot of the predicted delinquency rates
			var trace2 = {
				x: years,
				y: predictedDelinquencyRates,
				mode: 'lines',
				type: 'scatter'
			};
			
			// Combine the scatter plot and line plot into a single plot
			var data = [trace1, trace2];
			var layout = {
				title: 'Delinquency Rates vs. Years',
				xaxis: {
					title: 'Years'
				},
				yaxis: {
					title: 'Delinquency Rates'
				}
			};
			Plotly.newPlot('plot', data, layout);
		});
	});
}
