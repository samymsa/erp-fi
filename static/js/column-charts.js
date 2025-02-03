function getColumnChartOptions(produits, charges) {
  return {
    colors: ["#31C48D", "#F05252"],
    series: [
      {
        name: "Produits",
        color: "#31C48D",
        data: produits,
      },
      {
        name: "Charges",
        color: "#F05252",
        data: charges,
      },
    ],
    chart: {
      type: "bar",
      height: "320px",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "70%",
        borderRadiusApplication: "end",
        borderRadius: 8,
      },
    },
    tooltip: {
      shared: true,
      intersect: false,
      style: {
        fontFamily: "Inter, sans-serif",
      },
    },
    states: {
      hover: {
        filter: {
          type: "darken",
          value: 1,
        },
      },
    },
    stroke: {
      show: true,
      width: 0,
      colors: ["transparent"],
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: -14,
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    xaxis: {
      floating: false,
      labels: {
        show: true,
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: "text-xs font-normal fill-gray-500 dark:fill-gray-400",
        },
        formatter: function (value) {
          return value.slice(0, 4);
        },
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  };
}

function getRentabiliteProjets(projets) {
  let produits = [];
  let charges = [];
  let rentabilite = [];

  for (let i = 0; i < projets.length; i++) {
    produits.push({
      x: projets[i].id,
      y: projets[i].ca,
    });
    charges.push({
      x: projets[i].id,
      y: projets[i].charges,
    });
    rentabilite.push({
      x: projets[i].id,
      y: projets[i].rentabilite,
    });
  }

  return [produits, charges, rentabilite];
}

if (
  document.getElementById("column-chart") &&
  typeof ApexCharts !== "undefined"
) {
  const rentabiliteProjet = document.getElementById("rentabilite-projet");

  fetch(window.location.origin + "/rentabilite_projet/all")
    .then((response) => response.json())
    .then((projets) => {
      [produits, charges, rentabilite] = getRentabiliteProjets(projets);
      sumProduits = produits.reduce((acc, cur) => acc + cur.y, 0);
      sumCharges = charges.reduce((acc, cur) => acc + cur.y, 0);
      sumRentabilite = rentabilite.reduce((acc, cur) => acc + cur.y, 0);
      roi = (sumRentabilite / sumCharges) * 100;

      rentabiliteProjet.textContent = roi.toFixed(2) + " %";

      const options = getColumnChartOptions(produits, charges);
      const chart = new ApexCharts(
        document.getElementById("column-chart"),
        options
      );
      chart.render();
    });
}
