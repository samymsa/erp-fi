function getBarChartOptions(
  category,
  positive,
  negative,
  positiveLabel,
  negativeLabel
) {
  return {
    series: [
      {
        name: positiveLabel,
        color: "#31C48D",
        data: [positive],
      },
      {
        name: negativeLabel,
        data: [negative],
        color: "#F05252",
      },
    ],
    chart: {
      sparkline: {
        enabled: false,
      },
      type: "bar",
      width: "100%",
      height: 150,
      toolbar: {
        show: false,
      },
    },
    fill: {
      opacity: 1,
    },
    plotOptions: {
      bar: {
        horizontal: true,
        columnWidth: "100%",
        borderRadiusApplication: "end",
        borderRadius: 6,
        dataLabels: {
          position: "top",
        },
      },
    },
    legend: {
      show: true,
      position: "bottom",
    },
    dataLabels: {
      enabled: false,
    },
    tooltip: {
      shared: false,
      intersect: true,
      formatter: function (value) {
        return value.toFixed(2) + " €";
      },
    },
    xaxis: {
      labels: {
        show: true,
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: "text-xs font-normal fill-gray-500 dark:fill-gray-400",
        },
        formatter: function (value) {
          return value;
        },
      },
      categories: [category],
      axisTicks: {
        show: true,
      },
      axisBorder: {
        show: false,
      },
    },
    yaxis: {
      labels: {
        show: false,
      },
    },
    grid: {
      show: true,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: -20,
      },
    },
    fill: {
      opacity: 1,
    },
  };
}

if (document.getElementById("tva-chart") && typeof ApexCharts !== "undefined") {
  const tvaCollectee = document.getElementById("tva-collectee");
  const tvaDeductible = document.getElementById("tva-deductible");
  const tvaADeclarer = document.getElementById("tva-a-declarer");

  fetch(window.location.origin + "/tva")
    .then((response) => response.json())
    .then(({ collectee, deductible, a_declarer }) => {
      tvaCollectee.textContent = collectee.toFixed(2) + " €";
      tvaDeductible.textContent = (-deductible).toFixed(2) + " €";
      tvaADeclarer.textContent = a_declarer.toFixed(2) + " €";
      const options = getBarChartOptions(
        "TVA",
        collectee,
        deductible,
        "TVA Collectée",
        "TVA Déductible"
      );
      const chart = new ApexCharts(
        document.getElementById("tva-chart"),
        options
      );
      chart.render();
    });
}

if (document.getElementById("cr-chart") && typeof ApexCharts !== "undefined") {
  const cr = document.getElementById("cr");
  const crProduits = document.getElementById("cr-produits");
  const crCharges = document.getElementById("cr-charges");

  fetch(window.location.origin + "/compte_resultat")
    .then((response) => response.json())
    .then(({ charges, produits, resultat }) => {
      crProduits.textContent = produits.toFixed(2) + " €";
      crCharges.textContent = (-charges).toFixed(2) + " €";
      cr.textContent = resultat.toFixed(2) + " €";
      const options = getBarChartOptions(
        "Compte de résultat",
        produits,
        charges,
        "Produits",
        "Charges"
      );
      const chart = new ApexCharts(
        document.getElementById("cr-chart"),
        options
      );
      chart.render();
    });
}
