import {
  LitElement,
  html,
  css,
} from "https://cdn.jsdelivr.net/gh/lit/dist@3/core/lit-core.min.js";

import "https://cdn.jsdelivr.net/npm/chart.js";

class AUCPlotComponent extends LitElement {
  static properties = {
    answer: { type: Boolean },
    toggleEvent: { type: String },
  };

  static styles = css`
    .container {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #fff;
      flex-direction: column;
    }

    .container h1 {
      color: #444;
      margin-bottom: 50px;
      font-size: 30px;
      font-weight: 600;
    }

    .wrapper {
      height: 400px;
      width: 400px;
    }
  `;

  constructor() {
    super();
  }

  render() {
    return html`
      <div class="container">
        <h1>Area under curve y=x<sup>2</sup></h1>
        <div class="wrapper">
          <canvas id="myChart" width="100" height="100"></canvas>
        </div>
      </div>
    `;
  }

  _renderChart() {
    const ctx = this.shadowRoot.getElementById("myChart").getContext("2d");

    const data = {
      labels: Array.from({ length: 40 }, (_, i) => (i - 20) * 0.2), // X-axis labels from -5 to 5
      datasets: [
        {
          data: Array.from({ length: 40 }, (_, i) =>
            Math.pow((i - 20) * 0.2, 2)
          ), // Y-axis data
          fill: true,
          borderColor: "#ff8000",
          backgroundColor: (context) => {
            const chart = context.chart;
            const { ctx, chartArea } = chart;

            if (!chartArea) {
              return null;
            }

            const gradient = ctx.createLinearGradient(
              chartArea.left,
              0,
              chartArea.right,
              0
            );
            gradient.addColorStop(0.5, "rgba(255, 128, 0, 0)");
            gradient.addColorStop(0.5, "rgba(255, 128, 0, 0.2)");
            return gradient;
          },
          tension: 0.4,
        },
      ],
    };

    const config = {
      type: "line",
      data: data,
      options: {
        scales: {
          x: {
            type: "linear",
            position: "bottom",
          },
        },
        plugins: {
          legend: {
            display: false,
          },
        },
      },
      plugins: {
        filler: {
          propagate: false,
        },
      },
    };

    new Chart(ctx, config);
  }

  firstUpdated() {
    this._renderChart();
  }
}

customElements.define("aucplot-component", AUCPlotComponent);
