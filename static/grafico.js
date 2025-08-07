let chart;

async function carregarDados() {
	const resposta = await fetch("/dados");
	const dados = await resposta.json();
	const labels = dados.map(d => d.timestamp);
	const values = dados.map(d => d.valor);

	if (!chart) {
		const ctx = document.getElementById('grafico').getContext('2d');
		chart = new Chart(ctx, {
			type: 'line',
			data: {
				labels: labels,
				datasets: [{
					label: 'Valores simulados',
					data: values,
					borderColor: 'blue',
					tension: 0.2
				}]
			},
			options: {
				responsive: true,
				scales: {
					y: { title: { display: true, text: 'Valor' } }
				}
			}
		});
	} else {
		chart.data.labels = labels;
		chart.data.datasets[0].data = values;
		chart.update();
	}
}
carregarDados();
setInterval(carregarDados, 10000);
